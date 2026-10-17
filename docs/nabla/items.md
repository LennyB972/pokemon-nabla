# Objets ajoutés par Nabla

Référence de tous les objets que Nabla rend trouvables ou achetables. À tenir à jour à chaque ajout.

## Boutiques

**Boutiques Pokémon** : les 11 Boutiques de Hoenn proposent **la même liste** (`Nabla_Pokemart_Items`, `data/scripts/nabla/pokemart.inc`). Un article reste caché tant que le joueur n'a pas le nombre de badges requis, comme dans les jeux récents. Les paliers reprennent le moment où l'article apparaissait dans Émeraude :

| Badges | Articles débloqués |
|---|---|
| 0 | Poké Ball (après avoir reçu le Pokédex), Potion, Super Potion, Antidote, Anti-Para, Réveil, Corde Sortie, Repousse, Attaque +, Défense +, Vitesse +, Lettre Orange |
| 1 | Chrono Ball, Bis Ball |
| 2 | Super Ball, Précision +, Muscle +, Défense Spéciale, Bonbon Exp. S, Lettre Port |
| 3 | Faiblo Ball, Rappel, Anti-Brûle, Antigel, Queue Skitty, Super Repousse, Spécial +, Fil de Liaison |
| 4 | Bonbon Exp. M |
| 5 | Hyper Ball, Hyper Potion, Lettre Bois |
| 6 | Filet Ball, Scuba Ball, Total Soin, Max Repousse, Bonbon Exp. L |
| 7 | Potion Max, Lettre Ombre |

- Modifier un palier : tableau `sShopItemRequirements` dans `src/shop_criteria.c` (badges, et un flag optionnel). Il s'applique à toutes les boutiques normales.
- Ajouter un article : l'ajouter à `Nabla_Pokemart_Items`, et au tableau s'il doit être débloqué plus tard.

**Autres vendeurs** :

| Où | Objets | Défini dans |
|---|---|---|
| Centre Commercial de Nénucrique, 3ᵉ étage, vendeuse de gauche (vitamines) | Vitamines, les 21 Aromates, Capsule Talent | `data/maps/LilycoveCity_DepartmentStore_3F/scripts.inc` |
| Centre Commercial de Nénucrique, 3ᵉ étage, vendeur du milieu | Objets d'évolution par échange | `data/scripts/nabla/evolution_items.inc` |
| Centre Commercial de Nénucrique, 4ᵉ étage, vendeur du milieu | 65 Méga-Gemmes à 5 000 ₽ (toutes sauf celles de Hoenn trouvables au sol et celles des légendaires) | `data/scripts/nabla/mega_stones.inc` |

## Objets cachés

Ils sont dans les `bg_events` des `map.json` (type `hidden_item`). Leurs flags (`FLAG_NABLA_HIDDEN_ITEM_*`) sont dans `include/constants/flags.h` et doivent rester ≥ `FLAG_HIDDEN_ITEMS_START`.

| Map | Case (x, y) | Objet | Flag |
|---|---|---|---|
| Route102 | 34, 9 | `ITEM_EXP_CANDY_XS` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE102_EXP_CANDY_XS` |
| Route104 | 37, 6 | `ITEM_EXP_CANDY_XS` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE104_EXP_CANDY_XS` |
| Route116 | 41, 6 | `ITEM_EXP_CANDY_XS` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE116_EXP_CANDY_XS` |
| Route110 | 4, 11 | `ITEM_EXP_CANDY_S` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE110_EXP_CANDY_S` |
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
| Route118 | 38, 5 | `ITEM_BOLD_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE118_BOLD_MINT` |
| Route119 | 27, 9 | `ITEM_CALM_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE119_CALM_MINT` |
| Route120 | 25, 11 | `ITEM_IMPISH_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE120_IMPISH_MINT` |
| Route121 | 33, 5 | `ITEM_CAREFUL_MINT` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE121_CAREFUL_MINT` |
| MtChimney | 29, 6 | `ITEM_ABILITY_CAPSULE` | `FLAG_NABLA_HIDDEN_ITEM_MT_CHIMNEY_ABILITY_CAPSULE` |
| Route119 | 32, 36 | `ITEM_ABILITY_CAPSULE` | `FLAG_NABLA_HIDDEN_ITEM_ROUTE119_ABILITY_CAPSULE` |
| VictoryRoad_1F | 34, 15 | `ITEM_ABILITY_CAPSULE` | `FLAG_NABLA_HIDDEN_ITEM_VICTORY_ROAD_1F_ABILITY_CAPSULE` |
| ArtisanCave_B1F | 4, 11 | `ITEM_ABILITY_PATCH` | `FLAG_NABLA_HIDDEN_ITEM_ARTISAN_CAVE_B1F_ABILITY_PATCH` |
| DesertUnderpass | 107, 3 | `ITEM_ABILITY_PATCH` | `FLAG_NABLA_HIDDEN_ITEM_DESERT_UNDERPASS_ABILITY_PATCH` |

## Méga-Gemmes

- **Pokémon sauvages** : chaque Pokémon non légendaire dont la lignée a une Méga-Évolution porte la Méga-Gemme de sa lignée en **objet rare** (5 %, 20 % avec Œil Composé / Super Chance en tête). Dracaufeu et Raichu : la gemme X ; Absol, Carchacrok, Lucario : la gemme de base (pas la Z) ; Tarsal/Kirlia : Gardevoirite ; Stalgamin : Oniglalite. L'ancien objet rare est passé en objet commun quand la case était libre (46 espèces), sinon il a été retiré : Morceau d'Étoile de Stari/Staross et Baie Sitrus de Nanméouïe (leur case commune était déjà prise par Poussière Étoile et Baie Oran). Données : `.itemRare` / `.itemCommon` dans `src/data/pokemon/species_info/gen_*_families.h`.
- **Route 120** : Steven donne la Méga-Gemme du starter avec le Scope Devon (`Nabla_Route120_EventScript_GiveStarterMegaStone`).
- **Latiosite** : donné avec Latios (événement de l'Île du Sud). Les gemmes des légendaires (Mewtwo X/Y, Latias, Diancie, Zygarde, Heatran, Darkrai, Zeraora, Magearna) seront traitées avec les légendaires.
- **Au sol, visibles** (Poké Balls, flags `FLAG_NABLA_ITEM_*`, objets ajoutés en fin de `object_events`) :

| Map | Case (x, y) | Objet | Flag |
|---|---|---|---|
| Route102 | 11, 14 | `ITEM_GARDEVOIRITE` | `FLAG_NABLA_ITEM_ROUTE102_GARDEVOIRITE` |
| Route102 | 8, 2 | `ITEM_GALLADITE` | `FLAG_NABLA_ITEM_ROUTE102_GALLADITE` |
| GraniteCave_1F | 38, 9 | `ITEM_AGGRONITE` | `FLAG_NABLA_ITEM_GRANITE_CAVE_1F_AGGRONITE` |
| GraniteCave_B1F | 28, 11 | `ITEM_MAWILITE` | `FLAG_NABLA_ITEM_GRANITE_CAVE_B1F_MAWILITE` |
| GraniteCave_B2F | 11, 4 | `ITEM_SABLENITE` | `FLAG_NABLA_ITEM_GRANITE_CAVE_B2F_SABLENITE` |
| Route110 | 34, 39 | `ITEM_MANECTITE` | `FLAG_NABLA_ITEM_ROUTE110_MANECTITE` |
| Route114 | 7, 5 | `ITEM_ALTARIANITE` | `FLAG_NABLA_ITEM_ROUTE114_ALTARIANITE` |
| FieryPath | 19, 2 | `ITEM_CAMERUPTITE` | `FLAG_NABLA_ITEM_FIERY_PATH_CAMERUPTITE` |
| Route118 | 28, 6 | `ITEM_SHARPEDONITE` | `FLAG_NABLA_ITEM_ROUTE118_SHARPEDONITE` |
| Route120 | 28, 18 | `ITEM_ABSOLITE` | `FLAG_NABLA_ITEM_ROUTE120_ABSOLITE` |
| MtPyre_Exterior | 14, 7 | `ITEM_MEDICHAMITE` | `FLAG_NABLA_ITEM_MT_PYRE_EXTERIOR_MEDICHAMITE` |
| MtPyre_2F | 6, 3 | `ITEM_BANETTITE` | `FLAG_NABLA_ITEM_MT_PYRE_2F_BANETTITE` |
| MtPyre_Summit | 22, 2 | `ITEM_CHIMECHITE` | `FLAG_NABLA_ITEM_MT_PYRE_SUMMIT_CHIMECHITE` |
| ShoalCave_LowTideIceRoom | 13, 2 | `ITEM_GLALITITE` | `FLAG_NABLA_ITEM_SHOAL_CAVE_LOW_TIDE_ICE_ROOM_GLALITITE` |
| ShoalCave_LowTideLowerRoom | 24, 3 | `ITEM_FROSLASSITE` | `FLAG_NABLA_ITEM_SHOAL_CAVE_LOW_TIDE_LOWER_ROOM_FROSLASSITE` |
| MossdeepCity_StevensHouse | 4, 2 | `ITEM_METAGROSSITE` | `FLAG_NABLA_ITEM_MOSSDEEP_CITY_STEVENS_HOUSE_METAGROSSITE` |
| MeteorFalls_B1F_2R | 3, 14 | `ITEM_SALAMENCITE` | `FLAG_NABLA_ITEM_METEOR_FALLS_B1F_2R_SALAMENCITE` |

## Ajouter ou déplacer un objet caché

1. Trouver une case : `python3 dev_scripts/nabla/hidden_item_spots.py NomDeLaMap 10` (cases accessibles à pied, sans CS, de préférence dans un coin ou un cul-de-sac).
2. Prendre un `FLAG_UNUSED_*` situé après `FLAG_HIDDEN_ITEMS_START` et le renommer `FLAG_NABLA_HIDDEN_ITEM_<MAP>_<OBJET>`.
3. Ajouter l'objet dans les `bg_events` du `map.json` (ou via Porymap), puis mettre à jour ce tableau.
