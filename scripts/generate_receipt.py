"""
Generate the SunBubble ride receipt for the Coffee Guy scene.

Run: python scripts/generate_receipt.py
"""

import plotly.graph_objects as go
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chart_style import COLORS, save_figure

FONT = "IBM Plex Mono, Consolas, monospace"

fig = go.Figure()

# Receipt content
lines = [
    ("TRIP COMPLETE", True, COLORS["text_bright"]),
    ("", False, ""),
    ("Duration               48 min", False, COLORS["text"]),
    ("Distance              42.3 mi", False, COLORS["text"]),
    ("", False, ""),
    ("Energy consumed     7,214 Wh", False, COLORS["text"]),
    ("Energy generated      182 Wh", False, COLORS["accent"]),
    ("Net transit         7,032 Wh", False, COLORS["text"]),
    ("", False, ""),
    ("Calories burned       740 kcal", False, COLORS["text"]),
    ("Avg power output      228 W", False, COLORS["text"]),
    ("", False, ""),
    ("─" * 34, False, COLORS["grid"]),
    ("Base fare            $115.42", False, COLORS["text"]),
    ("Energy credit         -$1.05", False, COLORS["green"]),
    ("─" * 34, False, COLORS["grid"]),
    ("Total                $114.37", True, COLORS["text_bright"]),
    ("", False, ""),
    ("Account balance   2,847,291 Wh", False, COLORS["accent"]),
]

# Build the receipt as annotations on a blank figure
y = len(lines)
for line_text, bold, color in lines:
    if not line_text:
        y -= 1
        continue
    fig.add_annotation(
        x=0,
        y=y,
        text=f"<b>{line_text}</b>" if bold else line_text,
        showarrow=False,
        font=dict(
            family=FONT,
            size=18,
            color=color,
        ),
        xanchor="left",
        yanchor="middle",
    )
    y -= 1

fig.update_layout(
    paper_bgcolor=COLORS["bg"],
    plot_bgcolor=COLORS["bg"],
    width=520,
    height=480,
    margin=dict(l=30, r=30, t=30, b=20),
    xaxis=dict(
        visible=False,
        range=[-0.5, 10],
    ),
    yaxis=dict(
        visible=False,
        range=[-0.5, len(lines) + 0.5],
    ),
)

save_figure(fig, "sunbubble_receipt")
print("\nEmbed with:")
print('![SunBubble Receipt](../../assets/figures/sunbubble_receipt.png)')
