#!/usr/bin/env python3
"""Draws the NablaWestBeach map (data/layouts/NablaWestBeach/map.bin) from a plan made of shapes.

The plan describes the sea, the shores, grass islands, trees and rocks; coast.py turns it into blocks of the
General and Fallarbor tilesets. It is also a base to draw other beaches.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_west_beach.py
"""
import random

import coast

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
# Off the map: the sea (border block), except the sand strip of Route 115 at the entrance (rows 12-16)
out, problems = coast.to_blocks(g, objects, lambda x, y: "s" if x >= W and 12 <= y <= 16 else "w")
for p in problems:
    print("draw_west_beach.py: no block for", p)
coast.write("data/layouts/NablaWestBeach/map.bin", out)
