#!/usr/bin/env python3
"""Generate an H3 hexagonal globe visualization — mid-takeover look.

Uses actual Natural Earth land geometry for accurate coastline-following
fills. Green hex fills ONLY on cells whose centers fall within real land
polygons. Random opacity 0-1. Silver/gray hex borders everywhere.
"""

import h3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io import shapereader
from shapely.geometry import Point
from shapely.ops import unary_union
from shapely.prepared import prep
from pathlib import Path

BG_COLOR = '#0d1117'
LAND_COLOR = '#c0c8d0'   # near-white gray
OCEAN_COLOR = '#0a0e13'
OUTPUT_DIR = Path(__file__).parent.parent / 'book' / 'assets' / 'figures'

np.random.seed(42)

PROJ = ccrs.Orthographic(central_longitude=-30, central_latitude=25)
SRC = ccrs.PlateCarree()


def build_land_geometry():
    """Load Natural Earth land polygons and build a prepared geometry for fast lookup."""
    shpfile = shapereader.natural_earth(resolution='110m', category='physical', name='land')
    reader = shapereader.Reader(shpfile)
    land_geom = unary_union(list(reader.geometries()))
    return prep(land_geom)


def collect_cells(res, step, land_prep):
    """Collect H3 cells, classified using actual land geometry."""
    land_cells = set()
    ocean_cells = set()
    for lat in np.arange(-70, 75, step):
        for lon in np.arange(-180, 180, step):
            cell = h3.latlng_to_cell(lat, lon, res)
            # Check cell center against real land polygons
            clat, clon = h3.cell_to_latlng(cell)
            if land_prep.contains(Point(clon, clat)):
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
    print("Loading land geometry...")
    land_prep = build_land_geometry()

    fig = plt.figure(figsize=(10, 10), facecolor=BG_COLOR)
    ax = fig.add_subplot(1, 1, 1, projection=PROJ, facecolor=BG_COLOR)
    ax.set_global()

    # Globe outline
    ax.spines['geo'].set_edgecolor('#1a1f26')
    ax.spines['geo'].set_linewidth(0.5)

    # --- Base map (underneath everything) ---
    ax.add_feature(cfeature.OCEAN, facecolor=OCEAN_COLOR, zorder=0)
    ax.add_feature(cfeature.LAND, facecolor=LAND_COLOR, edgecolor='none', zorder=1)

    # --- Collect cells using real land geometry ---
    land1, ocean1 = collect_cells(res=1, step=4, land_prep=land_prep)
    land2, ocean2 = collect_cells(res=2, step=2, land_prep=land_prep)
    # Res 3 for fine-grained land fills
    land3, ocean3 = collect_cells(res=3, step=1.0, land_prep=land_prep)
    all_res1 = land1 | ocean1
    all_res2 = land2 | ocean2

    print(f"  Res 1: {len(land1)} land, {len(ocean1)} ocean")
    print(f"  Res 2: {len(land2)} land, {len(ocean2)} ocean")
    print(f"  Res 3: {len(land3)} land, {len(ocean3)} ocean")

    # --- Green fills: res 3 LAND CELLS ONLY ---
    # ~33% transparent (no fill), rest get random opacity 0-1
    GREEN = (66 / 255, 187 / 255, 106 / 255)  # single green color
    NBUCKETS = 20
    fill_buckets = {}

    for cell in land3:
        xy = cell_to_xy(cell)
        if xy is None:
            continue
        if np.random.random() < 0.50:
            continue  # 33% stay transparent
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
            facecolors=[(*GREEN, opacity)],
            edgecolors='none',
            zorder=2,
        ))

    # --- Coastlines ON TOP — bright enough to contrast ---
    ax.add_feature(cfeature.COASTLINE, edgecolor='#8899aa', linewidth=0.7, zorder=5)

    # --- Silver/gray borders ---
    # Res 1 (large hexagons, all cells)
    res1_polys = [xy for cell in all_res1 if (xy := cell_to_xy(cell)) is not None]
    if res1_polys:
        ax.add_collection(PolyCollection(
            res1_polys,
            facecolors='none',
            edgecolors=(180 / 255, 185 / 255, 190 / 255, 0.25),
            linewidths=0.8,
            zorder=3,
        ))

    # Res 2 (medium hexagons, all cells)
    res2_polys = [xy for cell in all_res2 if (xy := cell_to_xy(cell)) is not None]
    if res2_polys:
        ax.add_collection(PolyCollection(
            res2_polys,
            facecolors='none',
            edgecolors=(180 / 255, 185 / 255, 190 / 255, 0.16),
            linewidths=0.35,
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
