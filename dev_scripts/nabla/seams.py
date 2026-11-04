#!/usr/bin/env python3
"""Lists the pairs of neighbouring blocks of a map that no map of Emerald contains: where a drawing may not join
well (a cliff cut off, a hole in a wall). Look at each one: some are harmless (flowers next to a pond).

Usage (from the repo root): python3 dev_scripts/nabla/seams.py <Map or LAYOUT_ID>
"""
import json
import struct
import sys

LAYOUTS = [l for l in json.load(open("data/layouts/layouts.json"))["layouts"] if "id" in l]


def metatiles(layout):
    raw = open(layout["blockdata_filepath"], "rb").read()
    W, H = layout["width"], layout["height"]
    return [[struct.unpack_from("<H", raw, 2 * (y * W + x))[0] & 0x3FF for x in range(W)] for y in range(H)]


def pairs(layout):
    """The pairs of neighbouring metatiles of a layout, each metatile named with its tileset."""
    m = metatiles(layout)
    name = lambda v: (layout["primary_tileset"] if v < 0x200 else layout["secondary_tileset"], v)
    for y in range(layout["height"]):
        for x in range(layout["width"]):
            if x + 1 < layout["width"]:
                yield (x, y), "|", name(m[y][x]), name(m[y][x + 1])
            if y + 1 < layout["height"]:
                yield (x, y), "/", name(m[y][x]), name(m[y + 1][x])


if __name__ == "__main__":
    arg = sys.argv[1]
    layout_id = arg if arg.startswith("LAYOUT_") else json.load(open("data/maps/%s/map.json" % arg))["layout"]
    known = {p[1:] for l in LAYOUTS if "NABLA" not in l["id"] and "Frlg" not in l["name"] for p in pairs(l)}
    unknown = [p for p in pairs(next(l for l in LAYOUTS if l["id"] == layout_id)) if p[1:] not in known]
    for (x, y), d, a, b in unknown:
        print("(%d, %d) %s: %03x %s %03x" % (x, y, "and its right" if d == "|" else "over its bottom", a[1], d, b[1]))
    print("%d pairs unknown to Emerald" % len(unknown))
