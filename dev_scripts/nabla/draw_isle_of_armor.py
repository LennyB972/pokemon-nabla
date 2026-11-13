#!/usr/bin/env python3
"""Draws the NablaIsleOfArmor map (data/layouts/NablaIsleOfArmor/map.bin), a mirage of the Eon Flute.

West Beach (draw_west_beach.py) as an island: the same beach, its grass islands, groves and rock mounds, but with the
sea to the east too, where Route 115 goes on, and rocks in the sea all around the edges of the map (coast.sea_rocks),
so that surfing never reaches them. Zacian and Zamazenta wait on the grass to the north, Kubfu by the grove to the
west (it comes with the player); the altar stands on the sand in the middle, Eternatus appears next to it. The player
arrives on the beach to the east.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_isle_of_armor.py
"""
import random

import coast
import reach

W, H = 36, 26
LEGENDARIES = {"ZACIAN": (13, 9), "ZAMAZENTA": (21, 8)}
GIFTS = {"KUBFU": (10, 15)}
ALTAR, ETERNATUS = (18, 12), (20, 12)
ARRIVAL = (27, 14)

# --- Plan of West Beach ("~" sea, "." sand, "g" grass, "T" tall grass, "f" flowers, "o" rock on grass, "r" rock on
# sand, "D" under a rock mound), with a shore to the east mirroring the one to the west
g = [["." for _ in range(W)] for _ in range(H)]
objects = []
rng = random.Random(7)
shore = [W, W, 6, 5, 5, 5, 4, 4, 4, 5, 5, 6, 6, 6, 5, 5, 5, 4, 4, 5, 5, 6, 6, 6, W, W]   # first sand column
east = [-1, -1, 28, 29, 29, 29, 30, 30, 30, 29, 29, 30, 30, 30, 29, 29, 30, 30, 30, 29, 29, 29, 29, 28, -1, -1]  # last
north = [2] * 6 + [2, 2, 2, 2, 3, 3, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3] + [3, 3, 2, 2, 2, 2]
south = [23] * 6 + [23, 23, 23, 23, 23, 22, 22, 22, 23, 23, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 22, 22] \
    + [22, 23, 23, 22, 22, 22]
for y in range(H):
    for x in range(W):
        if x < shore[y] or x > east[y] or y < north[x] or y > south[x]:
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


def island(x0, y0, w, h, tall=True):
    for y in range(y0, y0 + h):
        for x in range(x0, x0 + w):
            edge_row = y in (y0, y0 + h - 1)
            edge_col = x in (x0, x0 + w - 1)
            if edge_row and edge_col:
                continue  # rounded corners
            put(x, y, "T" if tall and not edge_row and not edge_col else "g")


# Groves and rock mounds of West Beach (the groves to the east now stand on the beach)
tree(26, 5, 7)
tree(26, 17, 5)
dome(22, 19); dome(11, 18)
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
coast.sea_rocks(g, objects, rng)
coast.check_reachable(g, objects, ARRIVAL)
out, problems = coast.to_blocks(g, objects)
assert not problems, problems

# Every cell reached without the objects is reached with them, they can be reached on foot, and surfing never
# reaches the edges of the map
OBJECTS = {ALTAR, ETERNATUS, *LEGENDARIES.values(), *GIFTS.values()}
cells, talked = reach.reach(out, ARRIVAL, OBJECTS)
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= OBJECTS, alone - cells
assert talked == OBJECTS, OBJECTS - talked
assert all(0 < x < W - 1 and 0 < y < H - 1 for x, y in alone), "reaches the edge of the map"
coast.write("data/layouts/NablaIsleOfArmor/map.bin", out)
