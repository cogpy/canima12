#!/usr/bin/env python3
"""Cross-platform forensic audit analysis — Exchange + Gmail unified report."""
import json, os, glob, hashlib
from collections import defaultdict, Counter
from datetime import datetime

BASE = "/home/ubuntu/revstream1/docs/evidence/forensics"

def load_audit_files(platform_dir):
    """Load all .audit.json files from a platform directory tree."""
    audits = []
    for f in sorted(glob.glob(os.path.join(platform_dir, "**/*.audit.json"), recursive=True)):
        try:
            with open(f) as fh:
                data = json.load(fh)
                data["_source_file"] = f
                data["_scope"] = os.path.basename(os.path.dirname(f))
                audits.append(data)
        except Exception as e:
            print(f"  WARN: {f}: {e}")
    return audits

def extract_auth(audit):
    """Extract authentication verdicts from an audit JSON."""
    auth = audit.get("authentication", {}) or {}
    result = {}
    for k in ["spf", "dkim", "dmarc"]:
        val = auth.get(k)
        if val is None:
            result[k] = "unknown"
        elif isinstance(val, dict):
            result[k] = (val.get("result", "") or "unknown").lower()
        elif isinstance(val, str):
            result[k] = val.lower() if val else "unknown"
        else:
            result[k] = "unknown"
    return result

def extract_hops(audit):
    """Extract transport hop count and TLS info."""
    hops = audit.get("transport_hops", [])
    tls_count = sum(1 for h in hops if h.get("tls"))
    return {"total": len(hops), "tls": tls_count, "non_tls": len(hops) - tls_count}

def extract_envelope(audit):
    """Extract envelope info."""
    env = audit.get("envelope", {})
    return {
        "from": env.get("from", ""),
        "to": env.get("to", ""),
        "subject": env.get("subject", "")[:80],
        "date": env.get("date", ""),
    }

def analyze_platform(audits, platform_name):
    """Analyze all audits for a platform."""
    results = {
        "platform": platform_name,
        "total_messages": len(audits),
        "by_scope": defaultdict(int),
        "auth": {"spf": Counter(), "dkim": Counter(), "dmarc": Counter()},
        "hops": {"total": 0, "tls": 0, "non_tls": 0, "max": 0, "min": 999},
        "anomalies": [],
        "from_domains": Counter(),
    }
    for a in audits:
        scope = a.get("_scope", "unknown")
        results["by_scope"][scope] += 1
        
        auth = extract_auth(a)
        for k in ["spf", "dkim", "dmarc"]:
            results["auth"][k][auth[k]] += 1
        
        hops = extract_hops(a)
        results["hops"]["total"] += hops["total"]
        results["hops"]["tls"] += hops["tls"]
        results["hops"]["non_tls"] += hops["non_tls"]
        results["hops"]["max"] = max(results["hops"]["max"], hops["total"])
        results["hops"]["min"] = min(results["hops"]["min"], hops["total"]) if hops["total"] > 0 else results["hops"]["min"]
        
        env = extract_envelope(a)
        from_addr = env["from"]
        if "@" in from_addr:
            domain = from_addr.split("@")[-1].strip(">").strip()
            results["from_domains"][domain] += 1
        
        # Detect anomalies
        if auth["spf"] in ("fail", "softfail"):
            results["anomalies"].append({"type": "spf_failure", "severity": "high", "from": env["from"], "subject": env["subject"], "date": env["date"]})
        if auth["dkim"] == "fail":
            results["anomalies"].append({"type": "dkim_failure", "severity": "high", "from": env["from"], "subject": env["subject"], "date": env["date"]})
        if auth["dmarc"] == "fail":
            results["anomalies"].append({"type": "dmarc_failure", "severity": "high", "from": env["from"], "subject": env["subject"], "date": env["date"]})
        if hops["total"] > 8:
            results["anomalies"].append({"type": "excessive_hops", "severity": "medium", "hops": hops["total"], "from": env["from"], "subject": env["subject"]})
    
    if results["hops"]["min"] == 999:
        results["hops"]["min"] = 0
    
    return results

print("=" * 60)
print("CROSS-PLATFORM FORENSIC AUDIT ANALYSIS")
print(f"Generated: {datetime.utcnow().isoformat()}Z")
print("=" * 60)

# Load all audit files
print("\n[1] Loading Exchange audit files...")
exchange_audits = load_audit_files(os.path.join(BASE, "exchange-audit"))
print(f"    Loaded {len(exchange_audits)} Exchange audit files")

print("\n[2] Loading Gmail audit files...")
gmail_audits = load_audit_files(os.path.join(BASE, "gmail-audit"))
print(f"    Loaded {len(gmail_audits)} Gmail audit files")

# Analyze each platform
print("\n[3] Analyzing Exchange audits...")
ex_results = analyze_platform(exchange_audits, "Exchange Online")

print("\n[4] Analyzing Gmail audits...")
gm_results = analyze_platform(gmail_audits, "Google Workspace")

# Build unified report
report = {
    "generated": datetime.utcnow().isoformat() + "Z",
    "case_reference": "Case 2025-137857",
    "total_audited": len(exchange_audits) + len(gmail_audits),
    "platforms": {
        "exchange": {
            "total": ex_results["total_messages"],
            "by_scope": dict(ex_results["by_scope"]),
            "authentication": {k: dict(v) for k, v in ex_results["auth"].items()},
            "transport_hops": ex_results["hops"],
            "from_domains": dict(ex_results["from_domains"]),
            "anomalies": ex_results["anomalies"],
        },
        "gmail": {
            "total": gm_results["total_messages"],
            "by_scope": dict(gm_results["by_scope"]),
            "authentication": {k: dict(v) for k, v in gm_results["auth"].items()},
            "transport_hops": gm_results["hops"],
            "from_domains": dict(gm_results["from_domains"]),
            "anomalies": gm_results["anomalies"],
        },
    },
    "cross_platform_summary": {
        "total_anomalies": len(ex_results["anomalies"]) + len(gm_results["anomalies"]),
        "exchange_anomalies": len(ex_results["anomalies"]),
        "gmail_anomalies": len(gm_results["anomalies"]),
        "common_domains": list(set(ex_results["from_domains"].keys()) & set(gm_results["from_domains"].keys())),
        "exchange_only_domains": list(set(ex_results["from_domains"].keys()) - set(gm_results["from_domains"].keys())),
        "gmail_only_domains": list(set(gm_results["from_domains"].keys()) - set(ex_results["from_domains"].keys())),
    },
}

# Save report
out_file = os.path.join(BASE, "cross-platform", "cross_platform_analysis.json")
os.makedirs(os.path.dirname(out_file), exist_ok=True)
with open(out_file, "w") as f:
    json.dump(report, f, indent=2)
print(f"\n[5] Report saved: {out_file}")

# Print summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"\nTotal audited: {report['total_audited']} messages")
print(f"  Exchange: {ex_results['total_messages']} ({', '.join(f'{k}={v}' for k,v in ex_results['by_scope'].items())})")
print(f"  Gmail:    {gm_results['total_messages']} ({', '.join(f'{k}={v}' for k,v in gm_results['by_scope'].items())})")

print(f"\nAuthentication (Exchange):")
for k in ["spf", "dkim", "dmarc"]:
    print(f"  {k.upper()}: {dict(ex_results['auth'][k])}")

print(f"\nAuthentication (Gmail):")
for k in ["spf", "dkim", "dmarc"]:
    print(f"  {k.upper()}: {dict(gm_results['auth'][k])}")

print(f"\nTransport Hops:")
print(f"  Exchange: avg={ex_results['hops']['total']/max(ex_results['total_messages'],1):.1f}, max={ex_results['hops']['max']}, TLS={ex_results['hops']['tls']}/{ex_results['hops']['total']}")
print(f"  Gmail:    avg={gm_results['hops']['total']/max(gm_results['total_messages'],1):.1f}, max={gm_results['hops']['max']}, TLS={gm_results['hops']['tls']}/{gm_results['hops']['total']}")

print(f"\nAnomalies: {report['cross_platform_summary']['total_anomalies']} total")
for a in ex_results["anomalies"] + gm_results["anomalies"]:
    print(f"  [{a.get('severity','?').upper()}] {a['type']}: {a.get('from','')} — {a.get('subject','')}")

print(f"\nCross-platform domains:")
print(f"  Common: {report['cross_platform_summary']['common_domains']}")
print(f"  Exchange-only: {report['cross_platform_summary']['exchange_only_domains']}")
print(f"  Gmail-only: {report['cross_platform_summary']['gmail_only_domains']}")
