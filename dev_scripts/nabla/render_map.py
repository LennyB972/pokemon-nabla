#!/usr/bin/env python3
"""Renders a map (or a part of it) to a PNG image, to look at maps without Porymap.

Usage (from the repo root):
  python3 dev_scripts/nabla/render_map.py Route115 out.png            whole map
  python3 dev_scripts/nabla/render_map.py Route115 out.png 0 50 40 30  x y width height (in metatiles)
  python3 dev_scripts/nabla/render_map.py LAYOUT_ROUTE130_MIRAGE_ISLAND out.png   a layout without its own map
Options: --grid draws a line every 5 metatiles (labels every 10), --collision shades blocked metatiles.
"""
import json
import re
import sys

from PIL import Image, ImageDraw

NUM_TILES_IN_PRIMARY = 512
NUM_METATILES_IN_PRIMARY = 512
NUM_PALS_IN_PRIMARY = 6


def tileset_files(name):
    # tiles.png, palette files and metatiles.bin of a tileset, from its C declarations
    short = name.replace("gTileset_", "")
    graphics = open("src/data/tilesets/graphics.h").read() + open("src/graphics.c").read()  # General is in graphics.c
    tiles = re.search(r"gTilesetTiles_%s\[\] = \w+\(\"([^\"]+)\.png\"" % short, graphics).group(1) + ".png"
    palettes = re.search(r"gTilesetPalettes_%s\[\]\[16\] =\s*\{(.*?)\};" % short, graphics, re.S).group(1)
    palettes = re.findall(r"\"([^\"]+\.pal)\"", palettes)
    metatiles = re.search(r"gMetatiles_%s\[\] = INCBIN_U16\(\"([^\"]+)\"" % short, open("src/data/tilesets/metatiles.h").read()).group(1)
    return tiles, palettes, metatiles


def load_palette(path):
    lines = open(path).read().split("\n")[3:19]
    return [tuple(int(v) for v in line.split()[:3]) for line in lines]


def load_tileset(name):
    tiles_path, palette_paths, metatiles_path = tileset_files(name)
    image = Image.open(tiles_path)
    pixels = image.load()
    tiles = []
    for ty in range(image.height // 8):
        for tx in range(image.width // 8):
            tiles.append([[pixels[tx * 8 + x, ty * 8 + y] & 0xF for x in range(8)] for y in range(8)])
    data = open(metatiles_path, "rb").read()
    metatiles = [[int.from_bytes(data[i + 2 * j:i + 2 * j + 2], "little") for j in range(8)] for i in range(0, len(data), 16)]
    return tiles, [load_palette(p) for p in palette_paths], metatiles


def draw_metatile(px, ox, oy, metatile_id, primary, secondary):
    tileset = primary if metatile_id < NUM_METATILES_IN_PRIMARY else secondary
    index = metatile_id if metatile_id < NUM_METATILES_IN_PRIMARY else metatile_id - NUM_METATILES_IN_PRIMARY
    if index >= len(tileset[2]):
        return
    for layer in range(2):
        for t in range(4):
            entry = tileset[2][index][layer * 4 + t]
            tile_id, hflip, vflip, pal = entry & 0x3FF, entry >> 10 & 1, entry >> 11 & 1, entry >> 12
            tiles = primary[0] if tile_id < NUM_TILES_IN_PRIMARY else secondary[0]
            tile_id -= 0 if tile_id < NUM_TILES_IN_PRIMARY else NUM_TILES_IN_PRIMARY
            palette = (primary if pal < NUM_PALS_IN_PRIMARY else secondary)[1][pal]
            if tile_id >= len(tiles):
                continue
            for y in range(8):
                for x in range(8):
                    color = tiles[tile_id][7 - y if vflip else y][7 - x if hflip else x]
                    if color or layer == 0:
                        px[ox + (t % 2) * 8 + x, oy + (t // 2) * 8 + y] = palette[color]


def load_layout(map_name):
    # A map name (Route115) or a layout ID (LAYOUT_ROUTE130_MIRAGE_ISLAND)
    layout_id = map_name if map_name.startswith("LAYOUT_") else json.load(open(f"data/maps/{map_name}/map.json"))["layout"]
    return next(l for l in json.load(open("data/layouts/layouts.json"))["layouts"] if l.get("id") == layout_id)


def render(map_name, x0=0, y0=0, w=None, h=None, grid=False, collision=False):
    layout = load_layout(map_name)
    primary, secondary = load_tileset(layout["primary_tileset"]), load_tileset(layout["secondary_tileset"])
    width, height = layout["width"], layout["height"]
    blocks = open(layout["blockdata_filepath"], "rb").read()
    w, h = w or width - x0, h or height - y0
    out = Image.new("RGB", (w * 16, h * 16))
    px = out.load()
    for my in range(h):
        for mx in range(w):
            block = int.from_bytes(blocks[2 * ((y0 + my) * width + x0 + mx):][:2], "little")
            draw_metatile(px, mx * 16, my * 16, block & 0x3FF, primary, secondary)
            if collision and block >> 10 & 3:
                for y in range(0, 16, 2):
                    for x in range(y % 4, 16, 4):
                        px[mx * 16 + x, my * 16 + y] = (255, 0, 0)
    if grid:
        draw = ImageDraw.Draw(out)
        for gx in range(w):
            if (x0 + gx) % 5 == 0:
                draw.line([(gx * 16, 0), (gx * 16, h * 16)], fill=(255, 255, 0) if (x0 + gx) % 10 == 0 else (120, 120, 0))
                if (x0 + gx) % 10 == 0:
                    draw.text((gx * 16 + 2, 2), str(x0 + gx), fill=(255, 255, 0))
        for gy in range(h):
            if (y0 + gy) % 5 == 0:
                draw.line([(0, gy * 16), (w * 16, gy * 16)], fill=(255, 255, 0) if (y0 + gy) % 10 == 0 else (120, 120, 0))
                if (y0 + gy) % 10 == 0:
                    draw.text((2, gy * 16 + 2), str(y0 + gy), fill=(255, 255, 0))
    return out


if __name__ == "__main__":
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    numbers = [int(a) for a in args[2:6]]
    render(args[0], *numbers, grid="--grid" in flags, collision="--collision" in flags).save(args[1])
