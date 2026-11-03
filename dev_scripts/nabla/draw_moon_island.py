#!/usr/bin/env python3
"""Draws the NablaMoonIsland map (data/layouts/NablaMoonIsland/map.bin), a mirage of the Eon Flute.

An island above the sea like Birth Island (tilesets General and Dewford): its mountain, cliffs and trees are
taken from Birth Island's map, without the dock, the stairs and the triangle of light grass. On the summit, a
full moon of light grass, where Cresselia waits by day and Darkrai at night. The sea cannot be crossed.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_moon_island.py
"""
import struct

W, H = 30, 24
MOON = (15, 11)    # Cresselia and Darkrai
ARRIVAL = (15, 16)

src_w = 30
src = open("data/layouts/BirthIsland_Exterior/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * src_w + x))[0] for x in range(src_w)] for y in range(30)]
SEA = src[0][0]
GRASS = src[6][14]                # 0x001
CLIFF = src[17][14]               # 0x07c, the face of the cliff
WATERLINE = src[20][13]           # 0x189, the sea at the foot of the cliff
LIGHT = range(0x1d0, 0x1e3)       # the triangle of light grass (0x1d0-0x1e2)

out = [[SEA] * W for _ in range(H)]
for y in range(21):               # the island, down to the sea at the foot of its cliff
    for x in range(W):
        v = src[y][x]
        mt = v & 0x3FF
        if mt in LIGHT:
            v = GRASS
        elif mt == 0x0AF:         # stairs down to the dock
            v = CLIFF
        elif mt in (0x343, 0x344, 0x345):  # top of the dock
            v = WATERLINE
        elif mt == 0x308:         # light grass under the summit's tree
            v = GRASS
        out[y][x] = v
# The two trees by the cliff: their sides drawn against the triangle of light grass take the grass side of the
# other tree
for y in (14, 15, 16):
    out[y][10], out[y][20] = src[y][23], src[y][7]

# The full moon: a disc of light grass, its edges and corners picked from its neighbours
cx, cy = MOON
disc = {(x, y) for y in range(cy - 2, cy + 3) for x in range(cx - 2, cx + 3)
        if (x - cx) ** 2 + (y - cy) ** 2 <= 2.5 ** 2}
for x, y in disc:
    assert out[y][x] == GRASS, (x, y)
    up, down, left, right = (x, y - 1) in disc, (x, y + 1) in disc, (x - 1, y) in disc, (x + 1, y) in disc
    row = 0x1d0 if not up else 0x1e0 if not down else 0x1d8
    col = 0 if not left else 2 if not right else 1
    out[y][x] = GRASS & ~0x3FF | (row + col)
assert out[ARRIVAL[1]][ARRIVAL[0]] == GRASS

open("data/layouts/NablaMoonIsland/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
