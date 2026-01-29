#!/usr/bin/env python3
"""Generate an H3 hexagonal globe visualization — mid-takeover look.

Continental map underneath, silver/gray hex borders, green fills radiating
outward from major population centers (opacity 0-1). Uses matplotlib + cartopy.
"""

import h3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from pathlib import Path

BG_COLOR = '#0d1117'
LAND_COLOR = '#141a1f'
OCEAN_COLOR = '#0d1117'
OUTPUT_DIR = Path(__file__).parent.parent / 'book' / 'assets' / 'figures'

np.random.seed(42)

PROJ = ccrs.Orthographic(central_longitude=-30, central_latitude=25)
SRC = ccrs.PlateCarree()

# Major population centers (lat, lon) — takeover radiates from these
POP_CENTERS = [
    (40.7, -74.0),    # New York
    (51.5, -0.1),     # London
    (48.9, 2.3),      # Paris
    (55.8, 37.6),     # Moscow
    (35.7, 139.7),    # Tokyo
    (39.9, 116.4),    # Beijing
    (31.2, 121.5),    # Shanghai
    (19.1, 72.9),     # Mumbai
    (28.6, 77.2),     # Delhi
    (-23.6, -46.6),   # São Paulo
    (6.5, 3.4),       # Lagos
    (30.0, 31.2),     # Cairo
    (-33.9, 18.4),    # Cape Town
    (34.1, -118.2),   # Los Angeles
    (-33.4, -70.7),   # Santiago
    (1.3, 103.8),     # Singapore
    (37.6, 127.0),    # Seoul
    (52.5, 13.4),     # Berlin
    (41.0, 28.9),     # Istanbul
    (13.8, 100.5),    # Bangkok
    (-6.2, 106.8),    # Jakarta
    (35.7, 51.4),     # Tehran
    (14.6, -90.5),    # Guatemala City
    (25.3, 55.3),     # Dubai
    (-1.3, 36.8),     # Nairobi
    (43.7, -79.4),    # Toronto
    (59.3, 18.1),     # Stockholm
    (22.3, 114.2),    # Hong Kong
]

EARTH_RADIUS_KM = 6371.0


def haversine_km(lat1, lon1, lat2, lon2):
    """Great-circle distance in km between two points."""
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    return EARTH_RADIUS_KM * 2 * np.arcsin(np.sqrt(a))


def distance_to_nearest_center(lat, lon):
    """Min great-circle distance from (lat,lon) to any population center."""
    dists = [haversine_km(lat, lon, clat, clon) for clat, clon in POP_CENTERS]
    return min(dists)


def opacity_from_distance(dist_km):
    """Map distance to opacity: near centers = 1.0, far = 0.0.
    Sharp falloff over ~2500 km with slight noise for organic feel."""
    MAX_DIST = 2500.0
    base = max(0.0, 1.0 - (dist_km / MAX_DIST) ** 1.8)
    noise = np.random.uniform(-0.06, 0.06)
    return float(np.clip(base + noise, 0.0, 1.0))


def collect_cells(res, step):
    """Collect all H3 cells at given resolution."""
    cells = set()
    for lat in np.arange(-70, 75, step):
        for lon in np.arange(-180, 180, step):
            cells.add(h3.latlng_to_cell(lat, lon, res))
    return cells


def cell_to_xy(cell):
    """Convert H3 cell boundary to projected x,y coordinates.
    Returns None if the cell is on the far side of the globe."""
    boundary = h3.cell_to_boundary(cell)
    lons = np.array([b[1] for b in boundary])
    lats = np.array([b[0] for b in boundary])

    # Skip cells that wrap around the antimeridian
    if lons.max() - lons.min() > 180:
        return None

    coords = PROJ.transform_points(SRC, lons, lats)
    if np.any(np.isinf(coords[:, :2])):
        return None
    return coords[:, :2]


def cell_center(cell):
    """Return (lat, lon) of cell center."""
    lat, lon = h3.cell_to_latlng(cell)
    return lat, lon


def generate_globe():
    fig = plt.figure(figsize=(10, 10), facecolor=BG_COLOR)
    ax = fig.add_subplot(1, 1, 1, projection=PROJ, facecolor=BG_COLOR)
    ax.set_global()

    # Globe outline
    ax.spines['geo'].set_edgecolor('#1a1f26')
    ax.spines['geo'].set_linewidth(0.5)

    # --- Continental map underneath ---
    ax.add_feature(cfeature.OCEAN, facecolor=OCEAN_COLOR, zorder=0)
    ax.add_feature(cfeature.LAND, facecolor=LAND_COLOR, edgecolor='none', zorder=1)
    ax.add_feature(cfeature.COASTLINE, edgecolor='#2a3540', linewidth=0.3, zorder=1)

    # --- Collect cells ---
    all_res1 = collect_cells(res=1, step=4)
    all_res2 = collect_cells(res=2, step=2)

    print(f"  Res 1: {len(all_res1)} cells")
    print(f"  Res 2: {len(all_res2)} cells")

    # --- Green fills at res 2, opacity based on distance to pop centers ---
    # Quantize opacity to ~20 buckets for rendering efficiency
    NBUCKETS = 20
    fill_buckets = {}  # bucket_index -> list of xy arrays

    for cell in all_res2:
        xy = cell_to_xy(cell)
        if xy is None:
            continue
        lat, lon = cell_center(cell)
        dist = distance_to_nearest_center(lat, lon)
        opacity = opacity_from_distance(dist)
        if opacity < 0.02:
            continue  # skip near-invisible cells
        bucket = int(opacity * NBUCKETS)
        bucket = min(bucket, NBUCKETS - 1)
        fill_buckets.setdefault(bucket, []).append(xy)

    for bucket, polys in sorted(fill_buckets.items()):
        opacity = (bucket + 0.5) / NBUCKETS
        pc = PolyCollection(
            polys,
            facecolors=[(102 / 255, 187 / 255, 106 / 255, opacity)],
            edgecolors='none',
            zorder=2,
        )
        ax.add_collection(pc)

    # --- Silver/gray borders ---
    # Res 1 borders (large hexagons)
    res1_polys = [xy for cell in all_res1 if (xy := cell_to_xy(cell)) is not None]
    if res1_polys:
        ax.add_collection(PolyCollection(
            res1_polys,
            facecolors='none',
            edgecolors=(180 / 255, 185 / 255, 190 / 255, 0.25),
            linewidths=0.6,
            zorder=3,
        ))

    # Res 2 borders (medium hexagons)
    res2_polys = [xy for cell in all_res2 if (xy := cell_to_xy(cell)) is not None]
    if res2_polys:
        ax.add_collection(PolyCollection(
            res2_polys,
            facecolors='none',
            edgecolors=(180 / 255, 185 / 255, 190 / 255, 0.15),
            linewidths=0.25,
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
