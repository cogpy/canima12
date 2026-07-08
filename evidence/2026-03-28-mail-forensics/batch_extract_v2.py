#!/usr/bin/env python3
"""
Forensic Batch Extraction v2 — Downloads financial document attachments from R2
using the correct R2 keys stored in exchange_sync.attachments table.
"""
import psycopg2, psycopg2.extras, boto3, os, json, re, shutil
from botocore.config import Config
from datetime import datetime
from pathlib import Path

CONNECT = os.environ["CONNECT"]
R2_EP = os.environ.get("S3EP", "")
R2_AK = os.environ.get("AKID", "")
R2_SK = os.environ.get("AKSE", "")
BUCKET = "exchange-attachments"
COMCOSYS = "/home/ubuntu/comcosys"
FINCOSYS = "/home/ubuntu/fincosys"

def get_s3():
    return boto3.client('s3',
        endpoint_url=R2_EP,
        aws_access_key_id=R2_AK,
        aws_secret_access_key=R2_SK,
        config=Config(signature_version='s3v4'),
        region_name='auto'
    )

def sanitize(name, maxlen=150):
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', name)
    return name[:maxlen]

def download_batch(conn, s3, batch_name, priority, sql_query, comcosys_subdir, fincosys_subdir):
    """Download a batch of attachments from R2 using keys from the DB"""
    print(f"\n{'='*70}")
    print(f"BATCH: {batch_name} (Priority {priority})")
    print(f"{'='*70}")
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_query)
    rows = cur.fetchall()
    print(f"  Found {len(rows)} attachment records with R2 keys")
    
    if not rows:
        # Save empty manifest
        mdir = Path(COMCOSYS) / "financial_docs" / comcosys_subdir
        mdir.mkdir(parents=True, exist_ok=True)
        with open(mdir / "download_manifest.json", 'w') as f:
            json.dump({"batch": batch_name, "priority": priority, "total": 0, "downloaded": 0, "timestamp": datetime.utcnow().isoformat()}, f, indent=2)
        return 0
    
    comcosys_dir = Path(COMCOSYS) / "financial_docs" / comcosys_subdir
    fincosys_dir = Path(FINCOSYS) / "data" / "documents" / fincosys_subdir
    comcosys_dir.mkdir(parents=True, exist_ok=True)
    fincosys_dir.mkdir(parents=True, exist_ok=True)
    
    downloaded = 0
    skipped = 0
    errors = 0
    manifest = []
    
    for row in rows:
        r2_key = row['r2_key']
        att_name = row['att_name'] or 'unknown'
        fname = sanitize(att_name)
        doc_type = row.get('doc_type', 'unknown')
        subject = row.get('subject', '')
        
        # Deduplicate by adding a short hash if file exists with different content
        comcosys_path = comcosys_dir / fname
        if comcosys_path.exists():
            # Check size match
            existing_size = comcosys_path.stat().st_size
            if existing_size == (row.get('att_size') or 0):
                skipped += 1
                continue
            # Different file, add suffix
            stem = comcosys_path.stem
            suffix = comcosys_path.suffix
            fname = f"{stem}_{row['att_id'][:8]}{suffix}"
            comcosys_path = comcosys_dir / fname
        
        fincosys_path = fincosys_dir / fname
        
        try:
            s3.download_file(BUCKET, r2_key, str(comcosys_path))
            shutil.copy2(str(comcosys_path), str(fincosys_path))
            downloaded += 1
            
            manifest.append({
                'filename': fname,
                'r2_key': r2_key,
                'size': row.get('att_size', 0),
                'content_type': row.get('content_type', ''),
                'subject': (subject or '')[:200],
                'doc_type': doc_type,
                'message_id': row.get('message_id', ''),
                'attachment_id': row.get('att_id', ''),
            })
            
            if downloaded % 25 == 0:
                print(f"    Downloaded {downloaded} files...")
                
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"    ERROR: {fname[:60]}: {e}")
    
    # Save manifest
    with open(comcosys_dir / "download_manifest.json", 'w') as f:
        json.dump({
            'batch': batch_name,
            'priority': priority,
            'total_records': len(rows),
            'downloaded': downloaded,
            'skipped': skipped,
            'errors': errors,
            'timestamp': datetime.utcnow().isoformat(),
            'files': manifest
        }, f, indent=2)
    
    print(f"  RESULT: {downloaded} downloaded, {skipped} skipped, {errors} errors")
    return downloaded


def main():
    conn = psycopg2.connect(CONNECT)
    s3 = get_s3()
    results = {}
    
    # ============================================================
    # PRIORITY 1: CRITICAL
    # ============================================================
    
    # P1.1: Purchase Orders 2025-2026
    results['P1.1 POs 2025-26'] = download_batch(conn, s3,
        "P1.1: Purchase Orders 2025-2026", 1,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type, 
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'purchase_order'
          AND a.r2_key IS NOT NULL
          AND m.received_datetime >= '2025-01-01'
        ORDER BY m.received_datetime DESC
        """,
        "priority1_purchase_orders_2025",
        "procurement/purchase_orders/2025"
    )
    
    # P1.2: All regimaskin.co.za documents
    results['P1.2 regimaskin'] = download_batch(conn, s3,
        "P1.2: regimaskin.co.za Documents", 1,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE a.r2_key IS NOT NULL
          AND m.from_address LIKE '%regimaskin%'
        ORDER BY m.received_datetime DESC
        """,
        "priority1_regimaskin",
        "forensic/regimaskin"
    )
    
    # P1.3: Bank Statements (CRITICAL for fund flow tracing)
    results['P1.3 Bank Stmts'] = download_batch(conn, s3,
        "P1.3: Bank Statements (ALL)", 1,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'bank_statement'
          AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC
        """,
        "priority1_bank_statements",
        "banking/statements"
    )
    
    # ============================================================
    # PRIORITY 2: HIGH
    # ============================================================
    
    # P2.1: Intercompany Invoices
    results['P2.1 IC Invoices'] = download_batch(conn, s3,
        "P2.1: Intercompany Invoices", 2,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'invoice'
          AND a.r2_key IS NOT NULL
          AND (LOWER(a.name) LIKE '%strategic%' 
               OR LOWER(a.name) LIKE '%villa via%'
               OR LOWER(a.name) LIKE '%regima world%'
               OR LOWER(a.name) LIKE '%rww%'
               OR LOWER(a.name) LIKE '%derm%'
               OR LOWER(a.name) LIKE '%intercompany%'
               OR LOWER(m.subject) LIKE '%strategic%logistics%'
               OR LOWER(m.subject) LIKE '%villa via%'
               OR LOWER(m.subject) LIKE '%regima worldwide%')
        ORDER BY m.received_datetime DESC
        """,
        "priority2_intercompany_invoices",
        "forensic/intercompany_invoices"
    )
    
    # P2.2: Raw Materials
    results['P2.2 Raw Materials'] = download_batch(conn, s3,
        "P2.2: Raw Materials Records", 2,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'raw_materials'
          AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC
        """,
        "priority2_raw_materials",
        "manufacturing/raw_materials"
    )
    
    # P2.3: All remaining invoices with R2 keys (bulk)
    results['P2.3 Invoices (R2)'] = download_batch(conn, s3,
        "P2.3: All Invoices in R2", 2,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'invoice'
          AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC
        """,
        "priority2_all_invoices",
        "accounting/invoices"
    )
    
    # ============================================================
    # PRIORITY 3: MEDIUM
    # ============================================================
    
    # P3.1: Credit Notes 2022
    results['P3.1 CN 2022'] = download_batch(conn, s3,
        "P3.1: Credit Notes 2022 Spike", 3,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'credit_note'
          AND a.r2_key IS NOT NULL
          AND EXTRACT(YEAR FROM m.received_datetime) = 2022
        ORDER BY m.received_datetime DESC
        """,
        "priority3_credit_notes_2022",
        "accounting/credit_notes/2022"
    )
    
    # P3.2: Customs/Trade
    results['P3.2 Customs'] = download_batch(conn, s3,
        "P3.2: Customs & Trade Documents", 3,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'customs_trade'
          AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC
        """,
        "priority3_customs_trade",
        "trade/customs"
    )
    
    # P3.3: Quotations
    results['P3.3 Quotations'] = download_batch(conn, s3,
        "P3.3: Quotations", 3,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'quotation'
          AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC
        """,
        "priority3_quotations",
        "accounting/quotations"
    )
    
    # P3.4: Receipts
    results['P3.4 Receipts'] = download_batch(conn, s3,
        "P3.4: Receipts", 3,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'receipt'
          AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC
        """,
        "priority3_receipts",
        "accounting/receipts"
    )
    
    # P3.5: Delivery Notes
    results['P3.5 Delivery Notes'] = download_batch(conn, s3,
        "P3.5: Delivery Notes", 3,
        """
        SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'delivery_note'
          AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC
        """,
        "priority3_delivery_notes",
        "logistics/delivery_notes"
    )
    
    conn.close()
    
    # Summary
    print(f"\n{'='*70}")
    print("EXTRACTION SUMMARY")
    print(f"{'='*70}")
    grand = 0
    for name, count in results.items():
        print(f"  {name:25s}: {count:5d} files")
        grand += count
    print(f"  {'GRAND TOTAL':25s}: {grand:5d} files")
    
    # Save summary
    with open(Path(COMCOSYS) / "financial_docs" / "extraction_summary.json", 'w') as f:
        json.dump({
            'timestamp': datetime.utcnow().isoformat(),
            'grand_total': grand,
            'batches': results
        }, f, indent=2)

if __name__ == "__main__":
    main()
