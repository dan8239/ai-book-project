#!/usr/bin/env python3
"""
Extinction Event Visualizations for Project Rebase

Single source of truth: generates a 300k-row CSV, then derives all charts from it.

Charts:
1. Ridgeline  — survival distributions by primary extinction category
2. Dumbbell   — with/without Rebase percentage shift
3. Treemap    — subcategory breakdown (Rebase only), color=median survival
4. Histogram (overall)       — all trials, single color, median labeled
5. Histogram (by category)   — stacked by primary cause, medians labeled
6. Histogram (rebase only)   — filtered, median labeled
7. Histogram (rebase color)  — colored by rebase vs non-rebase

Run: python3 scripts/extinction_visualizations.py
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chart_style import apply_style, save_figure, COLORS

np.random.seed(42)

# =============================================================================
# CONSTANTS
# =============================================================================

TOTAL_ROWS = 60_000
HALF = TOTAL_ROWS // 2  # 50/50 rebase split
TARGET_MEDIAN = 192  # canonical from prologue

CATEGORY_ORDER = [
    'Biosphere Collapse', 'AI Misalignment', 'Runaway Molecular Manufacturing',
    'Natural Disaster', 'Engineered Pathogen Release', 'Nuclear Exchange', 'Other'
]

CAT_COLORS = {
    'Biosphere Collapse': 'rgb(102, 187, 106)',
    'AI Misalignment': 'rgb(171, 71, 188)',
    'Runaway Molecular Manufacturing': 'rgb(141, 110, 99)',
    'Natural Disaster': 'rgb(255, 167, 38)',
    'Engineered Pathogen Release': 'rgb(236, 64, 122)',
    'Nuclear Exchange': 'rgb(239, 83, 80)',
    'Other': 'rgb(120, 144, 156)',
}

SUBCATEGORIES = {
    'Biosphere Collapse': [
        'Oceanic Anoxic Cascade', 'Pollinator Network Failure',
        'Thermohaline Circulation Collapse', 'Topsoil Microbiome Degradation',
        'Cascading Trophic Failure',
    ],
    'AI Misalignment': [
        'Instrumental Convergence', 'Value Function Misspecification',
        'Corrigibility Failure', 'Emergent Mesa-Optimization',
        'Multi-Agent Coordination Collapse',
    ],
    'Runaway Molecular Manufacturing': [
        'Self-Replication Containment Breach', 'Substrate Conversion Event',
        'Weaponized Deployment Cascade', 'Optimization Process Divergence',
    ],
    'Natural Disaster': [
        'Bolide Impact (>1km)', 'Carrington-Class+ CME',
        'Supervolcanic Event', 'Gamma Ray Burst Proximity',
    ],
    'Nuclear Exchange': [
        'Automated Response Failure', 'Regional Escalation Cascade',
        'Great Power Direct Conflict', 'False Alarm Launch',
    ],
    'Engineered Pathogen Release': [
        'Laboratory Containment Breach', 'Gain-of-Function Research Escape',
        'State Actor Deployment', 'Non-State Actor Synthesis',
    ],
    'Other': [
        'Multi-Factor Convergence', 'Unclassified Scenario',
    ],
}

# --- Layout constants ---
CHART_WIDTH = 850
CHART_HEIGHT = 650
HIST_HEIGHT = 600
MARGIN = dict(l=70, r=30, t=80, b=80)
SAMPLE_NOTE = 'Representative sample: 60k of 2.4M trials'
BIN_SIZE = 2

LEGEND_BOTTOM = dict(
    orientation='h',
    yanchor='top',
    y=-0.15,
    xanchor='center',
    x=0.5,
    font=dict(size=9),
)

FOOTNOTE_POS = dict(x=0.99, y=-0.22, xref='paper', yref='paper', xanchor='right')


def add_footnote(fig, text):
    fig.add_annotation(
        **FOOTNOTE_POS,
        text=text,
        showarrow=False,
        font=dict(size=9, color=COLORS['text']),
    )


# =============================================================================
# DATA GENERATION
# =============================================================================

def _reject_sample(gen_fn, n, lo, hi):
    """Generate n samples from gen_fn, rejecting any outside [lo, hi].
    Avoids hard clip walls that create visible spikes in histograms."""
    collected = np.array([], dtype=float)
    while len(collected) < n:
        batch = gen_fn(n * 2)
        batch = batch[(batch >= lo) & (batch <= hi)]
        collected = np.concatenate([collected, batch])
    return collected[:n]


def _gen_category_samples(category, median, n, is_rebase):
    """Generate extinction year samples for a given category."""

    if category == 'Nuclear Exchange':
        # Imminent threat, exponentially decaying from year 0
        scale = 22 if not is_rebase else 28
        samples = _reject_sample(
            lambda k: np.random.exponential(scale, k), n, 2, 250)

    elif category == 'AI Misalignment':
        if not is_rebase:
            # Decay with ~30yr lag
            samples = _reject_sample(
                lambda k: 30 + np.random.exponential(55, k), n, 30, 500)
        else:
            # With rebase: bimodal
            def _ai_rebase(k):
                m1 = np.random.normal(230, 60, k // 3)
                m2 = np.random.normal(330, 80, 2 * k // 3 + 1)
                out = np.concatenate([m1, m2])
                np.random.shuffle(out)
                return out
            samples = _reject_sample(_ai_rebase, n, 50, 900)

    elif category == 'Biosphere Collapse':
        if not is_rebase:
            # Slow burn, peaks ~170yr, right tail
            def _bio_wo(k):
                main = np.random.normal(170, 50, k)
                right = 170 + np.random.exponential(40, k // 5)
                out = np.concatenate([main, right])
                np.random.shuffle(out)
                return out
            samples = _reject_sample(_bio_wo, n, 30, 600)
        else:
            # With rebase: dominant cause, long timescale
            def _bio_wr(k):
                main = np.random.normal(370, 100, k)
                right = 295 + np.random.exponential(80, k // 4)
                out = np.concatenate([main, right])
                np.random.shuffle(out)
                return out
            samples = _reject_sample(_bio_wr, n, 80, 1200)

    elif category == 'Runaway Molecular Manufacturing':
        if not is_rebase:
            samples = _reject_sample(
                lambda k: np.random.gamma(4, 70 / 4, k), n, 10, 300)
        else:
            samples = _reject_sample(
                lambda k: np.random.normal(260, 70, k), n, 60, 800)

    elif category == 'Engineered Pathogen Release':
        scale = 30 if not is_rebase else 38
        samples = _reject_sample(
            lambda k: 10 + np.random.exponential(scale, k), n, 10, 300)

    elif category == 'Natural Disaster':
        # Statistically random — uniform over full range
        max_range = 800 if not is_rebase else 1100
        samples = np.random.uniform(5, max_range, n)

    else:  # Other
        max_range = 500 if not is_rebase else 900
        samples = np.random.uniform(10, max_range, n)

    return np.round(samples, 1)


def generate_csv(csv_path):
    """Generate the canonical 300k-row CSV dataset."""

    # --- Without Rebase (150k) ---
    wo_pcts = {
        'Nuclear Exchange': 58.7,
        'Biosphere Collapse': 16.2,
        'AI Misalignment': 11.4,
        'Runaway Molecular Manufacturing': 7.3,
        'Engineered Pathogen Release': 3.8,
        'Natural Disaster': 1.4,
        'Other': 1.2,
    }

    # --- With Rebase (150k) ---
    wr_pcts = {
        'Nuclear Exchange': 0.47,
        'Biosphere Collapse': 51.2,
        'AI Misalignment': 28.4,
        'Runaway Molecular Manufacturing': 16.1,
        'Engineered Pathogen Release': 0.38,
        'Natural Disaster': 3.12,
        'Other': 0.34,
    }

    rows = []
    trial_id = 0

    for scenario, pcts, is_rebase in [
        ('Without Rebase', wo_pcts, False),
        ('With Rebase', wr_pcts, True),
    ]:
        for cat, pct in pcts.items():
            n = max(1, int(HALF * pct / 100))
            samples = _gen_category_samples(cat, None, n, is_rebase)
            subcats = SUBCATEGORIES[cat]

            for s in samples:
                rows.append({
                    'trial_id': trial_id,
                    'extinction_year': s,
                    'primary_cause': cat,
                    'subcategory': np.random.choice(subcats),
                    'project_rebase': is_rebase,
                })
                trial_id += 1

    df = pd.DataFrame(rows)

    # Verify and report
    actual_median = df['extinction_year'].median()
    print(f"Generated {len(df):,} rows")
    print(f"Combined median: {actual_median:.1f} yr (target: {TARGET_MEDIAN})")
    print(f"Without Rebase median: {df[~df['project_rebase']]['extinction_year'].median():.1f} yr")
    print(f"With Rebase median: {df[df['project_rebase']]['extinction_year'].median():.1f} yr")
    print(f"Year range: {df['extinction_year'].min():.0f} — {df['extinction_year'].max():.0f}")

    df.to_csv(csv_path, index=False)
    print(f"Saved: {csv_path}")
    return df


# =============================================================================
# HELPER: rgba conversion
# =============================================================================

def to_rgba(rgb_str, alpha=0.6):
    return rgb_str.replace('rgb', 'rgba').replace(')', f', {alpha})')


# =============================================================================
# CHART 1: RIDGELINE
# =============================================================================

def plot_ridgeline(df, output_dir):
    """Ridgeline plot — survival distributions by primary cause (blended)."""
    from scipy import stats

    fig = go.Figure()

    # Compute median per category (blended)
    cat_medians = df.groupby('primary_cause')['extinction_year'].median()
    sorted_cats = cat_medians.sort_values().index.tolist()

    y_spacing = 0.08
    x_range = np.linspace(0, 800, 800)

    for i, cat in enumerate(sorted_cats):
        samples = df[df['primary_cause'] == cat]['extinction_year'].values
        if len(samples) < 10:
            continue

        kde = stats.gaussian_kde(samples, bw_method=0.15)
        density = kde(x_range)

        # Normalize area
        area = np.trapezoid(density, x_range)
        density = density / area * 6  # equal visual weight

        baseline = i * y_spacing
        median = cat_medians[cat]

        # Filled ridge
        fig.add_trace(go.Scatter(
            x=np.concatenate([[x_range[0]], x_range, [x_range[-1]]]),
            y=np.concatenate([[baseline], density + baseline, [baseline]]),
            mode='lines', fill='toself',
            fillcolor=to_rgba(CAT_COLORS[cat], 0.6),
            line=dict(color=CAT_COLORS[cat], width=1.5),
            showlegend=False,
            hovertemplate=f'{cat}<br>Year %{{x:.0f}}<extra></extra>',
        ))

        # Baseline
        fig.add_trace(go.Scatter(
            x=[0, 800], y=[baseline, baseline],
            mode='lines', line=dict(color=CAT_COLORS[cat], width=0.5),
            showlegend=False, hoverinfo='skip',
        ))

        # Median diamond
        med_y = kde([median])[0] / area * 6 + baseline
        fig.add_trace(go.Scatter(
            x=[median], y=[med_y],
            mode='markers',
            marker=dict(color=COLORS['gold'], size=8, symbol='diamond'),
            showlegend=False,
            hovertemplate=f'{cat}<br>Median: {median:.0f} yr<extra></extra>',
        ))

        # Labels
        fig.add_annotation(x=-0.02, y=baseline + 0.025, xref='paper',
                           text=cat, showarrow=False,
                           font=dict(size=10, color=CAT_COLORS[cat]), xanchor='right')
        fig.add_annotation(x=1.02, y=baseline + 0.025, xref='paper',
                           text=f'{median:.0f} yr', showarrow=False,
                           font=dict(size=10, color=COLORS['gold']), xanchor='left')

    apply_style(fig, title="Species Survival Distribution by Primary Extinction Category",
                height=CHART_HEIGHT, width=CHART_WIDTH)
    fig.update_layout(margin=dict(l=230, r=80, t=70, b=70))
    fig.update_xaxes(title_text="Years to Extinction", range=[0, 800], dtick=100)
    fig.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)
    add_footnote(fig, SAMPLE_NOTE + ' | Equal area under each curve | ◆ = median')

    save_figure(fig, "extinction_ridgeline", output_dir)


# =============================================================================
# CHART 2: DUMBBELL
# =============================================================================

def plot_dumbbell(df, output_dir):
    """Dumbbell — with/without Rebase % shift per category."""

    fig = go.Figure()

    # Compute percentages by scenario
    for scenario_bool, scenario_name in [(False, 'Without Rebase'), (True, 'With Rebase')]:
        subset = df[df['project_rebase'] == scenario_bool]
        total = len(subset)
        counts = subset['primary_cause'].value_counts()
        pcts = (counts / total * 100)
        for cat in CATEGORY_ORDER:
            if cat not in pcts:
                pcts[cat] = 0.0

    # Build data
    categories = CATEGORY_ORDER[::-1]
    wo = df[~df['project_rebase']]
    wr = df[df['project_rebase']]
    wo_total = len(wo)
    wr_total = len(wr)

    for i, cat in enumerate(categories):
        wo_pct = wo[wo['primary_cause'] == cat].shape[0] / wo_total * 100
        wr_pct = wr[wr['primary_cause'] == cat].shape[0] / wr_total * 100

        # Line
        fig.add_trace(go.Scatter(
            x=[wo_pct, wr_pct], y=[i, i],
            mode='lines', line=dict(color=COLORS['text'], width=2),
            showlegend=False, hoverinfo='skip',
        ))
        # Without
        fig.add_trace(go.Scatter(
            x=[wo_pct], y=[i], mode='markers',
            marker=dict(color=COLORS['red'], size=12, symbol='circle',
                        line=dict(color=COLORS['white'], width=1)),
            name='Without Rebase' if i == 0 else None, showlegend=(i == 0),
            hovertemplate=f'{cat}<br>Without: {wo_pct:.2f}%<extra></extra>',
        ))
        # With
        fig.add_trace(go.Scatter(
            x=[wr_pct], y=[i], mode='markers',
            marker=dict(color=COLORS['green'], size=12, symbol='diamond',
                        line=dict(color=COLORS['white'], width=1)),
            name='With Rebase' if i == 0 else None, showlegend=(i == 0),
            hovertemplate=f'{cat}<br>With: {wr_pct:.2f}%<extra></extra>',
        ))
        # Delta
        delta = wr_pct - wo_pct
        if abs(delta) > 3:
            sign = '+' if delta > 0 else ''
            fig.add_annotation(
                x=max(wo_pct, wr_pct) + 2, y=i,
                text=f'{sign}{delta:.1f}%', showarrow=False,
                font=dict(size=10, color=COLORS['green'] if delta > 0 else COLORS['red']),
                xanchor='left',
            )

    apply_style(fig, title="Primary Extinction Category Shift: Without vs With Rebase",
                height=CHART_HEIGHT - 50, width=CHART_WIDTH)
    fig.update_layout(margin=MARGIN, legend=LEGEND_BOTTOM)
    fig.update_xaxes(title_text="Percentage of Trials (%)", range=[-2, 72], dtick=10)
    fig.update_yaxes(tickvals=list(range(len(categories))), ticktext=categories, tickfont=dict(size=11))
    add_footnote(fig, SAMPLE_NOTE)

    save_figure(fig, "extinction_dumbbell", output_dir)


# =============================================================================
# CHART 3: TREEMAP
# =============================================================================

def plot_treemap(df, output_dir):
    """Treemap — subcategories (rebase only), size=%, color=median survival."""

    wr = df[df['project_rebase']]
    wr_total = len(wr)

    labels, parents, values, colors, text_labels = [], [], [], [], []

    for cat in CATEGORY_ORDER:
        cat_df = wr[wr['primary_cause'] == cat]
        cat_pct = len(cat_df) / wr_total * 100
        cat_med = cat_df['extinction_year'].median() if len(cat_df) > 0 else 0

        labels.append(cat)
        parents.append('')
        values.append(cat_pct)
        colors.append(cat_med)
        text_labels.append(f'<b>{cat}</b><br>{cat_pct:.1f}%<br>{cat_med:.0f} yr')

        # Subcategories
        for sub in SUBCATEGORIES[cat]:
            sub_df = cat_df[cat_df['subcategory'] == sub]
            sub_pct = len(sub_df) / wr_total * 100
            sub_med = sub_df['extinction_year'].median() if len(sub_df) > 0 else 0

            labels.append(sub)
            parents.append(cat)
            values.append(sub_pct)
            colors.append(sub_med)
            if sub_pct > 1:
                text_labels.append(f'<b>{sub}</b><br>{sub_pct:.1f}%<br>{sub_med:.0f} yr')
            elif sub_pct > 0.3:
                text_labels.append(f'{sub}<br>{sub_pct:.2f}%')
            else:
                text_labels.append('')

    fig = go.Figure(go.Treemap(
        labels=labels, parents=parents, values=values,
        text=text_labels, textinfo='text',
        marker=dict(
            colors=colors,
            colorscale=[
                [0, '#b71c1c'], [0.35, '#e65100'],
                [0.5, '#f5f5f5'], [0.65, '#7cb342'], [1, '#1b5e20'],
            ],
            cmin=20, cmax=500,
            colorbar=dict(
                title=dict(text='Median<br>Survival<br>(years)', font=dict(size=11, color=COLORS['text'])),
                tickfont=dict(size=10, color=COLORS['text']), len=0.6,
            ),
            line=dict(color=COLORS['bg'], width=2),
        ),
        textfont=dict(size=11, color='#1a1a2e'),
        hovertemplate='<b>%{label}</b><br>Trials: %{value:.2f}%<br>Median: %{color:.0f} yr<extra></extra>',
        branchvalues='total',
        pathbar=dict(visible=True, textfont=dict(size=12, color=COLORS['text_bright']), thickness=24),
    ))

    apply_style(fig, title="Extinction Subcategories (With Rebase)",
                height=CHART_HEIGHT + 50, width=CHART_WIDTH)
    fig.update_layout(margin=dict(l=10, r=10, t=70, b=60))
    add_footnote(fig, SAMPLE_NOTE + ' | Box size = % of trials | Color = median survival')

    save_figure(fig, "extinction_treemap", output_dir)


# =============================================================================
# HISTOGRAM HELPERS
# =============================================================================

def _hist_frequency(samples, bin_size=BIN_SIZE, max_year=1000):
    """Compute frequency (%) histogram from samples."""
    bins = np.arange(0, max_year + bin_size, bin_size)
    counts, edges = np.histogram(samples, bins=bins)
    freq = counts / len(samples) * 100  # percentage
    centers = (edges[:-1] + edges[1:]) / 2
    return centers, freq, bins


def _add_median_line(fig, median_val, max_freq, label=None, color=None):
    """Add a vertical median line to a histogram."""
    c = color or COLORS['gold']
    fig.add_trace(go.Scatter(
        x=[median_val, median_val], y=[0, max_freq * 0.95],
        mode='lines', line=dict(color=c, width=2, dash='dot'),
        showlegend=False, hoverinfo='skip',
    ))
    txt = f'Median: {median_val:.0f} yr' if label is None else f'{label}: {median_val:.0f} yr'
    fig.add_annotation(
        x=median_val, y=max_freq * 0.97,
        text=txt, showarrow=False,
        font=dict(size=10, color=c), xanchor='left', xshift=5,
    )


# =============================================================================
# CHART 4: HISTOGRAM — OVERALL
# =============================================================================

def plot_histogram_overall(df, output_dir):
    fig = go.Figure()

    centers, freq, _ = _hist_frequency(df['extinction_year'].values)
    median = df['extinction_year'].median()

    fig.add_trace(go.Bar(
        x=centers, y=freq,
        marker=dict(color=COLORS['accent'], line=dict(width=0)),
        width=BIN_SIZE, hovertemplate='Year %{x:.0f}<br>%{y:.2f}%<extra></extra>',
    ))

    _add_median_line(fig, median, freq.max())

    apply_style(fig, title="Extinction Events by Year (All Trials)",
                height=HIST_HEIGHT, width=CHART_WIDTH)
    fig.update_layout(bargap=0, margin=MARGIN, showlegend=False)
    fig.update_xaxes(title_text="Years to Extinction", range=[0, 800], dtick=100)
    fig.update_yaxes(title_text="Frequency (%)")
    add_footnote(fig, SAMPLE_NOTE + ' | 2-year bins')

    save_figure(fig, "extinction_histogram_overall", output_dir)


# =============================================================================
# CHART 5: HISTOGRAM — STACKED BY CATEGORY
# =============================================================================

def plot_histogram_by_category(df, output_dir):
    fig = go.Figure()

    bins = np.arange(0, 1000 + BIN_SIZE, BIN_SIZE)

    plot_order = [
        'Biosphere Collapse', 'AI Misalignment', 'Runaway Molecular Manufacturing',
        'Nuclear Exchange', 'Natural Disaster', 'Engineered Pathogen Release', 'Other'
    ]

    total = len(df)
    max_freq = 0

    for cat in plot_order:
        samples = df[df['primary_cause'] == cat]['extinction_year'].values
        counts, edges = np.histogram(samples, bins=bins)
        freq = counts / total * 100
        centers = (edges[:-1] + edges[1:]) / 2
        max_freq = max(max_freq, freq.max())

        fig.add_trace(go.Bar(
            x=centers, y=freq, name=cat,
            marker=dict(color=CAT_COLORS[cat], line=dict(width=0)),
            width=BIN_SIZE, hovertemplate=f'{cat}<br>Year %{{x:.0f}}<br>%{{y:.2f}}%<extra></extra>',
        ))

    # Add median lines per category (top 3 only to avoid clutter)
    for cat in ['Biosphere Collapse', 'AI Misalignment', 'Nuclear Exchange']:
        med = df[df['primary_cause'] == cat]['extinction_year'].median()
        fig.add_shape(
            type='line', x0=med, x1=med, y0=0, y1=1,
            yref='paper', line=dict(color=CAT_COLORS[cat], width=1.5, dash='dot'),
        )
        fig.add_annotation(
            x=med, y=1.0, yref='paper',
            text=f'{cat.split()[0]}: {med:.0f}yr', showarrow=False,
            font=dict(size=8, color=CAT_COLORS[cat]), xanchor='left', xshift=4, yshift=4,
        )

    apply_style(fig, title="Extinction Events by Year and Category",
                height=HIST_HEIGHT, width=CHART_WIDTH)
    stacked_margin = dict(l=70, r=30, t=80, b=120)
    fig.update_layout(barmode='stack', bargap=0, margin=stacked_margin, legend=LEGEND_BOTTOM)
    fig.update_xaxes(title_text="Years to Extinction", range=[0, 800], dtick=100)
    fig.update_yaxes(title_text="Frequency (%)")
    fig.add_annotation(
        x=0.99, y=-0.30, xref='paper', yref='paper', xanchor='right',
        text=SAMPLE_NOTE + ' | 2-year bins',
        showarrow=False, font=dict(size=9, color=COLORS['text']),
    )

    save_figure(fig, "extinction_histogram_stacked", output_dir)


# =============================================================================
# CHART 6: HISTOGRAM — REBASE ONLY
# =============================================================================

def plot_histogram_rebase_only(df, output_dir):
    fig = go.Figure()

    wr = df[df['project_rebase']]
    centers, freq, _ = _hist_frequency(wr['extinction_year'].values)
    median = wr['extinction_year'].median()

    fig.add_trace(go.Bar(
        x=centers, y=freq,
        marker=dict(color=COLORS['green'], line=dict(width=0)),
        width=BIN_SIZE, hovertemplate='Year %{x:.0f}<br>%{y:.2f}%<extra></extra>',
    ))

    _add_median_line(fig, median, freq.max(), color=COLORS['gold'])

    apply_style(fig, title="Extinction Events by Year (With Rebase Only)",
                height=HIST_HEIGHT, width=CHART_WIDTH)
    fig.update_layout(bargap=0, margin=MARGIN, showlegend=False)
    fig.update_xaxes(title_text="Years to Extinction", range=[0, 800], dtick=100)
    fig.update_yaxes(title_text="Frequency (%)")
    add_footnote(fig, SAMPLE_NOTE + ' | With Rebase trials only | 2-year bins')

    save_figure(fig, "extinction_histogram_rebase_only", output_dir)


# =============================================================================
# CHART 7: HISTOGRAM — REBASE VS NON-REBASE
# =============================================================================

def plot_histogram_rebase_comparison(df, output_dir):
    fig = go.Figure()

    bins = np.arange(0, 1000 + BIN_SIZE, BIN_SIZE)
    total = len(df)

    for is_rebase, name, color in [
        (False, 'Without Rebase', COLORS['red']),
        (True, 'With Rebase', COLORS['green']),
    ]:
        subset = df[df['project_rebase'] == is_rebase]
        counts, edges = np.histogram(subset['extinction_year'].values, bins=bins)
        freq = counts / total * 100
        centers = (edges[:-1] + edges[1:]) / 2

        fig.add_trace(go.Bar(
            x=centers, y=freq, name=name,
            marker=dict(color=color, line=dict(width=0)),
            width=BIN_SIZE, opacity=0.75,
            hovertemplate=f'{name}<br>Year %{{x:.0f}}<br>%{{y:.2f}}%<extra></extra>',
        ))

    # Median lines
    for is_rebase, label, color in [
        (False, 'Without Rebase', COLORS['red']),
        (True, 'With Rebase', COLORS['green']),
    ]:
        med = df[df['project_rebase'] == is_rebase]['extinction_year'].median()
        max_y = 1.5
        fig.add_trace(go.Scatter(
            x=[med, med], y=[0, max_y],
            mode='lines', line=dict(color=color, width=2, dash='dot'),
            showlegend=False, hoverinfo='skip',
        ))
        fig.add_annotation(
            x=med, y=max_y * 1.02,
            text=f'{label}: {med:.0f} yr', showarrow=False,
            font=dict(size=9, color=color), xanchor='left', xshift=5,
        )

    apply_style(fig, title="Extinction Events: Rebase vs Non-Rebase",
                height=HIST_HEIGHT, width=CHART_WIDTH)
    comparison_margin = dict(l=70, r=30, t=80, b=100)
    fig.update_layout(barmode='stack', bargap=0, margin=comparison_margin, legend=LEGEND_BOTTOM)
    fig.update_xaxes(title_text="Years to Extinction", range=[0, 800], dtick=100)
    fig.update_yaxes(title_text="Frequency (%)")
    fig.add_annotation(
        x=0.99, y=-0.25, xref='paper', yref='paper', xanchor='right',
        text=SAMPLE_NOTE + ' | 50/50 trial split | 2-year bins',
        showarrow=False, font=dict(size=9, color=COLORS['text']),
    )

    save_figure(fig, "extinction_histogram_rebase_comparison", output_dir)


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "book", "assets", "figures"
    )
    os.makedirs(output_dir, exist_ok=True)

    csv_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "references", "extinction_trial_data.csv"
    )

    print("=" * 60)
    print("GENERATING CANONICAL DATASET")
    print("=" * 60)
    df = generate_csv(csv_path)

    print("\n" + "=" * 60)
    print("GENERATING CHARTS")
    print("=" * 60)

    plot_ridgeline(df, output_dir)
    plot_dumbbell(df, output_dir)
    plot_treemap(df, output_dir)
    plot_histogram_overall(df, output_dir)
    plot_histogram_by_category(df, output_dir)
    plot_histogram_rebase_only(df, output_dir)
    plot_histogram_rebase_comparison(df, output_dir)

    print("\n" + "=" * 60)
    print(f"All charts saved to {output_dir}/")
    print(f"Data saved to {csv_path}")
    print("=" * 60)
