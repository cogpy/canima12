#!/usr/bin/env python3
"""
BOM Forensic Cost Flow Analysis — Strategic Logistics CC

Analyzes bank transaction data to reconstruct aggregate cost flows
through SLG's supply chain (raw materials, packaging, contract manufacturing)
and compares against trial balance figures to quantify the phantom stock
created by Bernadine's manufacturing BOM in Pastel.

Data source: fincosys/fund_flow/all_transactions_enriched.csv
"""

import csv
import json
import os
from collections import defaultdict
from datetime import datetime

# ── Vendor Classification ──────────────────────────────────────────
# Based on forensic analysis of SLG payment recipients

VENDOR_CATEGORIES = {
    'manufacturer': {
        'keywords': ['prime regima', 'prime product', 'proficos'],
        'description': 'Contract manufacturers who convert raws + packaging into finished goods',
        'entities': {
            'Prime Product Manufacturing (Prime Regima)': ['prime regima', 'prime product manufa'],
            'Proficos': ['proficos'],
        }
    },
    'packaging': {
        'keywords': [
            'young pioneer', 'floraison', 'regima jars', 'masterpack',
            'consupaq', 'labelpak', 'crystal pack', 'drieline',
            'regima containers', 'mosaic', 'container'
        ],
        'description': 'Packaging suppliers (jars, bottles, tubes, labels, boxes)',
        'entities': {
            'Young Pioneer Containers': ['young pioneer'],
            'Containers Floraison': ['floraison'],
            'Regima Jars': ['regima jars'],
            'Masterpack': ['masterpack'],
            'Consupaq': ['consupaq'],
            'Labelpak': ['labelpak'],
            'Crystal Pack': ['crystal pack'],
            'Drieline': ['drieline'],
            'Regima Containers': ['regima containers'],
            'Mosaic': ['mosaic'],
        }
    },
    'raw_materials': {
        'keywords': [
            'cjp chem', 'natchem', 'carst', 'alistin', 'meganede',
            'chempure', 'croda', 'merck', 'savannah', 'hexachem',
            'materia medica', 'botanichem'
        ],
        'description': 'Raw material / active ingredient suppliers (pre-purchased, sent to packer)',
        'entities': {
            'CJP Chemicals (Seppic actives)': ['cjp chem'],
            'Natchem (Botanical extracts)': ['natchem'],
            'Carst & Walker (Mibelle peptides)': ['carst'],
            'Alistin (Peptide ingredient)': ['alistin'],
            'Meganede (Specialty ingredients)': ['meganede'],
            'Chempure (Chemicals)': ['chempure'],
            'Croda (Matrixyl peptides)': ['croda'],
            'Merck (Chemicals)': ['merck'],
            'Savannah Fine Chem': ['savannah'],
            'Hexachem': ['hexachem'],
            'Materia Medica': ['materia medica'],
        }
    },
    'logistics': {
        'keywords': ['jubilingo', 'courier logix', 'karen vdho'],
        'description': 'Logistics coordinators and couriers',
        'entities': {
            'Jubilingo (Karen van der Hoven)': ['jubilingo', 'karen vdho'],
            'Courier Logix': ['courier logix'],
        }
    },
}

# SLG and RST bank account numbers
SLG_ACCOUNT = '62432501494'
RST_ACCOUNT = '55270035642'

# Trial balance reference data (from forensic extraction)
TB_REFERENCE = {
    'FY2020': {
        'period': 'Mar 2019 – Feb 2020',
        'finished_goods_7700': 934840.08,  # Raw TB
        'finished_goods_7700_adjusted': 693510.89,  # After Bantjies' AJEs
        'raw_mat_primary_7540': 1516479.49,
        'raw_mat_empty_cont_7650': 4274946.92,
        'raw_mat_boxes_7750': 8231078.00,
        'cost_of_sales_2000': 13993637.14,
        'inventory_adjustment_2100_dr': 48423.24,
        'inventory_adjustment_2100_cr': 164089.40,
        'source': 'SL - TRIAL BALANCE 2020.xlsx (forensic_trial_balances.json)',
    },
    'FY2024': {
        'period': 'Mar 2023 – Feb 2024',
        'finished_goods_tb': 1443217.78,  # On trial balance (PHANTOM)
        'finished_goods_valuation': 0.00,  # On stock valuation (CORRECT)
        'finished_goods_credit': 2756321.85,  # Negative/credit balance
        'total_discrepancy': 4199539.63,  # R4.2M
        'source': 'Rynette email 4 Apr 2025 to Bantjies',
    },
}


def categorize_vendor(target_account):
    """Classify a payment target into a supply chain category."""
    target_lower = target_account.lower()
    for category, config in VENDOR_CATEGORIES.items():
        if any(kw in target_lower for kw in config['keywords']):
            # Find specific entity
            entity_name = category  # default
            for name, entity_keywords in config['entities'].items():
                if any(ek in target_lower for ek in entity_keywords):
                    entity_name = name
                    break
            return category, entity_name
    return 'other', target_account


def load_transactions(csv_path, account_filter=None):
    """Load and filter bank transactions from enriched CSV."""
    transactions = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if account_filter and row.get('account_number') != account_filter:
                continue
            transactions.append(row)
    return transactions


def analyze_cost_flows(transactions, direction='payment_out'):
    """Analyze cost flows by category and year."""
    yearly = defaultdict(lambda: defaultdict(float))
    yearly_count = defaultdict(lambda: defaultdict(int))
    vendor_totals = defaultdict(lambda: {'total': 0, 'count': 0, 'first': '9999', 'last': '0000'})
    category_vendors = defaultdict(lambda: defaultdict(float))

    for txn in transactions:
        if txn.get('transaction_type') != direction:
            continue

        target = txn.get('target_account', '')
        amount = float(txn.get('amount', 0))
        timestamp = txn.get('timestamp', '')
        year = timestamp[:4] if timestamp else 'unknown'

        # For FY alignment (Mar-Feb), compute fiscal year
        if timestamp:
            try:
                dt = datetime.strptime(timestamp[:10], '%Y-%m-%d')
                fy_year = dt.year if dt.month >= 3 else dt.year - 1
                fy = f"FY{fy_year + 1}"  # FY ending Feb of next year
            except ValueError:
                fy = f"CY{year}"
        else:
            fy = 'unknown'

        category, entity = categorize_vendor(target)

        yearly[fy][category] += amount
        yearly_count[fy][category] += 1
        vendor_totals[entity]['total'] += amount
        vendor_totals[entity]['count'] += 1
        vendor_totals[entity]['first'] = min(vendor_totals[entity]['first'], timestamp[:10] if timestamp else '9999')
        vendor_totals[entity]['last'] = max(vendor_totals[entity]['last'], timestamp[:10] if timestamp else '0000')
        category_vendors[category][entity] += amount

    return yearly, yearly_count, vendor_totals, category_vendors


def compute_discrepancy_analysis(yearly, tb_ref):
    """Compare actual cost flows to trial balance figures."""
    analysis = {}

    for fy, categories in sorted(yearly.items()):
        total_input = sum(categories.values())
        mfr = categories.get('manufacturer', 0)
        pkg = categories.get('packaging', 0)
        raw = categories.get('raw_materials', 0)
        logistics = categories.get('logistics', 0)
        other = categories.get('other', 0)

        # The actual cost of goods received should be approximately:
        # manufacturing fee + raw materials + packaging
        # (since the manufacturer charges for their service which includes
        # base materials + labour, and SLG separately pays for pre-purchased
        # raws and packaging)
        estimated_cogs = mfr + raw + pkg

        analysis[fy] = {
            'manufacturer': round(mfr, 2),
            'packaging': round(pkg, 2),
            'raw_materials': round(raw, 2),
            'logistics': round(logistics, 2),
            'other': round(other, 2),
            'total_input': round(total_input, 2),
            'estimated_cogs': round(estimated_cogs, 2),
        }

    # Add TB reference data where available
    if 'FY2020' in analysis:
        analysis['FY2020']['tb_finished_goods'] = tb_ref['FY2020']['finished_goods_7700']
        analysis['FY2020']['tb_cost_of_sales'] = tb_ref['FY2020']['cost_of_sales_2000']
        analysis['FY2020']['note'] = 'TB shows R935K finished goods; BOM already active'

    if 'FY2024' in analysis or 'FY2025' in analysis:
        fy_key = 'FY2024' if 'FY2024' in analysis else 'FY2025'
        analysis[fy_key]['tb_phantom_stock'] = tb_ref['FY2024']['finished_goods_tb']
        analysis[fy_key]['tb_negative_stock'] = tb_ref['FY2024']['finished_goods_credit']
        analysis[fy_key]['total_discrepancy'] = tb_ref['FY2024']['total_discrepancy']
        analysis[fy_key]['note'] = 'R4.2M discrepancy: R1.44M phantom + R2.76M negative'

    return analysis


def generate_report(analysis, vendor_totals, category_vendors):
    """Generate formatted text report."""
    lines = []
    lines.append("=" * 80)
    lines.append("BOM FORENSIC COST FLOW ANALYSIS — STRATEGIC LOGISTICS CC")
    lines.append("=" * 80)
    lines.append("")

    # Yearly summary
    lines.append("YEARLY COST FLOWS BY CATEGORY (Fiscal Years ending February)")
    lines.append("-" * 80)
    header = f"{'FY':<8} {'Manufacturer':>14} {'Packaging':>14} {'Raw Materials':>14} {'Other':>14} {'TOTAL':>14}"
    lines.append(header)
    lines.append("-" * 80)

    grand_total = defaultdict(float)
    for fy in sorted(analysis.keys()):
        if fy.startswith('FY'):
            data = analysis[fy]
            lines.append(
                f"{fy:<8} "
                f"R{data['manufacturer']:>12,.0f} "
                f"R{data['packaging']:>12,.0f} "
                f"R{data['raw_materials']:>12,.0f} "
                f"R{data['other']:>12,.0f} "
                f"R{data['total_input']:>12,.0f}"
            )
            for cat in ['manufacturer', 'packaging', 'raw_materials', 'other', 'total_input']:
                grand_total[cat] += data[cat]

    lines.append("-" * 80)
    lines.append(
        f"{'TOTAL':<8} "
        f"R{grand_total['manufacturer']:>12,.0f} "
        f"R{grand_total['packaging']:>12,.0f} "
        f"R{grand_total['raw_materials']:>12,.0f} "
        f"R{grand_total['other']:>12,.0f} "
        f"R{grand_total['total_input']:>12,.0f}"
    )

    # TB comparison
    lines.append("")
    lines.append("TRIAL BALANCE COMPARISON")
    lines.append("-" * 80)
    if 'FY2020' in analysis and 'tb_finished_goods' in analysis['FY2020']:
        lines.append(f"FY2020 TB Finished Goods (7700/000): R{analysis['FY2020']['tb_finished_goods']:,.2f}")
        lines.append(f"FY2020 TB Cost of Sales (2000/000):  R{analysis['FY2020']['tb_cost_of_sales']:,.2f}")
        lines.append(f"FY2020 Bank Mfr Payments:            R{analysis['FY2020']['manufacturer']:,.2f}")
        lines.append(f"  NOTE: {analysis['FY2020'].get('note', '')}")

    for fy in ['FY2024', 'FY2025']:
        if fy in analysis and 'total_discrepancy' in analysis[fy]:
            lines.append(f"\n{fy} DISCREPANCY (from Rynette's April 2025 email):")
            lines.append(f"  Phantom Finished Goods on TB:  R{analysis[fy]['tb_phantom_stock']:,.2f}")
            lines.append(f"  Negative Finished Goods:       R{analysis[fy]['tb_negative_stock']:,.2f}")
            lines.append(f"  TOTAL DISCREPANCY:             R{analysis[fy]['total_discrepancy']:,.2f}")
            lines.append(f"  NOTE: {analysis[fy].get('note', '')}")

    # Top vendors
    lines.append("")
    lines.append("TOP VENDORS BY TOTAL PAYMENT")
    lines.append("-" * 80)
    sorted_vendors = sorted(vendor_totals.items(), key=lambda x: x[1]['total'], reverse=True)
    for vendor, data in sorted_vendors[:20]:
        lines.append(
            f"  R{data['total']:>12,.2f} ({data['count']:>3} txns) "
            f"| {data['first']} to {data['last']} "
            f"| {vendor}"
        )

    # Category breakdowns
    for cat_name, cat_config in VENDOR_CATEGORIES.items():
        if cat_name in category_vendors:
            lines.append(f"\n{cat_name.upper()} VENDORS — {cat_config['description']}")
            lines.append("-" * 60)
            for vendor, total in sorted(category_vendors[cat_name].items(), key=lambda x: x[1], reverse=True):
                lines.append(f"  R{total:>12,.2f} | {vendor}")

    return "\n".join(lines)


def main():
    """Main analysis pipeline."""
    csv_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        '..', 'fincosys', 'fund_flow', 'all_transactions_enriched.csv'
    )

    if not os.path.exists(csv_path):
        # Try alternative path
        csv_path = '/home/user/fincosys/fund_flow/all_transactions_enriched.csv'

    if not os.path.exists(csv_path):
        print(f"ERROR: Transaction data not found at {csv_path}")
        return

    print(f"Loading transactions from {csv_path}...")

    # ── SLG Analysis ──
    print("\n[1/3] Analyzing SLG (Strategic Logistics CC) outgoing payments...")
    slg_txns = load_transactions(csv_path, account_filter=SLG_ACCOUNT)
    slg_yearly, slg_counts, slg_vendors, slg_cat_vendors = analyze_cost_flows(slg_txns)

    # ── RST Analysis (for manufacturer cross-reference) ──
    print("[2/3] Analyzing RST (RegimA Skin Treatments) manufacturer payments...")
    rst_txns = load_transactions(csv_path, account_filter=RST_ACCOUNT)
    rst_yearly, rst_counts, rst_vendors, rst_cat_vendors = analyze_cost_flows(rst_txns)

    # ── Discrepancy Analysis ──
    print("[3/3] Computing discrepancy analysis against trial balance data...")
    discrepancy = compute_discrepancy_analysis(slg_yearly, TB_REFERENCE)

    # ── Generate Report ──
    report = generate_report(discrepancy, slg_vendors, slg_cat_vendors)
    print("\n" + report)

    # ── Export JSON ──
    output = {
        'generated': datetime.now().isoformat(),
        'description': 'BOM Forensic Cost Flow Analysis — Strategic Logistics CC',
        'slg_account': SLG_ACCOUNT,
        'rst_account': RST_ACCOUNT,
        'fiscal_year_cost_flows': discrepancy,
        'top_vendors': {
            name: {
                'total': round(data['total'], 2),
                'count': data['count'],
                'first_transaction': data['first'],
                'last_transaction': data['last'],
            }
            for name, data in sorted(slg_vendors.items(), key=lambda x: x[1]['total'], reverse=True)[:30]
        },
        'category_totals': {
            cat: round(sum(vendors.values()), 2)
            for cat, vendors in slg_cat_vendors.items()
        },
        'rst_manufacturer_payments': {
            name: round(total, 2)
            for name, total in sorted(rst_cat_vendors.get('manufacturer', {}).items(), key=lambda x: x[1], reverse=True)
        },
        'trial_balance_reference': TB_REFERENCE,
        'methodology': {
            'data_source': 'FNB bank statements via fincosys/fund_flow/all_transactions_enriched.csv',
            'classification': 'Vendors classified by name matching against known supplier categories',
            'fiscal_year': 'March to February (aligned with SLG financial year)',
            'limitations': [
                'Bank payments show gross amounts, not unit prices or quantities',
                'Some vendors may be misclassified in "other" category',
                'No item-level Pastel stock transaction data available',
                'Manufacturing invoices from Prime/Proficos not individually available',
            ],
        },
    }

    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'evidence')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'bom_cost_flow_data.json')

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nJSON output saved to: {output_path}")
    print("Done.")


if __name__ == '__main__':
    main()
