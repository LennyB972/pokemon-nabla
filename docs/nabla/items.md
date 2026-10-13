# Objets ajoutés par Nabla

Référence de tous les objets que Nabla rend trouvables ou achetables. À tenir à jour à chaque ajout.

## Boutiques

| Où | Objets | Condition | Défini dans |
|---|---|---|---|
| Les 11 Boutiques Pokémon de Hoenn | Fil de Liaison | 3 badges | listes `data/maps/*_Mart/scripts.inc` |
| Les 11 Boutiques Pokémon de Hoenn | Bonbon Exp. S / M / L | 2 / 4 / 6 badges | idem |
| Centre Commercial de Nénucrique, 3ᵉ étage, vendeuse de gauche (vitamines) | Les 21 Aromates, Capsule Talent | — | `data/maps/LilycoveCity_DepartmentStore_3F/scripts.inc` |
| Centre Commercial de Nénucrique, 3ᵉ étage, vendeur du milieu | Objets d'évolution par échange | — | `data/scripts/nabla/evolution_items.inc` |

**Badges requis** : tableau `sShopItemBadgeRequirements` dans `src/shop_criteria.c`. Un objet qui y figure doit aussi avoir `.shopCriteriaFunc = ShopCriteriaByBadgeRequirement` dans `src/data/items.h`.

## Objets cachés

Ils sont dans les `bg_events` des `map.json` (type `hidden_item`). Leurs flags (`FLAG_NABLA_HIDDEN_ITEM_*`) sont dans `include/constants/flags.h` et doivent rester ≥ `FLAG_HIDDEN_ITEMS_START`.

| Map | Case (x, y) | Objet | Flag |
|---|---|---|---|
| Route102 | 34, 9 | `ITEM_EXP_CANDY_XS` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE102_EXP_CANDY_XS` |
| Route104 | 37, 6 | `ITEM_EXP_CANDY_XS` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE104_EXP_CANDY_XS` |
| Route116 | 41, 6 | `ITEM_EXP_CANDY_XS` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE116_EXP_CANDY_XS` |
| Route110 | 15, 15 | `ITEM_EXP_CANDY_S` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE110_EXP_CANDY_S` |
| Route117 | 15, 3 | `ITEM_EXP_CANDY_S` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE117_EXP_CANDY_S` |
| Route111 | 13, 112 | `ITEM_EXP_CANDY_S` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE111_EXP_CANDY_S` |
| Route113 | 41, 2 | `ITEM_EXP_CANDY_M` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE113_EXP_CANDY_M` |
| Route118 | 21, 2 | `ITEM_EXP_CANDY_M` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE118_EXP_CANDY_M` |
| Route119 | 23, 5 | `ITEM_EXP_CANDY_M` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE119_EXP_CANDY_M` |
| Route120 | 28, 2 | `ITEM_EXP_CANDY_L` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE120_EXP_CANDY_L` |
| Route121 | 17, 3 | `ITEM_EXP_CANDY_L` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE121_EXP_CANDY_L` |
| Route123 | 13, 3 | `ITEM_EXP_CANDY_L` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE123_EXP_CANDY_L` |
| VictoryRoad_B1F | 22, 4 | `ITEM_EXP_CANDY_XL` | `FLAG_NABLA_HIDDEN_ITEM_VICTORY_ROAD_B1F_EXP_CANDY_XL` |
| VictoryRoad_B2F | 32, 8 | `ITEM_EXP_CANDY_XL` | `FLAG_NABLA_HIDDEN_ITEM_VICTORY_ROAD_B2F_EXP_CANDY_XL` |
| PetalburgWoods | 12, 6 | `ITEM_ADAMANT_MINT` | `FLAG_NABLA_HIDDEN_ITEM_PETALBURG_WOODS_ADAMANT_MINT` |
| Route115 | 15, 5 | `ITEM_MODEST_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE115_MODEST_MINT` |
| Route114 | 4, 3 | `ITEM_JOLLY_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE114_JOLLY_MINT` |
| Route112 | 26, 6 | `ITEM_TIMID_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE112_TIMID_MINT` |
| Route118 | 9, 3 | `ITEM_BOLD_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE118_BOLD_MINT` |
| Route119 | 27, 9 | `ITEM_CALM_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE119_CALM_MINT` |
| Route120 | 25, 11 | `ITEM_IMPISH_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE120_IMPISH_MINT` |
| Route121 | 33, 5 | `ITEM_CAREFUL_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE121_CAREFUL_MINT` |
| MtChimney | 29, 6 | `ITEM_ABILITY_CAPSULE` | `FLAG_NABLA_HIDDEN_ITEM_MT_CHIMNEY_ABILITY_CAPSULE` |
| Route119 | 32, 36 | `ITEM_ABILITY_CAPSULE` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE119_ABILITY_CAPSULE` |
| VictoryRoad_1F | 34, 15 | `ITEM_ABILITY_CAPSULE` | `FLAG_NABLA_HIDDEN_ITEM_VICTORY_ROAD_1F_ABILITY_CAPSULE` |
| ArtisanCave_B1F | 4, 11 | `ITEM_ABILITY_PATCH` | `FLAG_NABLA_HIDDEN_ITEM_ARTISAN_CAVE_B1F_ABILITY_PATCH` |
| DesertUnderpass | 107, 3 | `ITEM_ABILITY_PATCH` | `FLAG_NABLA_HIDDEN_ITEM_DESERT_UNDERPASS_ABILITY_PATCH` |

## Ajouter ou déplacer un objet caché

1. Trouver une case : `python3 dev_scripts/nabla/hidden_item_spots.py NomDeLaMap 10` (cases accessibles à pied, sans CS, de préférence dans un coin ou un cul-de-sac).
2. Prendre un `FLAG_UNUSED_*` situé après `FLAG_HIDDEN_ITEMS_START` et le renommer `FLAG_NABLA_HIDDEN_ITEM_<MAP>_<OBJET>`.
3. Ajouter l'objet dans les `bg_events` du `map.json` (ou via Porymap), puis mettre à jour ce tableau.
