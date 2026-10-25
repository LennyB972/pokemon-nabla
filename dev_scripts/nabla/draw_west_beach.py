#!/usr/bin/env python3
"""Draws the NablaWestBeach map (data/layouts/NablaWestBeach/map.bin) from a plan made of shapes.

The plan (first part) describes the sea, the shores, grass islands, trees and rocks; the second part turns
it into blocks of the General and Fallarbor tilesets: shores and grass edges are picked from the
neighbours of each cell, and each block keeps the collision and elevation it has in Emerald's maps.
The rules of the tiles are in docs/nabla/zones.md. It is also a base to draw other beaches.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_west_beach.py
"""
import collections
import json
import random
import struct
import sys

W, H = 30, 26

# --- Plan: "~" sea, "." sand, "g" grass, "T" tall grass, "f" flowers, "o" rock on grass, "r" rock on sand,
# "D" under a rock mound; objects (trees, mounds, sea rocks) are drawn over the cells
g = [["." for _ in range(W)] for _ in range(H)]
objects = []
rng = random.Random(7)
# The sea: to the west (first sand column of each row), to the north (first sand row of each column)
# and to the south (last sand row of each column)
shore = [W, W, 6, 5, 5, 5, 4, 4, 4, 5, 5, 6, 6, 6, 5, 5, 5, 4, 4, 5, 5, 6, 6, 6, W, W]
north = [2] * 6 + [2, 2, 2, 2, 3, 3, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3]
south = [23] * 6 + [23, 23, 23, 23, 23, 22, 22, 22, 23, 23, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 22, 22]
for y in range(H):
    for x in range(W):
        if x < shore[y] or y < north[x] or y > south[x]:
            g[y][x] = "~"
def put(x, y, c):
    g[y][x] = c
def tree(x, y, n=3):
    for j in range(n):
        put(x, y + j, "g"); put(x + 1, y + j, "g")
    objects.append(("tree", x, y, n))
def dome(x, y):
    for j in range(3):
        for i in range(3):
            put(x + i, y + j, "D")
    objects.append(("dome", x, y))
# Rocks in the sea along the edges of the map, so that the limits can be seen. Two neighbouring rocks
# always share a side (no gap to the edge of the map); the corners are closed right at the edge.
def is_water(x, y, w=2, h=2):
    return all(0 <= x + i < W and 0 <= y + j < H and g[y + j][x + i] == "~" for i in range(w) for j in range(h))
def searock(x, y):
    assert is_water(x, y), (x, y)
    objects.append(("searock", x, y, rng.choice(["foam", "foam", "brown", "moss"])))
    for i in range(2):
        for j in range(2):
            g[y + j][x + i] = "R"
for x in range(0, W, 2):
    top = 0 if x in (0, W - 2) else rng.choice([o for o in (0, 1) if is_water(x, o)])
    bottom = H - 2 if x in (0, W - 2) else rng.choice([o for o in (H - 2, H - 3) if is_water(x, o)])
    searock(x, top)
    searock(x, bottom)
for y in range(2, H - 2, 2):
    searock(rng.choice([o for o in (0, 1) if is_water(o, y)]), y)
for x, y in [(2, 8), (3, 13), (2, 18)]:
    if is_water(x, y):
        searock(x, y)
for y in range(H):
    for x in range(W):
        if g[y][x] == "R":
            g[y][x] = "~"
# Trees on both sides of the entrance (east, rows 12-16), with a strip of beach along the sea of Route 115
tree(26, 5, 7)
tree(26, 17, 5)
dome(22, 19); dome(11, 18)
# Grass islands with tall grass, and groves
def island(x0, y0, w, h, tall=True):
    for y in range(y0, y0 + h):
        for x in range(x0, x0 + w):
            edge_row = y in (y0, y0 + h - 1)
            edge_col = x in (x0, x0 + w - 1)
            if edge_row and edge_col:
                continue  # rounded corners
            put(x, y, "T" if tall and not edge_row and not edge_col else "g")
island(11, 5, 6, 5)
island(19, 5, 5, 4)
island(15, 14, 7, 5)
island(8, 10, 4, 5, tall=False)
tree(9, 11)
put(8, 12, "f"); put(11, 12, "f")
for y in range(4, 9):
    put(7, y, "g"); put(8, y, "g")
tree(7, 4)
put(7, 7, "f"); put(8, 8, "f")
for y in range(17, 22):
    put(8, y, "g"); put(9, y, "g")
tree(8, 17)
put(8, 20, "f"); put(9, 21, "f")
put(15, 5, "o"); put(22, 8, "f"); put(21, 15, "f"); put(16, 7, "f"); put(17, 18, "o")
for x, y in [(10, 16), (19, 11), (24, 14), (19, 21), (17, 11), (13, 13), (12, 4), (24, 4), (6, 15), (16, 21)]:
    put(x, y, "r")

# --- Blocks
# --- Usual block value (metatile + collision + elevation) of each metatile in Emerald's maps on General
values = collections.defaultdict(collections.Counter)
for l in json.load(open("data/layouts/layouts.json"))["layouts"]:
    if l.get("primary_tileset") != "gTileset_General" or "Nabla" in l.get("name", ""):
        continue
    try:
        data = open(l["blockdata_filepath"], "rb").read()
    except OSError:
        continue
    if len(data) != l["width"] * l["height"] * 2:
        continue
    for v in struct.unpack("<%dH" % (len(data) // 2), data):
        values[v & 0x3FF][v] += 1
def block(mt):
    return values[mt].most_common(1)[0][0] if values[mt] else mt | (3 << 12)

grid = g
objects = [[str(v) for v in o] for o in objects]
WATER, SAND, GRASS = "~", ".", "gTFfo"
def kind(x, y):
    # Off the map: the sea (border block), except the sand strip of Route 115 at the entrance (rows 12-16)
    if not (0 <= x < W and 0 <= y < H):
        return "s" if x >= W and 12 <= y <= 16 else "w"
    c = grid[y][x]
    return "w" if c in WATER else "s" if c in SAND + "rD" else "g"
out = [[0] * W for _ in range(H)]
WATER_EDGES = {(1,0,0,0): 0x11c, (0,1,0,0): 0x12c, (0,0,1,0): 0x123, (0,0,0,1): 0x125,
               (1,0,1,0): 0x11b, (1,0,0,1): 0x11d, (0,1,1,0): 0x12b, (0,1,0,1): 0x12d}
GRASS_EDGES = {(1,0,0,0): 0x119, (0,1,0,0): 0x129, (0,0,1,0): 0x120, (0,0,0,1): 0x122,
               (1,0,1,0): 0x118, (1,0,0,1): 0x11a, (0,1,1,0): 0x128, (0,1,0,1): 0x12a}
problems = []
for y in range(H):
    for x in range(W):
        c = grid[y][x]
        if c == "~":
            out[y][x] = block(0x170)
        elif c in ".rD":
            n = {d: kind(x + dx, y + dy) for d, (dx, dy) in {"u": (0,-1), "d": (0,1), "l": (-1,0), "r": (1,0)}.items()}
            wk = tuple(int(n[d] == "w") for d in "udlr")
            gk = tuple(int(n[d] == "g") for d in "udlr")
            if any(wk) and any(gk):
                problems.append((x, y, "water and grass"))
            if any(wk):
                mt = WATER_EDGES.get(wk)
                if mt is None:
                    problems.append((x, y, "water edges %s" % (wk,))); mt = 0x124
            elif any(gk):
                mt = GRASS_EDGES.get(gk)
                if mt is None:
                    problems.append((x, y, "grass edges %s" % (gk,))); mt = 0x124
            else:
                diag = {d: kind(x + dx, y + dy) for d, (dx, dy) in {"ul": (-1,-1), "ur": (1,-1), "dl": (-1,1), "dr": (1,1)}.items()}
                mt = {"ul": 0x13d, "ur": 0x13e, "dl": 0x145, "dr": 0x146}.get(next((d for d, k in diag.items() if k == "w"), None), 0x124)
            out[y][x] = block(mt)
            if c == "r":
                out[y][x] = block(0xe2)
        elif c == "T":
            out[y][x] = block(0x0d)
        elif c == "f":
            out[y][x] = block(0x04)
        elif c == "o":
            out[y][x] = block(0xe0)
        else:  # grass, and under trees
            below = grid[y + 1][x] if y + 1 < H else None
            out[y][x] = block(0x01)
# --- Objects: tree TX TY [rows] (2 wide), dome DX DY (3x3 on sand), rock2 in water
for o in objects:
    if o[0] == "tree":   # stacked trees, n rows = 3 + 2k
        x, y, n = int(o[1]), int(o[2]), int(o[3]) if len(o) > 3 else 3
        seq = [(0x1ce, 0x1cf), (0x1d6, 0x1d7)] + [((0x1dc, 0x1dd), (0x1d4, 0x1d5))[i % 2] for i in range(n - 3)] + [(0x1e6, 0x1e7)]
        for i, (a, b) in enumerate(seq):
            out[y + i][x], out[y + i][x + 1] = block(a), block(b)
    elif o[0] == "dome":
        x, y = int(o[1]), int(o[2])
        for j, r in enumerate([(0x80, 0x81, 0x82), (0x88, 0x71, 0x8a), (0x90, 0x79, 0x92)]):
            for i, mt in enumerate(r):
                out[y + j][x + i] = block(mt)
    elif o[0] == "searock":
        x, y = int(o[1]), int(o[2])
        kinds = {"foam": [(0x150, 0x151), (0x158, 0x159)], "brown": [(0x175, 0x176), (0x17d, 0x17e)], "moss": [(0x348, 0x349), (0x350, 0x351)]}
        for j, r in enumerate(kinds[o[3] if len(o) > 3 else "foam"]):
            for i, mt in enumerate(r):
                out[y + j][x + i] = block(mt)
for p in [p for p in problems if grid[p[1]][p[0]] != "D"]:  # cells under a mound are drawn over
    print("draw_west_beach.py: no block for", p)
open("data/layouts/NablaWestBeach/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
