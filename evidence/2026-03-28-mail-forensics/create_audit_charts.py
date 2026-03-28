import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Forensic Audit Evidence Analysis — 96,472 Financial Documents', fontsize=14, fontweight='bold', y=0.98)

# 1. Purchase Order Collapse (top-left)
ax = axes[0, 0]
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
po_counts = [31, 50, 189, 378, 385, 93, 36, 70, 55, 7, 4]
colors = ['#2ecc71' if c > 100 else '#f39c12' if c > 30 else '#e74c3c' for c in po_counts]
bars = ax.bar(years, po_counts, color=colors, edgecolor='white', linewidth=0.5)
ax.set_title('Purchase Order Volume Collapse', fontweight='bold')
ax.set_xlabel('Year')
ax.set_ylabel('Number of POs')
ax.axhline(y=100, color='red', linestyle='--', alpha=0.5, label='Minimum expected')
# Annotate the fraud period
ax.axvspan(2025, 2026.5, alpha=0.1, color='red')
ax.text(2025.3, 350, 'FRAUD\nPERIOD', color='red', fontsize=9, fontweight='bold')
for bar, count in zip(bars, po_counts):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 5, str(count), ha='center', va='bottom', fontsize=8)

# 2. Credit Note Spike (top-right)
ax = axes[0, 1]
cn_years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
cn_counts = [1, 16, 9, 6, 80, 183, 718, 363, 91, 83]
colors2 = ['#e74c3c' if c > 500 else '#f39c12' if c > 100 else '#2ecc71' for c in cn_counts]
bars2 = ax.bar(cn_years, cn_counts, color=colors2, edgecolor='white', linewidth=0.5)
ax.set_title('Credit Note Volume (2022 Spike = 468 Courier Returns)', fontweight='bold')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Credit Notes')
ax.axhline(y=100, color='orange', linestyle='--', alpha=0.5)
for bar, count in zip(bars2, cn_counts):
    if count > 50:
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 10, str(count), ha='center', va='bottom', fontsize=8)

# 3. Invoice Sources (bottom-left)
ax = axes[1, 0]
sources = ['QuickBooks\n(60,362)', 'regima.zone\n(11,586)', 'Sage\n(5,372)', 'regimaskin\n(252)', 'Other\n(8,430)']
sizes = [60362, 11586, 5372, 252, 8430]
colors3 = ['#3498db', '#e67e22', '#2ecc71', '#e74c3c', '#95a5a6']
explode = (0, 0, 0, 0.15, 0)
wedges, texts, autotexts = ax.pie(sizes, labels=sources, colors=colors3, explode=explode, 
                                   autopct='%1.1f%%', startangle=90, textprops={'fontsize': 9})
autotexts[3].set_fontweight('bold')
autotexts[3].set_color('red')
ax.set_title('Invoice Sources (86,002 total)', fontweight='bold')

# 4. Bank Statement Coverage by Entity (bottom-right)
ax = axes[1, 1]
entities = ['SLG\n(62839612323)', 'SLG\n(62432501494)', 'RWW\n(62323196362)', 'Villa Via\n(62423540807)', 'RST\n(62839603835)']
stmts = [40, 15, 35, 18, 9]
missing = [0, 0, 20, 12, 0]
x = np.arange(len(entities))
width = 0.35
bars_have = ax.bar(x - width/2, stmts, width, label='Statements Found', color='#2ecc71', edgecolor='white')
bars_miss = ax.bar(x + width/2, missing, width, label='Months Missing', color='#e74c3c', edgecolor='white')
ax.set_title('FNB Statement Coverage by Entity', fontweight='bold')
ax.set_ylabel('Count')
ax.set_xticks(x)
ax.set_xticklabels(entities, fontsize=8)
ax.legend()
for bar, count in zip(bars_have, stmts):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5, str(count), ha='center', va='bottom', fontsize=8)
for bar, count in zip(bars_miss, missing):
    if count > 0:
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5, str(count), ha='center', va='bottom', fontsize=8, color='red', fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('/home/ubuntu/forensic_audit_charts.png', dpi=150, bbox_inches='tight')
print("Charts saved to /home/ubuntu/forensic_audit_charts.png")
