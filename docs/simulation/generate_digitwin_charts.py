#!/usr/bin/env python3
"""Generate visualization charts for DigiTwin simulation results."""

import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Load results
with open('/home/ubuntu/revstream1/docs/simulation/DIGITWIN_RESULTS_2026_03_11.json') as f:
    results = json.load(f)

# Dark theme
plt.style.use('dark_background')
COLORS = {
    'red': '#f85149', 'green': '#3fb950', 'yellow': '#d29922',
    'blue': '#58a6ff', 'purple': '#bc8cff', 'orange': '#db6d28',
    'cyan': '#39d2e0', 'pink': '#f778ba',
}

# ============================================================================
# Chart 1: Agent Cognitive Mode Timeline
# ============================================================================
fig, axes = plt.subplots(3, 2, figsize=(18, 12))
fig.suptitle('DigiTwin: Agent Cognitive Mode Analysis\nCase 2025-137857 — Revenue Stream Hijacking',
             fontsize=16, fontweight='bold', color='white')

agent_states = results['agent_final_states']
mode_colors = {
    'RESTING': '#555555', 'EXPLORATORY': COLORS['cyan'], 'FOCUSED': COLORS['blue'],
    'STRESSED': COLORS['red'], 'SOCIAL': COLORS['pink'], 'REFLECTIVE': COLORS['purple'],
    'VIGILANT': COLORS['orange'], 'MAINTENANCE': '#888888', 'REWARD': COLORS['green'],
    'THREAT': '#ff0000',
}

for idx, state in enumerate(agent_states):
    ax = axes[idx // 2][idx % 2]
    # Hormone levels bar chart
    hormones = ['Cortisol', 'Dopamine', 'NorEpi', 'Oxytocin']
    values = [state['cortisol'], state['dopamine_total'], state['norepinephrine'], state['oxytocin']]
    colors = [COLORS['red'], COLORS['green'], COLORS['orange'], COLORS['pink']]
    bars = ax.barh(hormones, values, color=colors, height=0.6)
    ax.set_xlim(0, 1.0)
    ax.set_title(f"{state['name']}\nMode: {state['final_mode']} | Valence: {state['valence']:.2f}",
                fontsize=10, fontweight='bold',
                color=COLORS['red'] if state['agent_type'] == 'antagonist' else COLORS['green'])
    ax.set_xlabel('Hormone Level')
    for bar, val in zip(bars, values):
        ax.text(val + 0.02, bar.get_y() + bar.get_height()/2, f'{val:.2f}',
               va='center', fontsize=9, color='white')

plt.tight_layout()
plt.savefig('/home/ubuntu/revstream1/docs/simulation/digitwin_agent_modes.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# Chart 2: Stock-Flow Financial Model
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle('DigiTwin: Stock-Flow Financial Model\nCase 2025-137857 — R38.4M Total Financial Impact',
             fontsize=16, fontweight='bold', color='white')

sf = results['stock_flow_final']

# Revenue vs Diverted
ax = axes[0][0]
labels = ['Legitimate\nRevenue', 'Diverted\nRevenue', 'Hidden\nAccounts']
values = [sf['regima_revenue']['final_value'], sf['diverted_revenue']['final_value'],
          sf['hidden_accounts']['final_value']]
colors = [COLORS['green'], COLORS['red'], COLORS['orange']]
bars = ax.bar(labels, [v/1e6 for v in values], color=colors, width=0.6)
ax.set_ylabel('ZAR (Millions)')
ax.set_title('Revenue Distribution', fontweight='bold')
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
           f'R{val/1e6:.1f}M', ha='center', fontsize=10, fontweight='bold', color='white')

# Ketoni Convergence
ax = axes[0][1]
ketoni_labels = ['Ketoni\nReceivable', 'FFT\nAssets', 'Shareholder\nLoan']
ketoni_values = [sf['ketoni_receivable']['final_value'], sf['fft_assets']['final_value'],
                 sf['shareholder_loan']['final_value']]
bars = ax.bar(ketoni_labels, [v/1e6 for v in ketoni_values],
             color=[COLORS['yellow'], COLORS['purple'], COLORS['red']], width=0.6)
ax.set_ylabel('ZAR (Millions)')
ax.set_title('Ketoni R18.685M Convergence', fontweight='bold')
for bar, val in zip(bars, ketoni_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
           f'R{val/1e6:.1f}M', ha='center', fontsize=10, fontweight='bold', color='white')

# DES Transaction Flow
ax = axes[1][0]
des = results['des_results']
sizes = [des['legitimate_transactions'], des['diverted_transactions']]
labels_pie = [f"Legitimate\n{des['legitimate_transactions']}", f"Diverted\n{des['diverted_transactions']}"]
wedges, texts, autotexts = ax.pie(sizes, labels=labels_pie,
                                   colors=[COLORS['green'], COLORS['red']],
                                   autopct='%1.1f%%', startangle=90,
                                   textprops={'color': 'white', 'fontsize': 10})
ax.set_title('Transaction Flow (DES Model)', fontweight='bold')

# What-If Scenarios
ax = axes[1][1]
scenarios = results['what_if_scenarios']
scenario_names = [s['name'] for s in scenarios]
savings = [s.get('estimated_savings', s.get('total_diverted', 0)) for s in scenarios]
colors_s = [COLORS['green'], COLORS['blue'], COLORS['red']]
bars = ax.barh(scenario_names, [v/1e6 for v in savings], color=colors_s, height=0.5)
ax.set_xlabel('ZAR (Millions)')
ax.set_title('What-If Scenario Impact', fontweight='bold')
for bar, val in zip(bars, savings):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
           f'R{val/1e6:.1f}M', va='center', fontsize=10, fontweight='bold', color='white')

plt.tight_layout()
plt.savefig('/home/ubuntu/revstream1/docs/simulation/digitwin_stock_flow.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# Chart 3: Burden of Proof Assessment
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 8))
fig.suptitle('DigiTwin: Simulation-Enhanced Burden of Proof Assessment\nCase 2025-137857',
             fontsize=16, fontweight='bold', color='white')

bop = results['burden_of_proof']
charges = bop['charges']
charge_names = [c['charge'] for c in charges]
probabilities = [c['probability'] for c in charges]

y_pos = np.arange(len(charge_names))
bars = ax.barh(y_pos, probabilities, color=[COLORS['green'] if p >= 0.95 else COLORS['yellow']
                                             for p in probabilities], height=0.6)

# Threshold lines
ax.axvline(x=0.50, color=COLORS['yellow'], linestyle='--', linewidth=1.5, alpha=0.7, label='Civil (50%)')
ax.axvline(x=0.95, color=COLORS['red'], linestyle='--', linewidth=1.5, alpha=0.7, label='Criminal (95%)')

ax.set_yticks(y_pos)
ax.set_yticklabels(charge_names, fontsize=11)
ax.set_xlabel('Probability', fontsize=12)
ax.set_xlim(0, 1.05)
ax.legend(loc='lower right', fontsize=10)

for bar, prob in zip(bars, probabilities):
    ax.text(prob + 0.01, bar.get_y() + bar.get_height()/2,
           f'{prob:.0%}', va='center', fontsize=11, fontweight='bold',
           color=COLORS['green'] if prob >= 0.95 else COLORS['yellow'])

plt.tight_layout()
plt.savefig('/home/ubuntu/revstream1/docs/simulation/digitwin_burden_of_proof.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# Chart 4: Phase Analysis - Agent Mode Distribution
# ============================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('DigiTwin: Phase-by-Phase Agent Cognitive Mode Distribution\nCase 2025-137857',
             fontsize=16, fontweight='bold', color='white')

phases = results['phase_analysis']
for idx, phase in enumerate(phases):
    ax = axes[idx // 3][idx % 3]
    agent_names = []
    mode_data = {}

    for agent_name, mode_info in phase.get('agent_modes', {}).items():
        short_name = agent_name.split()[-1] if len(agent_name.split()) > 1 else agent_name
        agent_names.append(short_name)
        for mode, count in mode_info.get('mode_distribution', {}).items():
            if mode not in mode_data:
                mode_data[mode] = []
            while len(mode_data[mode]) < len(agent_names) - 1:
                mode_data[mode].append(0)
            mode_data[mode].append(count)

    # Pad
    for mode in mode_data:
        while len(mode_data[mode]) < len(agent_names):
            mode_data[mode].append(0)

    if agent_names:
        x = np.arange(len(agent_names))
        width = 0.8 / max(len(mode_data), 1)
        for i, (mode, counts) in enumerate(mode_data.items()):
            color = mode_colors.get(mode, '#888888')
            ax.bar(x + i * width - 0.4 + width/2, counts, width, label=mode, color=color)
        ax.set_xticks(x)
        ax.set_xticklabels(agent_names, rotation=45, ha='right', fontsize=8)

    ax.set_title(f"Phase: {phase['phase']}\n{phase['period']}",
                fontsize=10, fontweight='bold')
    ax.set_ylabel('Count')

# Add legend to last subplot
handles = [mpatches.Patch(color=color, label=mode) for mode, color in mode_colors.items()
           if mode in ['STRESSED', 'REWARD', 'FOCUSED', 'THREAT', 'SOCIAL', 'EXPLORATORY', 'VIGILANT']]
axes[1][2].legend(handles=handles, loc='center', fontsize=9, ncol=2)

plt.tight_layout()
plt.savefig('/home/ubuntu/revstream1/docs/simulation/digitwin_phase_analysis.png', dpi=150, bbox_inches='tight')
plt.close()

print("All charts generated successfully!")
print("  - digitwin_agent_modes.png")
print("  - digitwin_stock_flow.png")
print("  - digitwin_burden_of_proof.png")
print("  - digitwin_phase_analysis.png")
