#!/usr/bin/env python3
"""Generates the region tables of Nabla's Safari Zone in src/data/wild_encounters.json.

Each Safari Zone area keeps its original table, followed by one table per region in the
order of SAFARI_REGIONS (the game picks the table with VAR_NABLA_SAFARI_REGION).
A region contains every non-legendary Pokémon that starts a line in that region:
babies added in later generations are skipped (Pikachu is Kanto, Pichu is Johto) and so are
cross-generation evolutions (Magmortar comes from Magmar). Regional forms belong to the
region of their form, and lines with a regional evolution also live in that region (Cubone in
Alola: the game evolves Pokémon into their regional form in their region's Safari Zone).
Non-Water Pokémon of the Water 1/2 egg groups (Dratini) live both on land and in the water.
The game sets the level and evolves the Pokémon, so tables only list species.

Usage (from the repo root):
  python3 dev_scripts/nabla/safari_tables.py Kanto      (re)generate one region
  python3 dev_scripts/nabla/safari_tables.py --doc      rewrite docs/nabla/safari.md
"""
import glob
import json
import re
import sys

ENCOUNTERS = "src/data/wild_encounters.json"
DOC = "docs/nabla/safari.md"

# Index in this list + 1 = value of VAR_NABLA_SAFARI_REGION (see include/constants/nabla.h)
SAFARI_REGIONS = ["Kanto", "Johto", "Sinnoh", "Unova", "Kalos", "Alola", "Galar", "Paldea",
                  "Starters", "Paradox", "UltraBeasts"]
NATIONAL_DEX_RANGES = {"Kanto": (1, 151), "Johto": (152, 251), "Hoenn": (252, 386), "Sinnoh": (387, 493),
                       "Unova": (494, 649), "Kalos": (650, 721), "Alola": (722, 809), "Galar": (810, 905),
                       "Paldea": (906, 1025)}
FORM_REGIONS = {"_ALOLA": "Alola", "_GALAR": "Galar", "_HISUI": "Galar", "_PALDEA": "Paldea"}
NOT_REGIONAL_FORMS = ["PIKACHU_ALOLA"]  # Pikachu in an Alola Cap
STARTERS = ("BULBASAUR CHARMANDER SQUIRTLE CHIKORITA CYNDAQUIL TOTODILE TREECKO TORCHIC MUDKIP TURTWIG "
            "CHIMCHAR PIPLUP SNIVY TEPIG OSHAWOTT CHESPIN FENNEKIN FROAKIE ROWLET LITTEN POPPLIO GROOKEY "
            "SCORBUNNY SOBBLE SPRIGATITO FUECOCO QUAXLY").split()

# Safari Zone areas, in the order shown in the doc. Northeast and Southeast open after the League.
AREAS = {
    "MAP_SAFARI_ZONE_SOUTH": ("South", ["NORMAL", "BUG", "GRASS", "FLYING"]),
    "MAP_SAFARI_ZONE_SOUTHWEST": ("Southwest", ["FAIRY", "ELECTRIC", "POISON", "GRASS"]),
    "MAP_SAFARI_ZONE_NORTH": ("North", ["ROCK", "GROUND", "FIGHTING", "FIRE", "STEEL"]),
    "MAP_SAFARI_ZONE_NORTHWEST": ("Northwest", ["PSYCHIC", "GHOST", "DARK", "DRAGON", "ICE"]),
    "MAP_SAFARI_ZONE_NORTHEAST": ("Northeast", []),
    "MAP_SAFARI_ZONE_SOUTHEAST": ("Southeast", []),
}
SLOTS = {"land_mons": 12, "water_mons": 5, "rock_smash_mons": 5, "fishing_mons": 10}
MIN_SPECIES = {"land_mons": 6, "water_mons": 3, "rock_smash_mons": 2, "fishing_mons": 3}


def number(text):
    # Stats can be "P_UPDATED_STATS >= GEN_6 ? 70 : 60": keep the updated value
    values = re.findall(r"\d+", text.split("?", 1)[1] if "?" in text else text)
    return int(values[0]) if values else 0


def expand_calls(text, functions):
    # Expands the calls of function-like macros (UNOWN_MISC_INFO(A, ...))
    call = re.compile(r"\b(%s)\(" % "|".join(functions))
    out, i = [], 0
    while (m := call.search(text, i)):
        out.append(text[i:m.start()])
        args, start, depth, j = [], m.end(), 1, m.end()
        while depth:
            depth += text[j] in "([{"
            depth -= text[j] in ")]}"
            if depth == 0 or (depth == 1 and text[j] == ","):
                args.append(text[start:j].strip())
                start = j + 1
            j += 1
        params, value = functions[m.group(1)]
        out.append(re.sub(r"#*\b\w+\b", lambda w: args[params.index(w.group(0).lstrip("#"))] if w.group(0).lstrip("#") in params else w.group(0), value).replace("##", ""))
        i = j
    return "".join(out + [text[i:]])


def species_files():
    # Some species are built by macros (Unown, Vivillon...) and some types and stats are macros
    # (JIGGLYPUFF_FAMILY_TYPES): expand them, keeping the updated value, which is defined first
    texts = [open(path).read().replace("\\\n", " ") for path in sorted(glob.glob("src/data/pokemon/species_info/gen_*_families.h"))]
    macros, functions = {}, {}
    for text in texts:
        for name, params, value in re.findall(r"^\s*#define (\w+)(\([^)]*\))?[ \t]+(.+?)\s*$", text, re.M):
            if params:
                functions.setdefault(name, ([p.strip() for p in params[1:-1].split(",")], re.sub(r"\s*##\s*", "##", value)))
            else:
                macros.setdefault(name, value)
    for text in texts:
        text = expand_calls(expand_calls(text, functions), functions)
        for _ in range(2):
            text = re.sub(r"\b[A-Z]\w+\b", lambda w: macros.get(w.group(0), w.group(0)), text)
        yield text


def load_species():
    order = re.findall(r"^\s+NATIONAL_DEX_(\w+),", open("include/constants/pokedex.h").read(), re.M)
    national = {name: i for i, name in enumerate(order)}
    species = {}
    for text in species_files():
        entries = re.findall(r"\n    \[SPECIES_(\w+)\] =\n    \{(.*?)\n    \},", text, re.S)
        entries += re.findall(r"\n    \[SPECIES_(\w+)\]\s*=\s*\{([^\n]*)\},?[ \t]*(?=\n)", text)
        for name, body in entries:
            dex = re.search(r"\.natDexNum = NATIONAL_DEX_(\w+)", body)
            # Types can be "P_UPDATED_TYPES >= GEN_6 ? TYPE_FAIRY : TYPE_NORMAL": keep the updated one
            types = re.search(r"\.types = (MON_TYPES\([^)]*\)|\{[^}]*\})", body)
            types = re.sub(r":\s*TYPE_\w+", "", types.group(1)) if types else ""
            stats = sum(number(s) for s in re.findall(r"\.base(?:HP|Attack|Defense|Speed|SpAttack|SpDefense)\s*= ([^,\n]+)", body))
            species[name] = dict(
                dex=national.get(dex.group(1)) if dex else None,
                types=list(dict.fromkeys(re.findall(r"\bTYPE_(\w+)", types))),
                bst=stats,
                legend=re.search(r"\.is(Legendary|SubLegendary|RestrictedLegendary|Mythical) = TRUE", body) is not None,
                ultra=".isUltraBeast = TRUE" in body,
                paradox=".isParadox = TRUE" in body,
                evos=re.findall(r"\{EVO_\w+, [^,]+, SPECIES_(\w+)", body),
                water_eggs=re.search(r"\.eggGroups = MON_EGG_GROUPS\([^)]*EGG_GROUP_WATER_[12]", body) is not None,
                regional_evos=[FORM_REGIONS["_" + r] for r in re.findall(r"\{IF_REGION, REGION_(\w+)\}", body)],
            )
    for data in species.values():
        data["pre"] = None
    for name, data in species.items():
        for target in data["evos"]:
            if target in species:
                species[target]["pre"] = name
    return species


def region_of(name, data):
    if name in NOT_REGIONAL_FORMS:
        return None
    for suffix, region in FORM_REGIONS.items():
        if name.endswith(suffix) or suffix + "_" in name:
            return region
    for region, (first, last) in NATIONAL_DEX_RANGES.items():
        if data["dex"] is not None and first <= data["dex"] <= last:
            return region
    return None


def line_start(species, name):
    # Babies added in later generations don't start the line (Pikachu, not Pichu)
    while species[name]["pre"] and species[species[name]["pre"]]["dex"] <= species[name]["dex"]:
        name = species[name]["pre"]
    return name


def final_bst(species, name, seen=()):
    data = species[name]
    return max([data["bst"]] + [final_bst(species, t, seen + (name,)) for t in data["evos"] if t in species and t not in seen])


def region_species(species, region):
    def is_base_entry(name, data):
        # Only the main entry of a species (cosmetic forms share its national dex number)
        same = [n for n, d in species.items() if d["dex"] == data["dex"] and region_of(n, d) == region_of(name, data)]
        return same and same[0] == name

    picked = []
    for name, data in species.items():
        if data["dex"] is None or "_MEGA" in name or "_GMAX" in name or not is_base_entry(name, data):
            continue
        pre = data["pre"]
        starts_line = pre is None or species[pre]["dex"] > data["dex"]  # babies come from later generations
        if region == "Starters":
            ok = name in STARTERS
        elif region == "Paradox":
            ok = data["paradox"]
        elif region == "UltraBeasts":
            ok = data["ultra"] and starts_line
        else:
            ok = (region_of(name, data) == region and starts_line and name not in STARTERS
                  and not data["legend"] and not data["ultra"] and not data["paradox"])
        if ok:
            picked.append(name)
        if region in data["regional_evos"]:
            start = line_start(species, name)
            if start not in STARTERS and not species[start]["legend"] and start not in picked:
                picked.append(start)
    return sorted(set(picked), key=lambda n: (final_bst(species, n), n))


def fill(names, count):
    # Slots are ordered from most to least common: the weakest Pokémon take the common slots
    return [names[i % len(names)] for i in range(count)] if names else []


def build_region(species, region, area_types):
    names = region_species(species, region)
    water = [n for n in names if "WATER" in species[n]["types"] or species[n]["water_eggs"]]
    rock = [n for n in names if species[n]["types"][:1] == ["ROCK"]]
    land = [n for n in names if "WATER" not in species[n]["types"]]
    areas = {area: {"land_mons": [], "water_mons": [], "rock_smash_mons": [], "fishing_mons": []} for area in AREAS}

    # Land: by type theme, the post-League areas take the Pokémon left when the themed areas are full
    pre_league = [a for a in AREAS if AREAS[a][1]]
    themed = {n: [a for t in species[n]["types"] for a in pre_league if t in AREAS[a][1] and "land_mons" in area_types[a]] for n in land}
    for n in land:
        candidates = [a for a in themed[n] if len(areas[a]["land_mons"]) < SLOTS["land_mons"]]
        if not candidates:
            candidates = sorted((a for a in AREAS if a not in pre_league and "land_mons" in area_types[a]), key=lambda a: len(areas[a]["land_mons"]))
        areas[candidates[0]]["land_mons"].append(n)
    # Water Pokémon alternate between surfing and fishing, Rock Pokémon also hide under rocks
    surf_areas = [a for a in AREAS if "water_mons" in area_types[a]]
    fish_areas = [a for a in AREAS if "fishing_mons" in area_types[a]]
    for i, n in enumerate(water):
        kind, pool = ("water_mons", surf_areas) if i % 2 == 0 else ("fishing_mons", fish_areas)
        target = min(pool, key=lambda a: len(areas[a][kind]))
        areas[target][kind].append(n)
    rock_areas = [a for a in AREAS if "rock_smash_mons" in area_types[a]]
    for i, n in enumerate(rock):
        areas[rock_areas[i % len(rock_areas)]]["rock_smash_mons"].append(n)
    # Tables with too few Pokémon (small regions) borrow the region's least used ones: weak ones
    # of the area's types before the League, the strongest after
    pools = {"land_mons": land, "water_mons": water, "fishing_mons": water, "rock_smash_mons": rock or land}
    for a in AREAS:
        for kind in area_types[a]:
            def priority(n):
                uses = sum(n in table for area in areas.values() for table in area.values())
                if a in pre_league:
                    return (uses, a not in themed.get(n, []), final_bst(species, n), n)
                return (uses, -final_bst(species, n), n)
            while len(areas[a][kind]) < MIN_SPECIES[kind]:
                options = [n for n in pools[kind] or names if n not in areas[a][kind]]
                if not options:
                    break
                areas[a][kind].append(min(options, key=priority))
    for a in AREAS:
        for kind in areas[a]:
            areas[a][kind].sort(key=lambda n: (final_bst(species, n), n))
    return names, areas


def make_entry(map_id, region, kinds, vanilla):
    entry = {"map": map_id, "base_label": f"gSafariZone_{AREAS[map_id][0]}_{region}"}
    for kind, names in kinds.items():
        if kind not in vanilla:
            continue
        entry[kind] = {"encounter_rate": vanilla[kind]["encounter_rate"],
                       "mons": [{"min_level": 25, "max_level": 30, "species": f"SPECIES_{n}"} for n in fill(names, SLOTS[kind])]}
    return entry


def generate(region):
    species = load_species()
    data = json.load(open(ENCOUNTERS))
    encounters = data["wild_encounter_groups"][0]["encounters"]
    vanilla = {e["map"]: e for e in encounters if e["map"] in AREAS and not re.search(r"_(Kanto|Johto|Sinnoh|Unova|Kalos|Alola|Galar|Paldea|Starters|Paradox|UltraBeasts)$", e["base_label"])}
    area_types = {a: [k for k in SLOTS if k in vanilla[a]] for a in AREAS}
    names, areas = build_region(species, region, area_types)
    index = SAFARI_REGIONS.index(region)
    for map_id in AREAS:
        # Region tables follow the original table in SAFARI_REGIONS order
        start = encounters.index(vanilla[map_id])
        block = [e for e in encounters[start + 1:start + 1 + len(SAFARI_REGIONS)] if e["map"] == map_id]
        existing = {e["base_label"].rsplit("_", 1)[1]: e for e in block}
        assert len(existing) >= index, f"{region} needs the regions before it in {map_id}"
        existing[region] = make_entry(map_id, region, areas[map_id], vanilla[map_id])
        ordered = [existing[r] for r in SAFARI_REGIONS if r in existing]
        encounters[start + 1:start + 1 + len(block)] = ordered
    open(ENCOUNTERS, "w").write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"{region}: {len(names)} Pokémon")


def write_doc():
    data = json.load(open(ENCOUNTERS))
    rates = {f["type"]: f["encounter_rates"] for f in data["wild_encounter_groups"][0]["fields"]}
    labels = {"land_mons": "Herbes", "water_mons": "Surf", "rock_smash_mons": "Éclate-Roc", "fishing_mons": "Pêche"}
    lines = ["# Safari par région", "",
             "Généré par `python3 dev_scripts/nabla/safari_tables.py --doc`. Chaque Pokémon apparaît au niveau des badges",
             "du joueur (au niveau 5 dans la zone Starters) et évolue selon son niveau. Les zones Nord-Est et Sud-Est",
             "s'ouvrent après la Ligue, comme les zones spéciales (Starters, Paradox, UltraBeasts).",
             "Dans le Safari d'une région, les évolutions régionales donnent la forme de cette région (Pikachu → Raichu",
             "d'Alola en Alola, Feurisson → Typhlosion de Hisui en Galar & Hisui).", ""]
    encounters = data["wild_encounter_groups"][0]["encounters"]
    for region in SAFARI_REGIONS:
        tables = [e for e in encounters if e["base_label"].endswith("_" + region) and e["map"] in AREAS]
        if not tables:
            continue
        lines += [f"## {region}", ""]
        for e in tables:
            lines.append(f"**{AREAS[e['map']][0]}**")
            for kind, label in labels.items():
                if kind not in e:
                    continue
                total = {}
                for slot, mon in enumerate(e[kind]["mons"]):
                    total[mon["species"][8:]] = total.get(mon["species"][8:], 0) + rates[kind][slot]
                per = 100 if kind != "fishing_mons" else 300
                lines.append(f"- {label} : " + ", ".join(f"{n.title()} {round(v * 100 / per)} %" for n, v in sorted(total.items(), key=lambda x: -x[1])))
            lines.append("")
    open(DOC, "w").write("\n".join(lines))


if __name__ == "__main__":
    if sys.argv[1] == "--doc":
        write_doc()
    else:
        generate(sys.argv[1])
        write_doc()
