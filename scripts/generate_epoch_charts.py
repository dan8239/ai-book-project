"""
Generate the epoch training charts for the Coffee Guy scene.

Two charts:
1. Median Extinction Time by Epoch — the slow grind, barely moving
2. Best Trial Survival by Epoch (log scale) — the sudden breakthrough

Run: python scripts/generate_epoch_charts.py
"""

import numpy as np
import plotly.graph_objects as go
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chart_style import apply_style, save_figure, COLORS

np.random.seed(42)

# --- Data Generation ---

epochs = np.arange(0, 4418)

# Median extinction: flat around 155-160 for thousands of epochs,
# then a slow inflection starting around epoch 3800
base = 155 + np.random.normal(0, 2.5, len(epochs))
# Add a gentle sigmoid inflection starting at epoch ~3800
inflection = 40 / (1 + np.exp(-0.012 * (epochs - 4000)))
median_extinction = base + inflection

# Pin endpoints BEFORE smoothing so they blend naturally
median_extinction[-1] = 192
# Blend the last 20 points into 192 to avoid a spike
for i in range(20):
    idx = -(20 - i)
    weight = i / 20.0
    median_extinction[idx] = median_extinction[idx] * (1 - weight) + 192 * weight

from scipy.ndimage import uniform_filter1d
median_extinction = uniform_filter1d(median_extinction, size=50)

# Best trial: flat and noisy in the low hundreds for almost all epochs,
# then a sudden vertical breakthrough at the very end
best_trial_log = np.log10(120) + np.random.normal(0, 0.12, len(epochs))
best_trial_log = uniform_filter1d(best_trial_log, size=30)
best_trial = 10 ** best_trial_log

# Last 3 epochs: sudden breakthrough (no gradual climb)
best_trial[-3] = 1842
best_trial[-2] = 1842
best_trial[-1] = 22000

# --- Font sizes scaled up for Obsidian embed readability ---

TITLE_SIZE = 22
AXIS_LABEL_SIZE = 17
TICK_SIZE = 15
ANNOTATION_SIZE = 14
MARKER_TEXT_SIZE = 16
LEGEND_SIZE = 14

# --- Chart 1: Median Extinction Time ---

fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=epochs,
    y=median_extinction,
    mode="lines",
    line=dict(color=COLORS["accent"], width=2),
    name="Median extinction time",
))

# Current epoch marker
fig1.add_trace(go.Scatter(
    x=[4417],
    y=[median_extinction[-1]],
    mode="markers+text",
    marker=dict(color=COLORS["gold"], size=12, symbol="diamond"),
    text=["192 yr"],
    textposition="top left",
    textfont=dict(color=COLORS["gold"], size=MARKER_TEXT_SIZE),
    name="Current (4,417)",
    showlegend=False,
))

# Annotation for the flat period
fig1.add_annotation(
    x=2000, y=155,
    text="~158 yr avg for 3,800 epochs",
    showarrow=False,
    font=dict(size=ANNOTATION_SIZE, color=COLORS["text"]),
    yshift=18,
)

apply_style(fig1, title="Median Extinction Time by Epoch")
fig1.update_layout(
    title=dict(font=dict(size=TITLE_SIZE)),
    legend=dict(font=dict(size=LEGEND_SIZE)),
)
fig1.update_xaxes(
    title_text="Epoch",
    title_font=dict(size=AXIS_LABEL_SIZE),
    tickfont=dict(size=TICK_SIZE),
    dtick=500,
)
fig1.update_yaxes(
    title_text="Years",
    title_font=dict(size=AXIS_LABEL_SIZE),
    tickfont=dict(size=TICK_SIZE),
    range=[100, 220],
)

save_figure(fig1, "median_extinction_by_epoch")

# --- Chart 2: Best Trial Survival (Log Scale) ---

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=epochs,
    y=best_trial,
    mode="lines",
    line=dict(color=COLORS["accent"], width=2),
    name="Best trial survival",
))

# Current epoch marker
fig2.add_trace(go.Scatter(
    x=[4417],
    y=[22000],
    mode="markers+text",
    marker=dict(color=COLORS["gold"], size=12, symbol="diamond"),
    text=[">20,000 yr"],
    textposition="middle left",
    textfont=dict(color=COLORS["gold"], size=MARKER_TEXT_SIZE),
    name="Current (4,417)",
    showlegend=False,
))

# Projection window line
fig2.add_hline(
    y=20000,
    line_dash="dot",
    line_color=COLORS["green"],
    line_width=1,
    annotation_text="Projection window (20,000 yr)",
    annotation_position="bottom right",
    annotation_font=dict(size=ANNOTATION_SIZE, color=COLORS["green"]),
)

# Previous best annotation
fig2.add_trace(go.Scatter(
    x=[4416],
    y=[1842],
    mode="markers+text",
    marker=dict(color=COLORS["text"], size=8, symbol="circle"),
    text=["1,842 yr"],
    textposition="top left",
    textfont=dict(color=COLORS["text"], size=ANNOTATION_SIZE),
    showlegend=False,
))

apply_style(fig2, title="Best Trial Survival by Epoch")
fig2.update_layout(
    title=dict(font=dict(size=TITLE_SIZE)),
    legend=dict(font=dict(size=LEGEND_SIZE)),
)
fig2.update_xaxes(
    title_text="Epoch",
    title_font=dict(size=AXIS_LABEL_SIZE),
    tickfont=dict(size=TICK_SIZE),
    dtick=500,
)
fig2.update_yaxes(
    title_text="Years (log scale)",
    title_font=dict(size=AXIS_LABEL_SIZE),
    tickfont=dict(size=TICK_SIZE),
    type="log",
    dtick=1,
)

save_figure(fig2, "best_trial_by_epoch")

print("\nDone. Embed in markdown with:")
print('![Median Extinction by Epoch](../../assets/figures/median_extinction_by_epoch.png)')
print('![Best Trial by Epoch](../../assets/figures/best_trial_by_epoch.png)')
