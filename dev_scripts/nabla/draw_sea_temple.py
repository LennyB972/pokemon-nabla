#!/usr/bin/env python3
"""Draws the NablaSeaTemple map (data/layouts/NablaSeaTemple/map.bin), a mirage of the Eon Flute, under the sea.

The trench below Route 134 that leads down to the Sealed Chamber (tilesets General and Underwater), without the arch
of its top, the way up to the surface of Route 134: the rocks around it close it (blocks found so that each pair of
neighbours occurs in Emerald's maps). The player arrives at the top of the trench, diving (the map is underwater)
and swims down to the carved rock at its bottom (without its inscription in braille), the temple, where Manaphy
waits. Without a way up, there is nowhere to surface: the Eon Flute takes the player back.

Running it again overwrites the map, including changes made in Porymap since.
Usage (from the repo root): python3 dev_scripts/nabla/draw_sea_temple.py
"""
import struct

import reach

W, H = 22, 48
LEGENDARIES = {"MANAPHY": (12, 44)}
ARRIVAL = (7, 4)
# The arch at the top of the trench and the rocks at its sides
CLOSED_ARCH = {(5, 0): 0x21b, (6, 0): 0x21b, (7, 0): 0x21b, (8, 0): 0x21f, (9, 0): 0x21d,
               (5, 1): 0x206, (6, 1): 0x21b, (7, 1): 0x21b, (8, 1): 0x21b, (9, 1): 0x21b}

src = open("data/layouts/Underwater_SealedChamber/map.bin", "rb").read()
src = [[struct.unpack_from("<H", src, 2 * (y * W + x))[0] for x in range(W)] for y in range(H)]
ROCK = src[0][0] & ~0x3FF                           # collision of the rocks

out = [row[:] for row in src]
for (x, y), metatile in CLOSED_ARCH.items():
    out[y][x] = ROCK | metatile
# The inscription in braille on the carved rock: plain rock, like on its sides
out[43][12] = src[43][11]

# Every cell reached without Manaphy is reached with it, and it can be reached
cells, talked = reach.reach(out, ARRIVAL, LEGENDARIES.values())
alone, _ = reach.reach(out, ARRIVAL)
assert alone - cells <= set(LEGENDARIES.values()), alone - cells
assert talked == set(LEGENDARIES.values()), set(LEGENDARIES.values()) - talked
assert all(0 < x < W - 1 and 0 < y < H - 1 for x, y in alone), "reaches the edge of the map"
open("data/layouts/NablaSeaTemple/map.bin", "wb").write(struct.pack("<%dH" % (W * H), *[v for row in out for v in row]))
