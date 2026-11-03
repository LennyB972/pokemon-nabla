#!/usr/bin/env python3
"""Draws the NablaLibertyIsland map (data/layouts/NablaLibertyIsland/map.bin), a mirage of the Eon Flute.

An island above the sea taken from Navel Rock's map (tilesets General and Dewford): a ring of sand on top of its
cliffs, around a rock in the middle, without the stairs, the dock, the harbor, the entrance of the cave and the
pebbles; its corners to the south are square, so that the whole ring can be walked.
Victini and Meloetta wait on the ring, to the north. The player arrives on the ring, to the south. The sea cannot
be crossed.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_liberty_island.py
"""
import struct

W, H = 21, 24
VICTINI, MELOETTA = (9, 4), (11, 4)
ARRIVAL = (10, 12)

src = open("data/layouts/NavelRock_Exterior/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
mt = lambda v: v & 0x3FF
SEA, SAND = src[0][0], src[4][8]                   # 0x170, 0x121
FACE, FACE_BOTTOM, WATERLINE = src[13][5], src[10][9], src[14][5]  # 0x07c, 0x091, 0x189

out = [row[:] for row in src]
for y in range(H):
    for x in range(W):
        if y >= 15 and mt(src[y][x]) >= 0x352:   # the harbor
            out[y][x] = SEA
        elif mt(src[y][x]) in (0x34b, 0x34c, 0x34d):  # the dock
            out[y][x] = SEA
out[13][9:12] = [FACE] * 3                         # the stairs: cliff
out[14][9:12] = [WATERLINE] * 3                    # the top of the dock: sea at the foot of the cliff
out[10][10] = FACE_BOTTOM                          # the entrance of the cave: rock
out[9][10] = FACE
# The pebbles: sand
for x, y in [(14, 5), (6, 6), (6, 9), (13, 10)]:
    out[y][x] = SAND
# The corners of rock in diagonal that cut the south of the ring from its sides: square corners instead, the
# inner sides of the ring going down to the cliff of the south
LEFT_SIDE, RIGHT_SIDE = src[7][5], src[7][15]      # 0x17c, 0x088
for y in (10, 11, 12):
    out[y][5], out[y][15] = LEFT_SIDE, RIGHT_SIDE
    for x in (6, 7, 13, 14):
        out[y][x] = SAND

# The whole ring can be walked from the arrival
free = lambda x, y: 0 <= x < W and 0 <= y < H and not (out[y][x] >> 10) & 3
seen, todo = set(), [ARRIVAL]
while todo:
    x, y = todo.pop()
    if (x, y) in seen or not free(x, y):
        continue
    seen.add((x, y))
    todo += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
for x, y in (VICTINI, MELOETTA, ARRIVAL):
    assert out[y][x] == SAND and (x, y) in seen, (x, y)
open("data/layouts/NablaLibertyIsland/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
