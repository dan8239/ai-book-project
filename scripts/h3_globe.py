#!/usr/bin/env python3
"""Generate an H3 hexagonal globe visualization — mid-takeover look.

Silver/gray hex borders across the whole globe, with randomly filled
green hexagons at varying opacity (land cells more likely, some ocean
cells lit for a spreading-takeover effect). Uses matplotlib + cartopy
for proper polygon fills on an orthographic projection.
"""

import h3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PolyCollection
import cartopy.crs as ccrs
from pathlib import Path
import random

BG_COLOR = '#0d1117'
OUTPUT_DIR = Path(__file__).parent.parent / 'book' / 'assets' / 'figures'

random.seed(42)
np.random.seed(42)

PROJ = ccrs.Orthographic(central_longitude=-30, central_latitude=25)
SRC = ccrs.PlateCarree()


def is_land(lat, lon):
    """Rough land detection using continental bounding boxes."""
    regions = [
        (15, 72, -170, -50),   # North America
        (-56, 13, -82, -34),   # South America
        (35, 72, -12, 45),     # Europe
        (-35, 37, -18, 52),    # Africa
        (5, 75, 45, 180),      # Asia (east)
        (-45, -10, 112, 155),  # Australia
        (5, 35, 68, 98),       # India/SE Asia
        (30, 46, 128, 146),    # Japan/Korea
        (-8, 6, 95, 141),      # Indonesia
        (12, 42, 32, 63),      # Middle East
        (60, 84, -73, -12),    # Greenland
    ]
    for lat_lo, lat_hi, lon_lo, lon_hi in regions:
        if lat_lo < lat < lat_hi and lon_lo < lon < lon_hi:
            return True
    return False


def collect_cells(res, step):
    """Collect H3 cells at given resolution, classified as land or ocean."""
    land_cells = set()
    ocean_cells = set()
    for lat in np.arange(-70, 75, step):
        for lon in np.arange(-180, 180, step):
            cell = h3.latlng_to_cell(lat, lon, res)
            if is_land(lat, lon):
                land_cells.add(cell)
            else:
                ocean_cells.add(cell)
    ocean_cells -= land_cells
    return land_cells, ocean_cells


def cell_to_xy(cell):
    """Convert H3 cell boundary to projected x,y coordinates.
    Returns None if the cell is on the far side of the globe."""
    boundary = h3.cell_to_boundary(cell)
    lons = [b[1] for b in boundary]
    lats = [b[0] for b in boundary]

    # Skip cells that wrap around the antimeridian
    if max(lons) - min(lons) > 180:
        return None

    coords = PROJ.transform_points(SRC, np.array(lons), np.array(lats))
    # Filter out points at infinity (far side of globe)
    if np.any(np.isinf(coords[:, :2])):
        return None
    return coords[:, :2]


def generate_globe():
    fig = plt.figure(figsize=(10, 10), facecolor=BG_COLOR)
    ax = fig.add_subplot(1, 1, 1, projection=PROJ, facecolor=BG_COLOR)
    ax.set_global()

    # Subtle globe outline
    ax.spines['geo'].set_edgecolor('#1a1f26')
    ax.spines['geo'].set_linewidth(0.5)

    # --- Collect cells ---
    land1, ocean1 = collect_cells(res=1, step=4)
    land2, ocean2 = collect_cells(res=2, step=2)

    all_res1 = land1 | ocean1
    all_res2 = land2 | ocean2

    print(f"  Res 1: {len(land1)} land, {len(ocean1)} ocean = {len(all_res1)} total")
    print(f"  Res 2: {len(land2)} land, {len(ocean2)} ocean = {len(all_res2)} total")

    # --- Green fills at res 2 (mid-takeover) ---
    fill_levels = [0.10, 0.18, 0.28, 0.38, 0.50, 0.65]

    # Land fills: 85% chance, higher opacity
    land_polys = {}  # opacity -> list of xy arrays
    for cell in land2:
        if random.random() < 0.85:
            opacity = random.choice(fill_levels[2:])  # 0.28-0.65
            xy = cell_to_xy(cell)
            if xy is not None:
                land_polys.setdefault(opacity, []).append(xy)

    # Ocean fills: 12% chance, lower opacity
    ocean_polys = {}
    for cell in ocean2:
        if random.random() < 0.12:
            opacity = random.choice(fill_levels[:3])  # 0.10-0.28
            xy = cell_to_xy(cell)
            if xy is not None:
                ocean_polys.setdefault(opacity, []).append(xy)

    # Render fills as PolyCollections (efficient)
    for opacity, polys in sorted({**land_polys, **ocean_polys}.items()):
        # Merge polys from land and ocean at same opacity
        all_at_level = polys
        if opacity in land_polys and opacity in ocean_polys:
            all_at_level = land_polys.get(opacity, []) + ocean_polys.get(opacity, [])
        pc = PolyCollection(
            all_at_level,
            facecolors=[(102/255, 187/255, 106/255, opacity)],
            edgecolors='none',
            zorder=2,
        )
        ax.add_collection(pc)

    # --- Silver/gray borders ---
    # Res 1 borders (large hexagons)
    res1_polys = []
    for cell in all_res1:
        xy = cell_to_xy(cell)
        if xy is not None:
            res1_polys.append(xy)

    if res1_polys:
        pc1 = PolyCollection(
            res1_polys,
            facecolors='none',
            edgecolors=(180/255, 185/255, 190/255, 0.30),
            linewidths=0.6,
            zorder=3,
        )
        ax.add_collection(pc1)

    # Res 2 borders (medium hexagons)
    res2_polys = []
    for cell in all_res2:
        xy = cell_to_xy(cell)
        if xy is not None:
            res2_polys.append(xy)

    if res2_polys:
        pc2 = PolyCollection(
            res2_polys,
            facecolors='none',
            edgecolors=(180/255, 185/255, 190/255, 0.18),
            linewidths=0.3,
            zorder=4,
        )
        ax.add_collection(pc2)

    # --- Save ---
    output_path = OUTPUT_DIR / 'h3_globe.png'
    fig.savefig(
        str(output_path),
        dpi=200,
        bbox_inches='tight',
        pad_inches=0,
        facecolor=BG_COLOR,
    )
    plt.close(fig)
    print(f"Saved: {output_path}")


if __name__ == '__main__':
    generate_globe()
