#!/usr/bin/env python3
"""Draws the NablaTapuIslands map (data/layouts/NablaTapuIslands/map.bin), a mirage of the Eon Flute.

An archipelago of beaches, like the islands of Alola: a main island in the middle, with Zeraora in its meadow and
Marshadow in the shade of its trees, and four islets around it, one for each Tapu. The player arrives on the beach
of the main island, to the south, and surfs from one island to another. Sea rocks close the edges of the map.
coast.py turns the plan into blocks of the General tileset.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_tapu_islands.py
"""
import random

import coast

W, H = 42, 36
ARRIVAL = (20, 23)
LEGENDARIES = {"TAPU_LELE": (8, 7), "TAPU_KOKO": (33, 6), "TAPU_BULU": (10, 28), "TAPU_FINI": (32, 29),
               "ZERAORA": (20, 15), "MARSHADOW": (20, 20)}

# --- Plan: ellipses without their thin tips; grass two cells away from the sea (a ring of sand of two cells)
land = set()
for cx, cy, rx, ry in [(20.5, 18, 8.5, 6.5), (8.5, 7.5, 5.5, 4.3), (33.5, 6.5, 4.5, 3.5), (9, 28, 6, 5), (32.5, 29, 4, 3.3)]:
    land |= {(x, y) for y in range(H) for x in range(W) if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1}
core = {(x, y) for x, y in land if all((x + i, y + j) in land for i in (-1, 0, 1) for j in (-1, 0, 1))}
land = {(x + i, y + j) for x, y in core for i in (-1, 0, 1) for j in (-1, 0, 1)}
g = [["~" for _ in range(W)] for _ in range(H)]
for x, y in land:
    g[y][x] = "g" if all((x + i, y + j) in land for i in range(-2, 3) for j in range(-2, 3)) else "."
objects = []
rng = random.Random(3)


def put(x, y, c):
    g[y][x] = c


def tree(x, y):
    for j in range(3):
        for i in range(2):
            assert g[y + j][x + i] == "g", (x, y)
    objects.append(("tree", x, y, 3))


# The main island: four trees around Marshadow, flowers in the meadow
for x, y in [(16, 16), (24, 16), (18, 19), (22, 19)]:
    tree(x, y)
for x, y in [(16, 20), (25, 20), (15, 18), (26, 18), (18, 15), (23, 15)]:
    put(x, y, "f")
# The islets: flowers around Tapu Lele, a rock by Tapu Koko, a tree by Tapu Bulu, sand around Tapu Fini
for x, y in [(9, 6), (10, 7), (7, 8), (10, 8), (9, 9)]:
    put(x, y, "f")
put(34, 7, "o")
tree(7, 27)

coast.sea_rocks(g, objects, rng)
reached = coast.check_reachable(g, objects, ARRIVAL)
for name, (x, y) in LEGENDARIES.items():
    assert g[y][x] == "g" and (x, y) in reached, name
assert g[ARRIVAL[1]][ARRIVAL[0]] == "."
out, problems = coast.to_blocks(g, objects)
for p in problems:
    print("draw_tapu_islands.py: no block for", p)
coast.write("data/layouts/NablaTapuIslands/map.bin", out)
