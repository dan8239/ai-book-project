#!/usr/bin/env python3
"""Generate an H3 hexagonal globe visualization — mid-takeover look.

High-contrast continental map underneath. Green hex fills ONLY on land
cells, random opacity 0-1. Silver/gray hex borders everywhere.
Uses matplotlib + cartopy.
"""

import h3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from pathlib import Path

BG_COLOR = '#0d1117'
LAND_COLOR = '#0f151c'
OCEAN_COLOR = '#0a0e13'
OUTPUT_DIR = Path(__file__).parent.parent / 'book' / 'assets' / 'figures'

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
    """Collect H3 cells, classified as land or ocean."""
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
    Returns None if on the far side of the globe or antimeridian."""
    boundary = h3.cell_to_boundary(cell)
    lons = np.array([b[1] for b in boundary])
    lats = np.array([b[0] for b in boundary])
    if lons.max() - lons.min() > 180:
        return None
    coords = PROJ.transform_points(SRC, lons, lats)
    if np.any(np.isinf(coords[:, :2])):
        return None
    return coords[:, :2]


def generate_globe():
    fig = plt.figure(figsize=(10, 10), facecolor=BG_COLOR)
    ax = fig.add_subplot(1, 1, 1, projection=PROJ, facecolor=BG_COLOR)
    ax.set_global()

    # Globe outline
    ax.spines['geo'].set_edgecolor('#1a1f26')
    ax.spines['geo'].set_linewidth(0.5)

    # --- Base map (underneath everything) ---
    ax.add_feature(cfeature.OCEAN, facecolor=OCEAN_COLOR, zorder=0)
    ax.add_feature(cfeature.LAND, facecolor=LAND_COLOR, edgecolor='none', zorder=1)

    # --- Collect cells ---
    land1, ocean1 = collect_cells(res=1, step=4)
    land2, ocean2 = collect_cells(res=2, step=2)
    all_res1 = land1 | ocean1
    all_res2 = land2 | ocean2

    print(f"  Res 1: {len(land1)} land, {len(ocean1)} ocean")
    print(f"  Res 2: {len(land2)} land, {len(ocean2)} ocean")

    # --- Green fills: LAND CELLS ONLY, random opacity 0-1 ---
    NBUCKETS = 20
    fill_buckets = {}

    for cell in land2:
        xy = cell_to_xy(cell)
        if xy is None:
            continue
        opacity = np.random.uniform(0.0, 1.0)
        if opacity < 0.03:
            continue
        bucket = int(opacity * NBUCKETS)
        bucket = min(bucket, NBUCKETS - 1)
        fill_buckets.setdefault(bucket, []).append(xy)

    for bucket, polys in sorted(fill_buckets.items()):
        opacity = (bucket + 0.5) / NBUCKETS
        ax.add_collection(PolyCollection(
            polys,
            facecolors=[(102 / 255, 187 / 255, 106 / 255, opacity)],
            edgecolors='none',
            zorder=2,
        ))

    # --- Coastlines ON TOP — bright enough to see ---
    ax.add_feature(cfeature.COASTLINE, edgecolor='#8899aa', linewidth=0.7, zorder=5)

    # --- Silver/gray borders ---
    # Res 1 (large hexagons, all cells)
    res1_polys = [xy for cell in all_res1 if (xy := cell_to_xy(cell)) is not None]
    if res1_polys:
        ax.add_collection(PolyCollection(
            res1_polys,
            facecolors='none',
            edgecolors=(180 / 255, 185 / 255, 190 / 255, 0.20),
            linewidths=0.5,
            zorder=3,
        ))

    # Res 2 (medium hexagons, all cells)
    res2_polys = [xy for cell in all_res2 if (xy := cell_to_xy(cell)) is not None]
    if res2_polys:
        ax.add_collection(PolyCollection(
            res2_polys,
            facecolors='none',
            edgecolors=(180 / 255, 185 / 255, 190 / 255, 0.12),
            linewidths=0.2,
            zorder=4,
        ))

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
