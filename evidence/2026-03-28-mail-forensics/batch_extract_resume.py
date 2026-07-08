#!/usr/bin/env python3
"""
Resumable Forensic Batch Extraction — Downloads from R2 with DB reconnect.
Skips already-downloaded files by checking filesystem.
"""
import psycopg2, psycopg2.extras, boto3, os, json, re, shutil, time
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
        endpoint_url=R2_EP, aws_access_key_id=R2_AK, aws_secret_access_key=R2_SK,
        config=Config(signature_version='s3v4'), region_name='auto')

def get_db():
    return psycopg2.connect(CONNECT)

def sanitize(name, maxlen=150):
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', name)[:maxlen]

BATCHES = [
    ("P1.3 Bank Stmts", 1, "priority1_bank_statements", "banking/statements",
     """SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'bank_statement' AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC"""),
    ("P2.1 IC Invoices", 2, "priority2_intercompany_invoices", "forensic/intercompany_invoices",
     """SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'invoice' AND a.r2_key IS NOT NULL
          AND (LOWER(a.name) LIKE '%strategic%' OR LOWER(a.name) LIKE '%villa via%'
               OR LOWER(a.name) LIKE '%regima world%' OR LOWER(a.name) LIKE '%rww%'
               OR LOWER(a.name) LIKE '%derm%' OR LOWER(a.name) LIKE '%intercompany%'
               OR LOWER(m.subject) LIKE '%strategic%logistics%'
               OR LOWER(m.subject) LIKE '%villa via%'
               OR LOWER(m.subject) LIKE '%regima worldwide%')
        ORDER BY m.received_datetime DESC"""),
    ("P2.2 Raw Materials", 2, "priority2_raw_materials", "manufacturing/raw_materials",
     """SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'raw_materials' AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC"""),
    ("P2.3 All Invoices", 2, "priority2_all_invoices", "accounting/invoices",
     """SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'invoice' AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC"""),
    ("P3.1 CN 2022", 3, "priority3_credit_notes_2022", "accounting/credit_notes/2022",
     """SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'credit_note' AND a.r2_key IS NOT NULL
          AND EXTRACT(YEAR FROM m.received_datetime) = 2022
        ORDER BY m.received_datetime DESC"""),
    ("P3.2 Customs", 3, "priority3_customs_trade", "trade/customs",
     """SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'customs_trade' AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC"""),
    ("P3.3 Quotations", 3, "priority3_quotations", "accounting/quotations",
     """SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'quotation' AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC"""),
    ("P3.4 Receipts", 3, "priority3_receipts", "accounting/receipts",
     """SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'receipt' AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC"""),
    ("P3.5 Delivery Notes", 3, "priority3_delivery_notes", "logistics/delivery_notes",
     """SELECT a.id as att_id, a.message_id, a.name as att_name, a.content_type,
               a.size as att_size, a.r2_key, f.doc_type, m.subject
        FROM exchange_sync.attachments a
        JOIN exchange_sync.financial_doc_downloads f ON f.message_id = a.message_id
        JOIN exchange_sync.messages m ON m.id = a.message_id
        WHERE f.doc_type = 'delivery_note' AND a.r2_key IS NOT NULL
        ORDER BY m.received_datetime DESC"""),
]

def run_batch(name, priority, comcosys_sub, fincosys_sub, sql):
    print(f"\n{'='*70}")
    print(f"BATCH: {name} (Priority {priority})")
    print(f"{'='*70}")
    
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    
    print(f"  Found {len(rows)} attachment records")
    
    cdir = Path(COMCOSYS) / "financial_docs" / comcosys_sub
    fdir = Path(FINCOSYS) / "data" / "documents" / fincosys_sub
    cdir.mkdir(parents=True, exist_ok=True)
    fdir.mkdir(parents=True, exist_ok=True)
    
    s3 = get_s3()
    dl, skip, err = 0, 0, 0
    manifest = []
    
    for row in rows:
        fname = sanitize(row['att_name'] or 'unknown')
        cpath = cdir / fname
        
        if cpath.exists():
            skip += 1
            continue
        
        try:
            s3.download_file(BUCKET, row['r2_key'], str(cpath))
            fpath = fdir / fname
            shutil.copy2(str(cpath), str(fpath))
            dl += 1
            manifest.append({
                'filename': fname, 'r2_key': row['r2_key'],
                'size': row.get('att_size', 0), 'doc_type': row.get('doc_type', ''),
                'subject': (row.get('subject') or '')[:200],
            })
            if dl % 50 == 0:
                print(f"    Downloaded {dl} files...")
        except Exception as e:
            err += 1
            if err <= 3:
                print(f"    ERROR: {str(e)[:100]}")
    
    with open(cdir / "download_manifest.json", 'w') as f:
        json.dump({'batch': name, 'priority': priority, 'total': len(rows),
                   'downloaded': dl, 'skipped': skip, 'errors': err,
                   'timestamp': datetime.utcnow().isoformat(), 'files': manifest}, f, indent=2)
    
    print(f"  RESULT: {dl} downloaded, {skip} skipped, {err} errors")
    return dl

results = {}
for name, pri, csub, fsub, sql in BATCHES:
    try:
        results[name] = run_batch(name, pri, csub, fsub, sql)
    except Exception as e:
        print(f"  BATCH FAILED: {e}")
        results[name] = -1
        time.sleep(2)

print(f"\n{'='*70}")
print("EXTRACTION SUMMARY")
print(f"{'='*70}")
grand = 0
for n, c in results.items():
    print(f"  {n:25s}: {c:5d} files")
    if c > 0: grand += c
print(f"  {'GRAND TOTAL':25s}: {grand:5d} files")

with open(Path(COMCOSYS) / "financial_docs" / "extraction_summary.json", 'w') as f:
    json.dump({'timestamp': datetime.utcnow().isoformat(), 'grand_total': grand, 'batches': results}, f, indent=2)
