#!/usr/bin/env python3
"""Draws the NablaBirdIslet map (data/layouts/NablaBirdIslet/map.bin), the first mirage of the Eon Flute.

A round islet in the open sea: a ring of sand, a meadow with trees and flowers, and three perches for the
legendary birds (north, west, east). The player arrives on the beach to the south. Sea rocks close the
edges of the map. coast.py turns the plan into blocks of the General tileset.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_bird_islet.py
"""
import random

import coast

W, H = 26, 24
ARRIVAL = (12, 19)
PERCHES = {"north": (12, 7), "west": (7, 12), "east": (18, 12)}

# --- Plan: the islet, row by row (first and last column of land)
ISLET = {4: (10, 15), 5: (8, 17), 6: (7, 18), 7: (6, 19), 8: (5, 20), 9: (5, 20), 10: (4, 21), 11: (4, 21),
         12: (4, 21), 13: (4, 21), 14: (4, 21), 15: (5, 20), 16: (5, 20), 17: (6, 19), 18: (7, 18), 19: (8, 17),
         20: (10, 15)}
g = [["~" for _ in range(W)] for _ in range(H)]
for y, (x0, x1) in ISLET.items():
    for x in range(x0, x1 + 1):
        g[y][x] = "."
land = {(x, y) for y in range(H) for x in range(W) if g[y][x] == "."}
# Grass two cells away from the sea, so that a ring of sand of two cells goes around it
for x, y in land:
    if all((x + i, y + j) in land for i in range(-2, 3) for j in range(-2, 3)):
        g[y][x] = "g"
objects = []
rng = random.Random(11)


def put(x, y, c):
    g[y][x] = c


def tree(x, y):
    for j in range(3):
        for i in range(2):
            assert g[y + j][x + i] == "g", (x, y)
    objects.append(("tree", x, y, 3))


# Trees at the corners of the meadow (the west and east perches between two of them), flowers and small rocks
for x, y in [(8, 9), (16, 9), (8, 13), (16, 13)]:
    tree(x, y)
for x, y in [(11, 9), (14, 9), (10, 12), (15, 12), (12, 15), (13, 15), (11, 11), (14, 11)]:
    put(x, y, "f")
for x, y in [(10, 16), (15, 8)]:
    put(x, y, "o")
for x, y in [(6, 9), (19, 15), (9, 18)]:
    put(x, y, "r")
for name, (x, y) in PERCHES.items():
    assert g[y][x] in "gf.", name
assert g[ARRIVAL[1]][ARRIVAL[0]] == ".", "arrival"


# Rocks in the sea along the edges of the map (see draw_west_beach.py): two neighbouring rocks always share
# a side, the corners are closed right at the edge
def is_water(x, y):
    return all(0 <= x + i < W and 0 <= y + j < H and g[y + j][x + i] == "~" for i in range(2) for j in range(2))


rocks = set()
def searock(x, y):
    assert is_water(x, y) and not any((x + i, y + j) in rocks for i in range(2) for j in range(2)), (x, y)
    objects.append(("searock", x, y, rng.choice(["foam", "foam", "brown", "moss"])))
    rocks.update((x + i, y + j) for i in range(2) for j in range(2))


for x in range(0, W, 2):
    corner = x in (0, 2, W - 4, W - 2)  # at the edge, next to the rocks of the side columns
    searock(x, 0 if corner else rng.choice([0, 1]))
    searock(x, H - 2 if corner or 8 <= x <= 17 else rng.choice([H - 2, H - 3]))  # away from the beach
for y in range(2, H - 2, 2):
    searock(rng.choice([0, 1]), y)
    searock(W - 2 - rng.choice([0, 1]), y)

# --- Every cell the player can reach (walking or surfing) is away from the edges of the map
blocked = rocks | {(x + i, y + j) for o in objects if o[0] == "tree" for x, y in [o[1:3]] for i in range(2) for j in range(3)}
seen, todo = set(), [ARRIVAL]
while todo:
    x, y = todo.pop()
    if (x, y) in seen or not (0 <= x < W and 0 <= y < H) or (x, y) in blocked or g[y][x] in "or":
        continue
    seen.add((x, y))
    assert 0 < x < W - 1 and 0 < y < H - 1, ("reaches the edge", x, y)
    todo += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

out, problems = coast.to_blocks(g, objects)
for p in problems:
    print("draw_bird_islet.py: no block for", p)
coast.write("data/layouts/NablaBirdIslet/map.bin", out)
