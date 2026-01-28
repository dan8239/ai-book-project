"""
Shared chart styling for the AI Book Project.

Usage:
    from chart_style import apply_style, COLORS, save_figure

All figures use a dark corporate dashboard aesthetic —
the kind of UI a researcher at Quant would actually see.
"""

import plotly.graph_objects as go
import plotly.io as pio

# Color palette
COLORS = {
    "bg": "#0a0e17",
    "paper": "#0a0e17",
    "grid": "#1a2035",
    "text": "#8892a0",
    "text_bright": "#c8d0dc",
    "accent": "#4fc3f7",       # primary data line
    "accent_dim": "#1a3a4a",   # muted version
    "gold": "#ffd54f",         # highlight / current epoch marker
    "red": "#ef5350",          # danger / extinction
    "green": "#66bb6a",        # success / survival
    "white": "#e0e0e0",
}

FONT = "IBM Plex Mono, Consolas, monospace"


def apply_style(fig: go.Figure, title: str = "", height: int = 500, width: int = 900) -> go.Figure:
    """Apply the standard Quant dashboard style to a plotly figure."""
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=COLORS["bg"],
        plot_bgcolor=COLORS["bg"],
        font=dict(family=FONT, size=13, color=COLORS["text"]),
        title=dict(
            text=title,
            font=dict(size=16, color=COLORS["text_bright"]),
            x=0.02,
            xanchor="left",
        ),
        height=height,
        width=width,
        margin=dict(l=60, r=30, t=60, b=50),
        xaxis=dict(
            gridcolor=COLORS["grid"],
            zerolinecolor=COLORS["grid"],
            tickfont=dict(size=11),
        ),
        yaxis=dict(
            gridcolor=COLORS["grid"],
            zerolinecolor=COLORS["grid"],
            tickfont=dict(size=11),
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=11, color=COLORS["text"]),
        ),
    )
    return fig


def save_figure(fig: go.Figure, name: str, assets_dir: str = None):
    """Save a figure as PNG to the assets/figures directory."""
    import os
    if assets_dir is None:
        assets_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "book", "assets", "figures"
        )
    os.makedirs(assets_dir, exist_ok=True)
    path = os.path.join(assets_dir, f"{name}.png")
    fig.write_image(path, scale=3)
    print(f"Saved: {path}")
    return path
