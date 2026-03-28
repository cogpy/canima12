#!/usr/bin/env python3
"""
Download manufacturing BOM and formulation attachments from Cloudflare R2.
Searches the exchange-attachments bucket for BOM-related files,
downloads them, and organizes into comcosys and fincosys repos.
"""
import boto3
import hashlib
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from botocore.config import Config

# R2 Config
S3_ENDPOINT = os.environ.get("S3EP", "")
ACCESS_KEY = os.environ.get("AKID", "")
SECRET_KEY = os.environ.get("AKSE", "")
BUCKET = "exchange-attachments"

# Repo roots
COMCOSYS = Path("/home/ubuntu/comcosys")
FINCOSYS = Path("/home/ubuntu/fincosys")

# BOM-related search terms (case-insensitive)
BOM_TERMS = [
    "bom", "formul", "price list", "price_list", "pricelist",
    "strategic logistics", "prime product", "raw material",
    "ingredient", "recipe", "inci", "cosmetic listing",
]

# File extensions to download (skip tiny inline images)
GOOD_EXTS = {".pdf", ".xlsx", ".xls", ".csv", ".doc", ".docx", ".zip", ".pptx"}


def safe_filename(name):
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', name or "attachment")
    return name.strip('. ')[:200] or "attachment"


def extract_user_from_key(key):
    """Extract user email from R2 key like tenant_id/user_at_domain/..."""
    parts = key.split("/")
    if len(parts) >= 2:
        user_part = parts[1]
        if "_at_" in user_part:
            return user_part.replace("_at_", "@")
    return "unknown"


def main():
    if not all([S3_ENDPOINT, ACCESS_KEY, SECRET_KEY]):
        print("ERROR: R2 credentials not set (S3EP, AKID, AKSE)")
        sys.exit(1)

    s3 = boto3.client(
        "s3",
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        config=Config(signature_version="s3v4"),
        region_name="auto",
    )

    print(f"[SCAN] Scanning R2 bucket '{BUCKET}' for BOM-related files...")
    paginator = s3.get_paginator("list_objects_v2")
    
    bom_files = []
    scanned = 0
    
    for page in paginator.paginate(Bucket=BUCKET):
        for obj in page.get("Contents", []):
            scanned += 1
            key = obj["Key"]
            key_lower = key.lower()
            
            # Match BOM-related files
            if any(term in key_lower for term in BOM_TERMS):
                # Extract filename from key
                fname = key.split("/")[-1]
                # Remove the attachment ID prefix (e.g., "AQMkAGM2_")
                if "_" in fname and len(fname.split("_")[0]) > 6:
                    fname = "_".join(fname.split("_")[1:])
                
                ext = Path(fname).suffix.lower()
                
                # Skip tiny images and non-document files
                if ext in GOOD_EXTS or (ext in (".png", ".jpg") and obj["Size"] > 50000):
                    bom_files.append({
                        "key": key,
                        "size": obj["Size"],
                        "filename": fname,
                        "user": extract_user_from_key(key),
                        "last_modified": obj["LastModified"].isoformat(),
                    })
        
        if scanned % 10000 == 0:
            print(f"  Scanned {scanned:,} objects, found {len(bom_files)} BOM files so far...")
    
    print(f"[SCAN] Complete: scanned {scanned:,} objects, found {len(bom_files)} BOM-related files")
    
    if not bom_files:
        print("[DONE] No BOM files found in R2")
        return
    
    # Download each file
    stats = {"downloaded": 0, "errors": 0, "total_bytes": 0, "skipped": 0}
    manifest = []
    
    for i, bf in enumerate(bom_files):
        fname = safe_filename(bf["filename"])
        user = bf["user"]
        size = bf["size"]
        
        print(f"  [{i+1}/{len(bom_files)}] {fname} ({size:,} bytes) from {user}")
        
        try:
            resp = s3.get_object(Bucket=BUCKET, Key=bf["key"])
            binary = resp["Body"].read()
        except Exception as e:
            print(f"    ERROR: {e}")
            stats["errors"] += 1
            continue
        
        sha256 = hashlib.sha256(binary).hexdigest()
        
        # Determine year from last_modified
        year = bf["last_modified"][:4]
        
        # Save to comcosys
        comcosys_dir = COMCOSYS / f"financial_docs/manufacturing_bom/{year}"
        comcosys_dir.mkdir(parents=True, exist_ok=True)
        comcosys_path = comcosys_dir / fname
        
        # Deduplicate by checking if file already exists with same size
        if comcosys_path.exists() and comcosys_path.stat().st_size == size:
            stats["skipped"] += 1
            continue
        
        # Handle name collisions
        counter = 1
        orig_path = comcosys_path
        while comcosys_path.exists():
            stem = orig_path.stem
            suffix = orig_path.suffix
            comcosys_path = comcosys_dir / f"{stem}_{counter}{suffix}"
            counter += 1
        
        comcosys_path.write_bytes(binary)
        
        # Write metadata sidecar
        meta = {
            "r2_key": bf["key"],
            "r2_bucket": BUCKET,
            "doc_type": "manufacturing_bom",
            "user_email": user,
            "filename": bf["filename"],
            "file_size": size,
            "sha256": sha256,
            "downloaded_from": "r2",
            "downloaded_at": datetime.utcnow().isoformat(),
        }
        meta_path = comcosys_path.with_suffix(comcosys_path.suffix + ".meta.json")
        meta_path.write_text(json.dumps(meta, indent=2))
        
        # Save to fincosys
        fincosys_dir = FINCOSYS / f"data/documents/manufacturing/{year}"
        fincosys_dir.mkdir(parents=True, exist_ok=True)
        fincosys_path = fincosys_dir / fname
        counter = 1
        orig_path2 = fincosys_path
        while fincosys_path.exists():
            stem = orig_path2.stem
            suffix = orig_path2.suffix
            fincosys_path = fincosys_dir / f"{stem}_{counter}{suffix}"
            counter += 1
        fincosys_path.write_bytes(binary)
        
        manifest.append({
            "filename": fname,
            "comcosys_path": str(comcosys_path.relative_to(COMCOSYS)),
            "fincosys_path": str(fincosys_path.relative_to(FINCOSYS)),
            "r2_key": bf["key"],
            "size": size,
            "sha256": sha256,
            "user": user,
        })
        
        stats["downloaded"] += 1
        stats["total_bytes"] += size
    
    # Save manifest
    manifest_path = COMCOSYS / "financial_docs/manufacturing_bom/download_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    
    mb = stats["total_bytes"] / (1024 * 1024)
    print(f"\n{'='*60}")
    print(f"[DONE] Downloaded: {stats['downloaded']} files")
    print(f"       Skipped:    {stats['skipped']} (already exist)")
    print(f"       Errors:     {stats['errors']}")
    print(f"       Total size: {mb:.1f} MB")
    print(f"       Manifest:   {manifest_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
