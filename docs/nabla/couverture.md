# Couverture des Pokémon

Généré par `python3 dev_scripts/nabla/coverage.py`. Une espèce (formes cosmétiques comprises) est obtenable si on
peut la capturer ou la recevoir, la faire éclore ou y faire évoluer une espèce obtenable avec un objet trouvable.

- **Espèces obtenables** : 984 / 984 hors légendaires et fabuleux.
- **Légendaires et fabuleux** : 8 / 97 (les autres : phase 7).

## Espèces manquantes (hors légendaires)

Aucune.

## Légendaires et fabuleux obtenables

Groudon, Kyogre, Latias, Latios, Rayquaza, Regice, Regirock, Registeel

## Évolutions à vérifier en jeu

Conditions que le script ne peut pas vérifier (combat, pas, météo, lieu, capacité hors niveau).

- Basculin_White_Striped → Basculegion_M : IF_RECOIL_DAMAGE_GE 294
- Bisharp → Kingambit : IF_DEFEAT_X_WITH_ITEMS SPECIES_BISHARP ITEM_LEADERS_CREST 3
- Bramblin → Brambleghast : IF_MIN_OVERWORLD_STEPS 1000
- Charjabug → Vikavolt : IF_IN_MAPSEC MAPSEC_NEW_MAUVILLE
- Crabrawler → Crabominable : IF_IN_MAP MAP_SHOAL_CAVE_LOW_TIDE_ICE_ROOM
- Eevee → Glaceon : IF_IN_MAP MAP_SHOAL_CAVE_LOW_TIDE_ICE_ROOM
- Eevee → Leafeon : IF_IN_MAP MAP_PETALBURG_WOODS
- Farfetchd_Galar → Sirfetchd : IF_CRITICAL_HITS_GE 3, fin de combat
- Feebas → Milotic : IF_MIN_BEAUTY 170
- Magneton → Magnezone : IF_IN_MAPSEC MAPSEC_NEW_MAUVILLE
- Milcery → Alcremie_Strawberry_Vanilla_Cream : tourner sur soi-même
- Nosepass → Probopass : IF_IN_MAPSEC MAPSEC_NEW_MAUVILLE
- Pawmo → Pawmot : IF_MIN_OVERWORLD_STEPS 1000
- Rellor → Rabsca : IF_MIN_OVERWORLD_STEPS 1000
- Sliggoo → Goodra : IF_WEATHER WEATHER_RAIN
- Sliggoo_Hisui → Goodra_Hisui : IF_WEATHER WEATHER_RAIN
- Yamask_Galar → Runerigus : IF_CURRENT_DAMAGE_GE 49, script EVO_TRIGGER_TABLET_CURSE

## Objets d'évolution

| Objet | Où |
|---|---|
| Auspicious Armor | boutique ou script (evolution_items.inc) |
| Berry Sweet | boutique ou script (evolution_items.inc) |
| Black Augurite | boutique ou script (evolution_items.inc) |
| Clover Sweet | boutique ou script (evolution_items.inc) |
| Cracked Pot | boutique ou script (evolution_items.inc) |
| Dawn Stone | boutique ou script (evolution_items.inc) |
| Deep Sea Scale | boutique ou script (SlateportCity_Harbor) |
| Deep Sea Tooth | boutique ou script (SlateportCity_Harbor) |
| Dragon Scale | boutique ou script (evolution_items.inc) |
| Dubious Disc | boutique ou script (evolution_items.inc) |
| Dusk Stone | boutique ou script (evolution_items.inc) |
| Electirizer | boutique ou script (evolution_items.inc) |
| Fire Stone | boutique ou script (evolution_items.inc) |
| Flower Sweet | boutique ou script (evolution_items.inc) |
| Galarica Cuff | boutique ou script (evolution_items.inc) |
| Galarica Wreath | boutique ou script (evolution_items.inc) |
| Gimmighoul Coin | boutique ou script (evolution_items.inc) |
| Ice Stone | boutique ou script (evolution_items.inc) |
| Kings Rock | boutique ou script (MossdeepCity) |
| Leaf Stone | boutique ou script (evolution_items.inc) |
| Linking Cord | boutique ou script (evolution_items.inc) |
| Love Sweet | boutique ou script (evolution_items.inc) |
| Magmarizer | boutique ou script (evolution_items.inc) |
| Malicious Armor | boutique ou script (evolution_items.inc) |
| Metal Alloy | boutique ou script (evolution_items.inc) |
| Metal Coat | boutique ou script (evolution_items.inc) |
| Moon Stone | boutique ou script (evolution_items.inc) |
| Oval Stone | tenu par Chansey sauvage |
| Peat Block | boutique ou script (evolution_items.inc) |
| Poke Ball | boutique ou script (LilycoveCity_DepartmentStore_2F) |
| Prism Scale | boutique ou script (evolution_items.inc) |
| Protector | boutique ou script (evolution_items.inc) |
| Razor Claw | tenu par Jangmo_O sauvage |
| Razor Fang | tenu par Bruxish sauvage |
| Reaper Cloth | boutique ou script (evolution_items.inc) |
| Ribbon Sweet | boutique ou script (evolution_items.inc) |
| Sachet | boutique ou script (evolution_items.inc) |
| Shiny Stone | boutique ou script (evolution_items.inc) |
| Star Sweet | boutique ou script (evolution_items.inc) |
| Strawberry Sweet | boutique ou script (evolution_items.inc) |
| Sun Stone | boutique ou script (MossdeepCity_SpaceCenter_1F) |
| Sweet Apple | boutique ou script (evolution_items.inc) |
| Syrupy Apple | boutique ou script (evolution_items.inc) |
| Tart Apple | boutique ou script (evolution_items.inc) |
| Thunder Stone | boutique ou script (evolution_items.inc) |
| Unremarkable Teacup | boutique ou script (evolution_items.inc) |
| Upgrade | boutique ou script (evolution_items.inc) |
| Water Stone | boutique ou script (evolution_items.inc) |
| Whipped Dream | boutique ou script (evolution_items.inc) |
