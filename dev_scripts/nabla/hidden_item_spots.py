#!/usr/bin/env python3
"""Lists good spots for a hidden item on a map, best first.

A spot is a walkable land tile reachable on foot from the map's warps or
edges, with no event on it, away from the map edges, and preferably in a
corner or a dead end (more blocked neighbours). Object events (NPCs, cuttable
trees, breakable rocks, boulders) block the way, so spots needing an HM to
reach are left out, and spots right next to an object are skipped.

Usage (from the repo root): python3 dev_scripts/nabla/hidden_item_spots.py MAP_FOLDER [COUNT]
Example: python3 dev_scripts/nabla/hidden_item_spots.py Route104 5
"""
import json
import struct
import sys
from collections import deque

WATER_ELEVATION = 1
EDGE_MARGIN = 2


def load_map(map_name):
    map_json = json.load(open(f"data/maps/{map_name}/map.json"))
    layouts = json.load(open("data/layouts/layouts.json"))["layouts"]
    layout = next(l for l in layouts if l.get("id") == map_json["layout"])
    width, height = layout["width"], layout["height"]
    data = open(layout["blockdata_filepath"], "rb").read()
    blocks = [[struct.unpack_from("<H", data, 2 * (y * width + x))[0] for x in range(width)] for y in range(height)]
    return map_json, width, height, blocks


def is_walkable(block):
    collision = (block >> 10) & 3
    elevation = block >> 12
    return collision == 0 and elevation != WATER_ELEVATION


def find_spots(map_name):
    map_json, width, height, blocks = load_map(map_name)
    objects = {(o["x"], o["y"]) for o in map_json.get("object_events") or []}
    events = set()
    for kind in ("object_events", "warp_events", "coord_events", "bg_events"):
        for event in map_json.get(kind) or []:
            events.add((event["x"], event["y"]))

    # Start from warps and walkable tiles on the map edges (connections)
    starts = [(w["x"], w["y"]) for w in map_json.get("warp_events") or []]
    for x in range(width):
        starts += [(x, 0), (x, height - 1)]
    for y in range(height):
        starts += [(0, y), (width - 1, y)]

    reachable = set()
    queue = deque()
    for x, y in starts:
        if 0 <= x < width and 0 <= y < height and is_walkable(blocks[y][x]):
            reachable.add((x, y))
            queue.append((x, y))
    # Warps can sit on blocked tiles (doors): step off them
    for x, y in [(w["x"], w["y"]) for w in map_json.get("warp_events") or []]:
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < width and 0 <= ny < height and is_walkable(blocks[ny][nx]) and (nx, ny) not in reachable:
                reachable.add((nx, ny))
                queue.append((nx, ny))
    while queue:
        x, y = queue.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (0 <= nx < width and 0 <= ny < height and (nx, ny) not in reachable
             and (nx, ny) not in objects and is_walkable(blocks[ny][nx])):
                reachable.add((nx, ny))
                queue.append((nx, ny))

    # Elevation 15 is used by bridges, and 0 by multi-level tiles unless the whole map lies at 0
    elevations = [blocks[y][x] >> 12 for x, y in reachable]
    ground = max(set(elevations), key=elevations.count) if elevations else 3
    excluded = {15} if ground == 0 else {0, 15}

    spots = []
    for x, y in reachable:
        if (x, y) in events:
            continue
        # Keep away from other objects (NPCs, other item balls)
        if any(abs(x - ox) + abs(y - oy) <= 2 for ox, oy in objects):
            continue
        if not (EDGE_MARGIN <= x < width - EDGE_MARGIN and EDGE_MARGIN <= y < height - EDGE_MARGIN):
            continue
        if blocks[y][x] >> 12 in excluded:
            continue
        blocked = sum(1 for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)) if (nx, ny) not in reachable)
        if 2 <= blocked <= 3:
            spots.append((blocked, x, y, blocks[y][x] >> 12))
    # Dead ends first, then a stable order
    spots.sort(key=lambda s: (-s[0], s[2], s[1]))
    return spots


if __name__ == "__main__":
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    for blocked, x, y, elevation in find_spots(sys.argv[1])[:count]:
        print(f"x={x} y={y} elevation={elevation} blocked_neighbours={blocked}")
