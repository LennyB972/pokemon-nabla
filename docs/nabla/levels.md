# Niveaux des dresseurs ordinaires et des Pokémon sauvages (étape 4.3)

Généré par `python3 dev_scripts/nabla/scale_levels.py` : ne pas modifier à la main. Pour rééquilibrer une étape de l'aventure, changer son facteur (`PARTS`) ou la place d'une map (`MAP_PARTS`) dans le script et le relancer : il repart toujours des niveaux d'origine.

## Facteurs

Un niveau est multiplié par le facteur de l'étape où on le rencontre (arrondi). Facteur = level cap Nabla ÷ niveau du Pokémon le plus fort du Champion d'origine.

| Étape | Champion d'origine → cap | Facteur |
|---|---|---|
| Avant le 1er badge | 15 → 16 | ×1.07 |
| 1er → 2e badge | 19 → 20 | ×1.05 |
| 2e → 3e badge | 24 → 27 | ×1.12 |
| 3e → 4e badge | 29 → 34 | ×1.17 |
| 4e → 5e badge | 31 → 35 | ×1.13 |
| 5e → 6e badge | 33 → 41 | ×1.24 |
| 6e → 7e badge | 42 → 51 | ×1.21 |
| 7e → 8e badge | 46 → 59 | ×1.28 |
| Route Victoire | Conseil 4 : Damien 46 → 66 | ×1.40 |

- Un dresseur prend l'étape de sa map, ou celle de son niveau d'origine si elle est plus tardive (dresseurs en Surf, revanches).
- Pokémon sauvages : au plus tôt l'étape où on les rencontre (Surf : 5ᵉ badge, Éclate-Roc : 3ᵉ, Canne : 1er, Super Canne : 5ᵉ, Méga Canne : 6ᵉ).
- Évolutions : un Pokémon de dresseur évolue quand le relèvement lui fait atteindre son niveau d'évolution ; les évolutions par échange, objet, bonheur… se font au niveau 40. Les Pokémon sauvages évoluent dans le jeu, selon leur niveau (même règle).
- Non touchés : dresseurs de l'étape 4.2, revanches des Champions, après la Ligue, Safari (niveaux selon les badges), zones Nabla (réglées avec les zones voisines), légendaires et cadeaux.

## Étape de chaque map

| Étape | Maps |
|---|---|
| Avant le 1er badge | LittlerootTown, OldaleTown, Route101, Route102, Route103, Route104, PetalburgWoods, PetalburgCity, RustboroCity, Route116 |
| 1er → 2e badge | RusturfTunnel, DewfordTown, GraniteCave, Route106 |
| 2e → 3e badge | Route109, SlateportCity, Route110, MauvilleCity, Route117, Route111 |
| 3e → 4e badge | Route112, Route113, Route114, Route115, FallarborTown, MeteorFalls_1F_1R, MtChimney, JaggedPass, LavaridgeTown, FieryPath |
| 4e → 5e badge | PetalburgCity_Gym, MirageTower |
| 5e → 6e badge | Route105, Route107, Route108, AbandonedShip, Route118, Route119, Route120, ScorchedSlab, NewMauville, FortreeCity |
| 6e → 7e badge | Route121, Route122, MtPyre, Route123, LilycoveCity, MagmaHideout, AquaHideout, Route124, Route125, MossdeepCity, Route126, Route127, Route128, ShoalCave |
| 7e → 8e badge | MossdeepCity_SpaceCenter, SeafloorCavern, Route129, Route130, Route131, Route132, Route133, Route134, PacifidlogTown, SootopolisCity, CaveOfOrigin, SkyPillar, Underwater |
| Route Victoire | VictoryRoad, EverGrandeCity, MeteorFalls_1F_2R, MeteorFalls_B1F |
| Non touchées | SSTidal, MeteorFalls_StevensCave, BattleFrontier, TrainerHill, ArtisanCave, DesertUnderpass, TerraCave, MarineCave, AlteringCave, SafariZone, NavelRock, BirthIsland, FarawayIsland, SouthernIsland, Nabla |

## Pokémon fixes

| Script | Pokémon | Avant | Après |
|---|---|---|---|
| `data/maps/NewMauville_Inside/scripts.inc` | Voltorb | 25 | 31 |
| `data/maps/AquaHideout_B1F/scripts.inc` | Electrode | 30 | 36 |
| `data/maps/Route120/scripts.inc` | Kecleon | 30 | 37 |
| `data/scripts/kecleon.inc` | Kecleon | 30 | 37 |

## Évolutions des Pokémon de dresseurs

| Dresseur | Avant | Après |
|---|---|---|
| `TRAINER_SAWYER_1` | Geodude 21 | Graveler 25 |
| `TRAINER_GRUNT_WEATHER_INST_2` | Carvanha 27 | Sharpedo 34 |
| `TRAINER_GRUNT_WEATHER_INST_3` | Carvanha 26 | Sharpedo 32 |
| `TRAINER_GRUNT_SPACE_CENTER_1` | Numel 32 | Camerupt 41 |
| `TRAINER_GRUNT_WEATHER_INST_4` | Carvanha 28 | Sharpedo 35 |
| `TRAINER_LEAH` | Spoink 31 | Grumpig 38 |
| `TRAINER_ROSE_5` | Gloom 34 | Vileplume 41 |
| `TRAINER_ROSE_5` | Roselia 34 | Roserade 41 |
| `TRAINER_WILTON_4` | Wailmer 32 | Wailord 40 |
| `TRAINER_WILTON_5` | Wailmer 35 | Wailord 43 |
| `TRAINER_WARREN` | Graveler 33 | Golem 42 |
| `TRAINER_BROOKE_3` | Numel 29 | Camerupt 34 |
| `TRAINER_BROOKE_4` | Numel 32 | Camerupt 40 |
| `TRAINER_BROOKE_4` | Roselia 32 | Roserade 40 |
| `TRAINER_BROOKE_5` | Roselia 34 | Roserade 41 |
| `TRAINER_TASHA` | Shuppet 32 | Banette 39 |
| `TRAINER_VALERIE_2` | Spoink 31 | Grumpig 38 |
| `TRAINER_GRUNT_SPACE_CENTER_2` | Numel 30 | Camerupt 38 |
| `TRAINER_SHEILA` | Shroomish 21 | Breloom 25 |
| `TRAINER_OLIVIA` | Clamperl 35 | Huntail 45 |
| `TRAINER_OLIVIA` | Lombre 39 | Ludicolo 50 |
| `TRAINER_MOLLIE` | Meditite 33 | Medicham 42 |
| `TRAINER_STEVE_5` | Rhydon 35 | Rhyperior 43 |
| `TRAINER_LUIS` | Carvanha 26 | Sharpedo 32 |
| `TRAINER_DOMINIK` | Tentacool 26 | Tentacruel 32 |
| `TRAINER_DARRIN` | Tentacool 24 | Tentacruel 30 |
| `TRAINER_DARRIN` | Wingull 24 | Pelipper 30 |
| `TRAINER_DARRIN` | Tentacool 24 | Tentacruel 30 |
| `TRAINER_TONY_1` | Carvanha 26 | Sharpedo 32 |
| `TRAINER_MATTHEW` | Carvanha 26 | Sharpedo 32 |
| `TRAINER_SANTIAGO` | Wailmer 33 | Wailord 42 |
| `TRAINER_FRANKLIN` | Sealeo 34 | Walrein 44 |
| `TRAINER_CHAD` | Wailmer 33 | Wailord 40 |
| `TRAINER_TONY_4` | Staryu 34 | Starmie 41 |
| `TRAINER_HITOSHI` | Machoke 32 | Machamp 41 |
| `TRAINER_KOICHI` | Machop 24 | Machoke 28 |
| `TRAINER_NOB_5` | Machoke 33 | Machamp 41 |
| `TRAINER_NOB_5` | Machoke 33 | Machamp 41 |
| `TRAINER_DALTON_2` | Magnemite 25 | Magneton 31 |
| `TRAINER_DALTON_2` | Magnemite 25 | Magneton 31 |
| `TRAINER_DALTON_3` | Magnemite 28 | Magneton 35 |
| `TRAINER_DALTON_3` | Magnemite 28 | Magneton 35 |
| `TRAINER_DALTON_5` | Magneton 34 | Magnezone 41 |
| `TRAINER_DALTON_5` | Magneton 34 | Magnezone 41 |
| `TRAINER_BERNIE_4` | Slugma 32 | Magcargo 40 |
| `TRAINER_BEAU` | Sandshrew 21 | Sandslash 24 |
| `TRAINER_ETHAN_1` | Taillow 20 | Swellow 23 |
| `TRAINER_AUTUMN` | Shroomish 21 | Breloom 25 |
| `TRAINER_EDWARD` | Abra 15 | Kadabra 17 |
| `TRAINER_BLAKE` | Girafarig 36 | Farigiraf 44 |
| `TRAINER_WILLIAM` | Kirlia 26 | Gardevoir 32 |
| `TRAINER_CAMERON_2` | Kadabra 33 | Alakazam 40 |
| `TRAINER_CAMERON_3` | Kadabra 38 | Alakazam 46 |
| `TRAINER_MAURA` | Kadabra 36 | Alakazam 44 |
| `TRAINER_JACKI_2` | Kadabra 34 | Alakazam 41 |
| `TRAINER_JACKI_3` | Kadabra 37 | Alakazam 45 |
| `TRAINER_JERRY_3` | Kirlia 29 | Gardevoir 34 |
| `TRAINER_KAREN_4` | Loudred 32 | Exploud 40 |
| `TRAINER_MIGUEL_3` | Skitty 32 | Delcatty 40 |
| `TRAINER_BETHANY` | Azurill 35 | Marill 45 |
| `TRAINER_SHELBY_1` | Makuhita 21 | Hariyama 25 |
| `TRAINER_BARNY` | Tentacool 25 | Tentacruel 31 |
| `TRAINER_BARNY` | Carvanha 25 | Sharpedo 31 |
| `TRAINER_ELLIOT_3` | Carvanha 26 | Sharpedo 30 |
| `TRAINER_ELLIOT_3` | Tentacool 26 | Tentacruel 30 |
| `TRAINER_RONALD` | Magikarp 19 | Gyarados 24 |
| `TRAINER_BENJAMIN_4` | Magneton 36 | Magnezone 44 |
| `TRAINER_BENJAMIN_5` | Magneton 39 | Magnezone 47 |
| `TRAINER_ABIGAIL_2` | Magnemite 28 | Magneton 33 |
| `TRAINER_ABIGAIL_4` | Magneton 34 | Magnezone 41 |
| `TRAINER_ABIGAIL_5` | Magneton 37 | Magnezone 45 |
| `TRAINER_DYLAN_2` | Doduo 28 | Dodrio 33 |
| `TRAINER_MARIA_2` | Doduo 28 | Dodrio 33 |
| `TRAINER_CAMDEN` | Staryu 33 | Starmie 40 |
| `TRAINER_CAMDEN` | Staryu 33 | Starmie 40 |
| `TRAINER_DEMETRIUS` | Electrike 25 | Manectric 31 |
| `TRAINER_ISAIAH_1` | Staryu 35 | Starmie 43 |
| `TRAINER_PABLO_1` | Staryu 33 | Starmie 40 |
| `TRAINER_PABLO_1` | Staryu 33 | Starmie 40 |
| `TRAINER_CHASE` | Staryu 34 | Starmie 44 |
| `TRAINER_ISAIAH_2` | Staryu 39 | Starmie 47 |
| `TRAINER_ISOBEL` | Staryu 34 | Starmie 41 |
| `TRAINER_DONNY` | Staryu 34 | Starmie 41 |
| `TRAINER_TALIA` | Staryu 34 | Starmie 44 |
| `TRAINER_KATELYN_1` | Staryu 35 | Starmie 43 |
| `TRAINER_ALLISON` | Staryu 33 | Starmie 42 |
| `TRAINER_KATELYN_2` | Staryu 39 | Starmie 47 |
| `TRAINER_NICOLAS_5` | Shelgon 49 | Salamence 69 |
| `TRAINER_JARED` | Doduo 27 | Dodrio 34 |
| `TRAINER_EDWARDO` | Doduo 29 | Dodrio 36 |
| `TRAINER_ROBERT_1` | Swablu 29 | Altaria 36 |
| `TRAINER_ROBERT_2` | Swablu 32 | Altaria 40 |
| `TRAINER_LAO_4` | Koffing 30 | Weezing 37 |
| `TRAINER_LAO_4` | Koffing 30 | Weezing 37 |
| `TRAINER_LAO_4` | Koffing 30 | Weezing 37 |
| `TRAINER_LAO_4` | Koffing 32 | Weezing 40 |
| `TRAINER_LAO_5` | Koffing 33 | Weezing 40 |
| `TRAINER_LAO_5` | Koffing 33 | Weezing 40 |
| `TRAINER_LAO_5` | Koffing 33 | Weezing 40 |
| `TRAINER_MADELINE_2` | Numel 29 | Camerupt 34 |
| `TRAINER_MADELINE_3` | Numel 32 | Camerupt 40 |
| `TRAINER_MADELINE_4` | Roselia 34 | Roserade 41 |
| `TRAINER_MADELINE_5` | Roselia 37 | Roserade 45 |
| `TRAINER_ALICE` | Wingull 24 | Pelipper 27 |
| `TRAINER_JENNY_1` | Wailmer 34 | Wailord 41 |
| `TRAINER_LINDA` | Seadra 33 | Kingdra 42 |
| `TRAINER_JENNY_2` | Wailmer 38 | Wailord 46 |
| `TRAINER_DIANA_1` | Oddish 19 | Gloom 22 |
| `TRAINER_IRENE` | Marill 17 | Azumarill 19 |
| `TRAINER_DIANA_4` | Swablu 31 | Altaria 35 |
| `TRAINER_ERNEST_1` | Machoke 33 | Machamp 40 |
| `TRAINER_ERNEST_2` | Machoke 36 | Machamp 44 |
| `TRAINER_ERNEST_3` | Machoke 39 | Machamp 47 |
| `TRAINER_ANNIKA` | Feebas 39 | Milotic 50 |
| `TRAINER_ANNIKA` | Feebas 39 | Milotic 50 |
| `TRAINER_JONAS` | Koffing 31 | Weezing 38 |
| `TRAINER_KELVIN` | Machoke 33 | Machamp 42 |
| `TRAINER_REYNA` | Meditite 33 | Medicham 42 |
| `TRAINER_HUDSON` | Wailmer 34 | Wailord 44 |
| `TRAINER_EDWIN_4` | Lombre 32 | Ludicolo 40 |
| `TRAINER_EDWIN_4` | Nuzleaf 32 | Shiftry 40 |
| `TRAINER_ISAAC_2` | Makuhita 22 | Hariyama 25 |
| `TRAINER_ISAAC_4` | Aron 28 | Lairon 33 |
| `TRAINER_LYDIA_2` | Wingull 22 | Pelipper 25 |
| `TRAINER_LYDIA_2` | Shroomish 22 | Breloom 25 |
| `TRAINER_LYDIA_4` | Goldeen 28 | Seaking 33 |
| `TRAINER_SOPHIA` | Roselia 38 | Roserade 46 |
| `TRAINER_CATHERINE_3` | Gloom 33 | Vileplume 41 |
| `TRAINER_CATHERINE_3` | Roselia 33 | Roserade 41 |
| `TRAINER_CATHERINE_4` | Gloom 36 | Vileplume 44 |
| `TRAINER_CATHERINE_4` | Roselia 36 | Roserade 44 |
| `TRAINER_CATHERINE_5` | Roselia 39 | Roserade 47 |
| `TRAINER_GRUNT_SEAFLOOR_CAVERN_5` | Golbat 35 | Crobat 45 |
| `TRAINER_SYLVIA` | Meditite 36 | Medicham 44 |
| `TRAINER_GRUNT_MT_CHIMNEY_2` | Zubat 20 | Golbat 23 |
| `TRAINER_KATHLEEN` | Kadabra 36 | Alakazam 44 |
| `TRAINER_CLIFFORD` | Girafarig 36 | Farigiraf 44 |
| `TRAINER_GRUNT_SPACE_CENTER_4` | Baltoy 32 | Claydol 41 |
| `TRAINER_GRUNT_SPACE_CENTER_7` | Baltoy 32 | Claydol 41 |
| `TRAINER_ISABELLA` | Staryu 34 | Starmie 41 |
| `TRAINER_JONATHAN` | Loudred 33 | Exploud 42 |
| `TRAINER_HALEY_4` | Lombre 32 | Ludicolo 40 |
| `TRAINER_HALEY_5` | Lombre 34 | Ludicolo 41 |
| `TRAINER_CRISSY` | Wailmer 39 | Wailord 50 |
| `TRAINER_ALAN` | Geodude 22 | Graveler 25 |
| `TRAINER_TRENT_2` | Geodude 24 | Graveler 28 |
| `TRAINER_TRENT_2` | Geodude 24 | Graveler 28 |
| `TRAINER_TRENT_2` | Geodude 24 | Graveler 28 |
| `TRAINER_TRENT_5` | Graveler 33 | Golem 41 |
| `TRAINER_TRENT_5` | Graveler 33 | Golem 41 |
| `TRAINER_TRENT_5` | Graveler 33 | Golem 41 |
| `TRAINER_KEIGO` | Koffing 28 | Weezing 35 |
| `TRAINER_RILEY` | Koffing 28 | Weezing 35 |
| `TRAINER_ALEXA` | Gloom 34 | Vileplume 41 |
| `TRAINER_RUBEN` | Nosepass 34 | Probopass 41 |
| `TRAINER_KOJI_1` | Machoke 34 | Machamp 41 |
| `TRAINER_WAYNE` | Wailmer 36 | Wailord 44 |
| `TRAINER_KIM_AND_IRIS` | Swablu 32 | Altaria 39 |
| `TRAINER_LISA_AND_RAY` | Goldeen 27 | Seaking 34 |
| `TRAINER_LISA_AND_RAY` | Tentacool 25 | Tentacruel 31 |
| `TRAINER_SOPHIE` | Marill 17 | Azumarill 20 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_3` | Numel 29 | Camerupt 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_5` | Numel 28 | Camerupt 34 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_12` | Numel 29 | Camerupt 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_15` | Numel 29 | Camerupt 35 |
| `TRAINER_CORY_1` | Wingull 24 | Pelipper 30 |
| `TRAINER_CORY_1` | Machop 24 | Machoke 30 |
| `TRAINER_CORY_1` | Tentacool 24 | Tentacruel 30 |
| `TRAINER_ALIX` | Kirlia 26 | Gardevoir 30 |
| `TRAINER_MAKAYLA` | Roselia 33 | Roserade 42 |
| `TRAINER_MYLES` | Electrike 25 | Manectric 30 |
| `TRAINER_PAT` | Electrike 25 | Manectric 30 |
| `TRAINER_PAT` | Gulpin 25 | Swalot 30 |
| `TRAINER_ANDRES_3` | Nosepass 33 | Probopass 41 |
| `TRAINER_ANDRES_4` | Nosepass 35 | Probopass 43 |
| `TRAINER_ANDRES_5` | Nosepass 37 | Probopass 45 |
| `TRAINER_CORY_5` | Machoke 36 | Machamp 44 |
| `TRAINER_PABLO_2` | Staryu 37 | Starmie 45 |
| `TRAINER_PABLO_2` | Staryu 37 | Starmie 45 |
| `TRAINER_PABLO_3` | Staryu 39 | Starmie 47 |
| `TRAINER_PABLO_3` | Staryu 39 | Starmie 47 |
| `TRAINER_KOJI_2` | Machoke 37 | Machamp 45 |
| `TRAINER_KOJI_2` | Machoke 37 | Machamp 45 |
| `TRAINER_KOJI_3` | Machoke 39 | Machamp 47 |
| `TRAINER_KOJI_3` | Machoke 39 | Machamp 47 |
| `TRAINER_CRISTIN_2` | Loudred 35 | Exploud 43 |
| `TRAINER_CRISTIN_2` | Vigoroth 35 | Slaking 43 |
| `TRAINER_CRISTIN_3` | Loudred 37 | Exploud 45 |
| `TRAINER_CRISTIN_4` | Loudred 39 | Exploud 47 |
| `TRAINER_FERNANDO_2` | Loudred 35 | Exploud 43 |
| `TRAINER_FERNANDO_3` | Loudred 37 | Exploud 45 |
| `TRAINER_FERNANDO_4` | Loudred 39 | Exploud 47 |
| `TRAINER_SAWYER_3` | Numel 28 | Camerupt 33 |
| `TRAINER_SAWYER_4` | Numel 30 | Camerupt 34 |
| `TRAINER_SAWYER_5` | Machoke 33 | Machamp 41 |
| `TRAINER_GABRIELLE_3` | Skitty 33 | Delcatty 40 |
| `TRAINER_GABRIELLE_3` | Lombre 33 | Ludicolo 40 |
| `TRAINER_GABRIELLE_3` | Nuzleaf 33 | Shiftry 40 |
| `TRAINER_GABRIELLE_4` | Lombre 35 | Ludicolo 43 |
| `TRAINER_GABRIELLE_4` | Nuzleaf 35 | Shiftry 43 |
| `TRAINER_THALIA_2` | Wailmer 34 | Wailord 41 |
| `TRAINER_THALIA_3` | Wailmer 36 | Wailord 44 |
| `TRAINER_THALIA_3` | Seadra 36 | Kingdra 44 |
| `TRAINER_THALIA_4` | Wailmer 38 | Wailord 46 |
| `TRAINER_THALIA_4` | Seadra 38 | Kingdra 46 |

## Dresseurs

| Dresseur | Map | Étape | Avant | Après |
|---|---|---|---|---|
| `TRAINER_GRUNT_PETALBURG_WOODS` | PetalburgWoods | Avant le 1er badge | 9 | 10 |
| `TRAINER_JAMES_1` | PetalburgWoods | Avant le 1er badge | 6 | 6 |
| `TRAINER_LYLE` | PetalburgWoods | Avant le 1er badge | 3 | 3 |
| `TRAINER_ALLEN` | Route102 | Avant le 1er badge | 3-4 | 3-4 |
| `TRAINER_CALVIN_1` | Route102 | Avant le 1er badge | 5 | 5 |
| `TRAINER_RICK` | Route102 | Avant le 1er badge | 4 | 4 |
| `TRAINER_TIANA` | Route102 | Avant le 1er badge | 4 | 4 |
| `TRAINER_AMY_AND_LIV_1` | Route103 | Avant le 1er badge | 15 | 16 |
| `TRAINER_ANDREW` | Route103 | Avant le 1er badge | 5-15 | 5-16 |
| `TRAINER_DAISY` | Route103 | Avant le 1er badge | 14 | 15 |
| `TRAINER_ISABELLE` | Route103 | Avant le 1er badge | 15 | 16 |
| `TRAINER_MARCOS` | Route103 | Avant le 1er badge | 15 | 16 |
| `TRAINER_MIGUEL_1` | Route103 | Avant le 1er badge | 15 | 16 |
| `TRAINER_PETE` | Route103 | Avant le 1er badge | 15 | 16 |
| `TRAINER_RHETT` | Route103 | Avant le 1er badge | 15 | 16 |
| `TRAINER_BILLY` | Route104 | Avant le 1er badge | 5-7 | 5-7 |
| `TRAINER_CINDY_1` | Route104 | Avant le 1er badge | 7 | 7 |
| `TRAINER_DARIAN` | Route104 | Avant le 1er badge | 9 | 10 |
| `TRAINER_GINA_AND_MIA_1` | Route104 | Avant le 1er badge | 6 | 6 |
| `TRAINER_HALEY_1` | Route104 | Avant le 1er badge | 6 | 6 |
| `TRAINER_IVAN` | Route104 | Avant le 1er badge | 5-7 | 5-7 |
| `TRAINER_WINSTON_1` | Route104 | Avant le 1er badge | 7 | 7 |
| `TRAINER_CLARK` | Route116 | Avant le 1er badge | 8 | 9 |
| `TRAINER_DAWSON` | Route116 | Avant le 1er badge | 8 | 9 |
| `TRAINER_DEVAN` | Route116 | Avant le 1er badge | 8 | 9 |
| `TRAINER_JANICE` | Route116 | Avant le 1er badge | 9 | 10 |
| `TRAINER_JERRY_1` | Route116 | Avant le 1er badge | 9 | 10 |
| `TRAINER_JOEY` | Route116 | Avant le 1er badge | 9 | 10 |
| `TRAINER_JOHNSON` | Route116 | Avant le 1er badge | 8 | 9 |
| `TRAINER_JOSE` | Route116 | Avant le 1er badge | 8 | 9 |
| `TRAINER_KAREN_1` | Route116 | Avant le 1er badge | 9 | 10 |
| `TRAINER_SARAH` | Route116 | Avant le 1er badge | 8 | 9 |
| `TRAINER_JOSH` | RustboroCity_Gym | Avant le 1er badge | 10 | 11 |
| `TRAINER_MARC` | RustboroCity_Gym | Avant le 1er badge | 8 | 9 |
| `TRAINER_TOMMY` | RustboroCity_Gym | Avant le 1er badge | 8 | 9 |
| `TRAINER_BRENDEN` | DewfordTown_Gym | 1er → 2e badge | 13 | 14 |
| `TRAINER_CRISTIAN` | DewfordTown_Gym | 1er → 2e badge | 13 | 14 |
| `TRAINER_JOCELYN` | DewfordTown_Gym | 1er → 2e badge | 13 | 14 |
| `TRAINER_LAURA` | DewfordTown_Gym | 1er → 2e badge | 13 | 14 |
| `TRAINER_LILITH` | DewfordTown_Gym | 1er → 2e badge | 13 | 14 |
| `TRAINER_TAKAO` | DewfordTown_Gym | 1er → 2e badge | 13 | 14 |
| `TRAINER_ELLIOT_1` | Route106 | 1er → 2e badge | 7-10 | 7-11 |
| `TRAINER_NED` | Route106 | 1er → 2e badge | 11 | 12 |
| `TRAINER_GRUNT_RUSTURF_TUNNEL` | RusturfTunnel | 1er → 2e badge | 11 | 12 |
| `TRAINER_MIKE_2` | RusturfTunnel | 1er → 2e badge | 16 | 17 |
| `TRAINER_ANGELO` | MauvilleCity_Gym | 2e → 3e badge | 17 | 19 |
| `TRAINER_BEN` | MauvilleCity_Gym | 2e → 3e badge | 17 | 19 |
| `TRAINER_KIRK` | MauvilleCity_Gym | 2e → 3e badge | 17 | 19 |
| `TRAINER_SHAWN` | MauvilleCity_Gym | 2e → 3e badge | 17 | 19 |
| `TRAINER_VIVIAN` | MauvilleCity_Gym | 2e → 3e badge | 17 | 19 |
| `TRAINER_DOUGLAS` | Route106 | 2e → 3e badge | 24 | 27 |
| `TRAINER_ALICE` | Route109 | 2e → 3e badge | 24 | 27 |
| `TRAINER_CHANDLER` | Route109 | 2e → 3e badge | 12 | 14 |
| `TRAINER_EDMOND` | Route109 | 2e → 3e badge | 13 | 15 |
| `TRAINER_HAILEY` | Route109 | 2e → 3e badge | 13 | 15 |
| `TRAINER_HUEY` | Route109 | 2e → 3e badge | 12 | 14 |
| `TRAINER_LOLA_1` | Route109 | 2e → 3e badge | 12 | 14 |
| `TRAINER_RICKY_1` | Route109 | 2e → 3e badge | 13 | 15 |
| `TRAINER_DWAYNE` | Route109_SeashoreHouse | 2e → 3e badge | 11 | 12 |
| `TRAINER_JOHANNA` | Route109_SeashoreHouse | 2e → 3e badge | 13 | 15 |
| `TRAINER_SIMON` | Route109_SeashoreHouse | 2e → 3e badge | 12 | 14 |
| `TRAINER_ABIGAIL_1` | Route110 | 2e → 3e badge | 16 | 18 |
| `TRAINER_ALYSSA` | Route110 | 2e → 3e badge | 15 | 17 |
| `TRAINER_ANTHONY` | Route110 | 2e → 3e badge | 14 | 16 |
| `TRAINER_BENJAMIN_1` | Route110 | 2e → 3e badge | 16 | 18 |
| `TRAINER_DALE` | Route110 | 2e → 3e badge | 11-14 | 12-16 |
| `TRAINER_EDWARD` | Route110 | 2e → 3e badge | 15 | 17 |
| `TRAINER_EDWIN_1` | Route110 | 2e → 3e badge | 14 | 16 |
| `TRAINER_ISABEL_1` | Route110 | 2e → 3e badge | 14 | 16 |
| `TRAINER_JACLYN` | Route110 | 2e → 3e badge | 16 | 18 |
| `TRAINER_JACOB` | Route110 | 2e → 3e badge | 6-14 | 7-16 |
| `TRAINER_JASMINE` | Route110 | 2e → 3e badge | 6-14 | 7-16 |
| `TRAINER_JOSEPH` | Route110 | 2e → 3e badge | 14 | 16 |
| `TRAINER_KALEB` | Route110 | 2e → 3e badge | 14 | 16 |
| `TRAINER_TIMMY` | Route110 | 2e → 3e badge | 13-15 | 15-17 |
| `TRAINER_EDDIE` | Route110_TrickHousePuzzle1 | 2e → 3e badge | 14-16 | 16-18 |
| `TRAINER_ROBIN` | Route110_TrickHousePuzzle1 | 2e → 3e badge | 14 | 16 |
| `TRAINER_SALLY` | Route110_TrickHousePuzzle1 | 2e → 3e badge | 16 | 18 |
| `TRAINER_GEORGIA` | Route110_TrickHousePuzzle2 | 2e → 3e badge | 16 | 18 |
| `TRAINER_PAUL` | Route110_TrickHousePuzzle2 | 2e → 3e badge | 15 | 17 |
| `TRAINER_TED` | Route110_TrickHousePuzzle2 | 2e → 3e badge | 17 | 19 |
| `TRAINER_ALAN` | Route110_TrickHousePuzzle3 | 2e → 3e badge | 22 | 25 |
| `TRAINER_JUSTIN` | Route110_TrickHousePuzzle3 | 2e → 3e badge | 24 | 27 |
| `TRAINER_MARTHA` | Route110_TrickHousePuzzle3 | 2e → 3e badge | 23 | 26 |
| `TRAINER_BEAU` | Route111 | 2e → 3e badge | 21 | 24 |
| `TRAINER_BECKY` | Route111 | 2e → 3e badge | 22 | 25 |
| `TRAINER_BIANCA` | Route111 | 2e → 3e badge | 18 | 20 |
| `TRAINER_BRANDEN` | Route111 | 2e → 3e badge | 22 | 25 |
| `TRAINER_BROOKE_1` | Route111 | 2e → 3e badge | 17 | 19 |
| `TRAINER_BRYAN` | Route111 | 2e → 3e badge | 22 | 25 |
| `TRAINER_CELIA` | Route111 | 2e → 3e badge | 22 | 25 |
| `TRAINER_CELINA` | Route111 | 2e → 3e badge | 18 | 20 |
| `TRAINER_DAISUKE` | Route111 | 2e → 3e badge | 19 | 21 |
| `TRAINER_DREW` | Route111 | 2e → 3e badge | 23 | 26 |
| `TRAINER_DUSTY_1` | Route111 | 2e → 3e badge | 23 | 26 |
| `TRAINER_HAYDEN` | Route111 | 2e → 3e badge | 18 | 20 |
| `TRAINER_HEIDI` | Route111 | 2e → 3e badge | 22 | 25 |
| `TRAINER_IRENE` | Route111 | 2e → 3e badge | 17 | 19 |
| `TRAINER_TRAVIS` | Route111 | 2e → 3e badge | 18 | 20 |
| `TRAINER_TYRON` | Route111 | 2e → 3e badge | 19 | 21 |
| `TRAINER_VICKY` | Route111 | 2e → 3e badge | 18 | 20 |
| `TRAINER_VICTOR` | Route111 | 2e → 3e badge | 16 | 18 |
| `TRAINER_VICTORIA` | Route111 | 2e → 3e badge | 17 | 19 |
| `TRAINER_VIVI` | Route111 | 2e → 3e badge | 15 | 17 |
| `TRAINER_WILTON_1` | Route111 | 2e → 3e badge | 17 | 19 |
| `TRAINER_AISHA` | Route117 | 2e → 3e badge | 17 | 19 |
| `TRAINER_ANNA_AND_MEG_1` | Route117 | 2e → 3e badge | 15-17 | 17-19 |
| `TRAINER_BRANDI` | Route117 | 2e → 3e badge | 17 | 19 |
| `TRAINER_DEREK` | Route117 | 2e → 3e badge | 16 | 18 |
| `TRAINER_DYLAN_1` | Route117 | 2e → 3e badge | 17 | 19 |
| `TRAINER_ISAAC_1` | Route117 | 2e → 3e badge | 11 | 12 |
| `TRAINER_ISAAC_2` | Route117 | 2e → 3e badge | 22 | 25 |
| `TRAINER_LYDIA_1` | Route117 | 2e → 3e badge | 11 | 12 |
| `TRAINER_LYDIA_2` | Route117 | 2e → 3e badge | 22 | 25 |
| `TRAINER_MARIA_1` | Route117 | 2e → 3e badge | 17 | 19 |
| `TRAINER_MELINA` | Route117 | 2e → 3e badge | 17 | 19 |
| `TRAINER_GRUNT_MUSEUM_1` | SlateportCity_OceanicMuseum_2F | 2e → 3e badge | 15 | 17 |
| `TRAINER_GRUNT_MUSEUM_2` | SlateportCity_OceanicMuseum_2F | 2e → 3e badge | 14 | 16 |
| `TRAINER_AUTUMN` | JaggedPass | 3e → 4e badge | 21 | 25 |
| `TRAINER_DIANA_1` | JaggedPass | 3e → 4e badge | 19 | 22 |
| `TRAINER_DIANA_2` | JaggedPass | 3e → 4e badge | 25 | 29 |
| `TRAINER_DIANA_3` | JaggedPass | 3e → 4e badge | 28 | 33 |
| `TRAINER_ERIC` | JaggedPass | 3e → 4e badge | 20 | 23 |
| `TRAINER_ETHAN_1` | JaggedPass | 3e → 4e badge | 20 | 23 |
| `TRAINER_ETHAN_2` | JaggedPass | 3e → 4e badge | 26 | 30 |
| `TRAINER_ETHAN_3` | JaggedPass | 3e → 4e badge | 29 | 34 |
| `TRAINER_GRUNT_JAGGED_PASS` | JaggedPass | 3e → 4e badge | 22 | 26 |
| `TRAINER_JULIO` | JaggedPass | 3e → 4e badge | 21 | 25 |
| `TRAINER_AXLE` | LavaridgeTown_Gym_1F | 3e → 4e badge | 23 | 27 |
| `TRAINER_COLE` | LavaridgeTown_Gym_1F | 3e → 4e badge | 23 | 27 |
| `TRAINER_DANIELLE` | LavaridgeTown_Gym_1F | 3e → 4e badge | 23 | 27 |
| `TRAINER_GERALD` | LavaridgeTown_Gym_1F | 3e → 4e badge | 23 | 27 |
| `TRAINER_ELI` | LavaridgeTown_Gym_1F, LavaridgeTown_Gym_B1F | 3e → 4e badge | 23 | 27 |
| `TRAINER_JACE` | LavaridgeTown_Gym_1F, LavaridgeTown_Gym_B1F | 3e → 4e badge | 23 | 27 |
| `TRAINER_JEFF` | LavaridgeTown_Gym_1F, LavaridgeTown_Gym_B1F | 3e → 4e badge | 22 | 26 |
| `TRAINER_KEEGAN` | LavaridgeTown_Gym_1F, LavaridgeTown_Gym_B1F | 3e → 4e badge | 23 | 27 |
| `TRAINER_GRUNT_MT_CHIMNEY_1` | MtChimney | 3e → 4e badge | 20 | 23 |
| `TRAINER_GRUNT_MT_CHIMNEY_2` | MtChimney | 3e → 4e badge | 20 | 23 |
| `TRAINER_MELISSA` | MtChimney | 3e → 4e badge | 21 | 25 |
| `TRAINER_SAWYER_1` | MtChimney | 3e → 4e badge | 21 | 25 |
| `TRAINER_SAWYER_2` | MtChimney | 3e → 4e badge | 26 | 30 |
| `TRAINER_SAWYER_3` | MtChimney | 3e → 4e badge | 28 | 33 |
| `TRAINER_SHEILA` | MtChimney | 3e → 4e badge | 21 | 25 |
| `TRAINER_SHELBY_1` | MtChimney | 3e → 4e badge | 21 | 25 |
| `TRAINER_SHIRLEY` | MtChimney | 3e → 4e badge | 21 | 25 |
| `TRAINER_JAMES_2` | PetalburgWoods | 3e → 4e badge | 27 | 32 |
| `TRAINER_JAMES_3` | PetalburgWoods | 3e → 4e badge | 29 | 34 |
| `TRAINER_CALVIN_2` | Route102 | 3e → 4e badge | 27 | 32 |
| `TRAINER_AMY_AND_LIV_2` | Route103 | 3e → 4e badge | 27 | 32 |
| `TRAINER_MIGUEL_2` | Route103 | 3e → 4e badge | 29 | 34 |
| `TRAINER_CINDY_3` | Route104 | 3e → 4e badge | 27 | 32 |
| `TRAINER_HALEY_2` | Route104 | 3e → 4e badge | 26 | 30 |
| `TRAINER_HALEY_3` | Route104 | 3e → 4e badge | 29 | 34 |
| `TRAINER_WINSTON_2` | Route104 | 3e → 4e badge | 27 | 32 |
| `TRAINER_ELLIOT_2` | Route106 | 3e → 4e badge | 24-27 | 28-32 |
| `TRAINER_ELLIOT_3` | Route106 | 3e → 4e badge | 26-29 | 30-34 |
| `TRAINER_KYLA` | Route106 | 3e → 4e badge | 26 | 30 |
| `TRAINER_AUSTINA` | Route109 | 3e → 4e badge | 26 | 30 |
| `TRAINER_CARTER` | Route109 | 3e → 4e badge | 25 | 29 |
| `TRAINER_DAVID` | Route109 | 3e → 4e badge | 25 | 29 |
| `TRAINER_ELIJAH` | Route109 | 3e → 4e badge | 25 | 29 |
| `TRAINER_GWEN` | Route109 | 3e → 4e badge | 26 | 30 |
| `TRAINER_LOLA_2` | Route109 | 3e → 4e badge | 26 | 30 |
| `TRAINER_LOLA_3` | Route109 | 3e → 4e badge | 29 | 34 |
| `TRAINER_MEL_AND_PAUL` | Route109 | 3e → 4e badge | 27 | 32 |
| `TRAINER_RICKY_2` | Route109 | 3e → 4e badge | 27 | 32 |
| `TRAINER_ABIGAIL_2` | Route110 | 3e → 4e badge | 28 | 33 |
| `TRAINER_EDWIN_2` | Route110 | 3e → 4e badge | 26 | 30 |
| `TRAINER_EDWIN_3` | Route110 | 3e → 4e badge | 29 | 34 |
| `TRAINER_ISABEL_2` | Route110 | 3e → 4e badge | 26 | 30 |
| `TRAINER_ISABEL_3` | Route110 | 3e → 4e badge | 29 | 34 |
| `TRAINER_CORA` | Route110_TrickHousePuzzle4 | 3e → 4e badge | 27 | 32 |
| `TRAINER_PAULA` | Route110_TrickHousePuzzle4 | 3e → 4e badge | 27 | 32 |
| `TRAINER_YUJI` | Route110_TrickHousePuzzle4 | 3e → 4e badge | 26 | 30 |
| `TRAINER_BROOKE_2` | Route111 | 3e → 4e badge | 26 | 30 |
| `TRAINER_BROOKE_3` | Route111 | 3e → 4e badge | 29 | 34 |
| `TRAINER_DUSTY_2` | Route111 | 3e → 4e badge | 27 | 32 |
| `TRAINER_WILTON_2` | Route111 | 3e → 4e badge | 26 | 30 |
| `TRAINER_WILTON_3` | Route111 | 3e → 4e badge | 29 | 34 |
| `TRAINER_BRICE` | Route112 | 3e → 4e badge | 17 | 20 |
| `TRAINER_BRYANT` | Route112 | 3e → 4e badge | 18 | 21 |
| `TRAINER_CAROL` | Route112 | 3e → 4e badge | 17 | 20 |
| `TRAINER_LARRY` | Route112 | 3e → 4e badge | 18 | 21 |
| `TRAINER_SHAYLA` | Route112 | 3e → 4e badge | 18 | 21 |
| `TRAINER_TRENT_1` | Route112 | 3e → 4e badge | 16-17 | 19-20 |
| `TRAINER_TRENT_2` | Route112 | 3e → 4e badge | 24 | 28 |
| `TRAINER_TRENT_3` | Route112 | 3e → 4e badge | 27 | 32 |
| `TRAINER_COBY` | Route113 | 3e → 4e badge | 17-19 | 20-22 |
| `TRAINER_DILLON` | Route113 | 3e → 4e badge | 19 | 22 |
| `TRAINER_JAYLEN` | Route113 | 3e → 4e badge | 19 | 22 |
| `TRAINER_LAO_1` | Route113 | 3e → 4e badge | 17 | 20 |
| `TRAINER_LAO_2` | Route113 | 3e → 4e badge | 24-26 | 28-30 |
| `TRAINER_LAO_3` | Route113 | 3e → 4e badge | 27-29 | 32-34 |
| `TRAINER_LAWRENCE` | Route113 | 3e → 4e badge | 18 | 21 |
| `TRAINER_LUNG` | Route113 | 3e → 4e badge | 18 | 21 |
| `TRAINER_MADELINE_1` | Route113 | 3e → 4e badge | 19 | 22 |
| `TRAINER_MADELINE_2` | Route113 | 3e → 4e badge | 29 | 34 |
| `TRAINER_SOPHIE` | Route113 | 3e → 4e badge | 17-19 | 20-22 |
| `TRAINER_TORI_AND_TIA` | Route113 | 3e → 4e badge | 19 | 22 |
| `TRAINER_WYATT` | Route113 | 3e → 4e badge | 18 | 21 |
| `TRAINER_ANGELINA` | Route114 | 3e → 4e badge | 18 | 21 |
| `TRAINER_BERNIE_1` | Route114 | 3e → 4e badge | 18 | 21 |
| `TRAINER_BERNIE_2` | Route114 | 3e → 4e badge | 26 | 30 |
| `TRAINER_BERNIE_3` | Route114 | 3e → 4e badge | 29 | 34 |
| `TRAINER_CHARLOTTE` | Route114 | 3e → 4e badge | 19 | 22 |
| `TRAINER_CLAUDE` | Route114 | 3e → 4e badge | 16-18 | 19-21 |
| `TRAINER_KAI` | Route114 | 3e → 4e badge | 19 | 22 |
| `TRAINER_LENNY` | Route114 | 3e → 4e badge | 18 | 21 |
| `TRAINER_LUCAS_1` | Route114 | 3e → 4e badge | 18 | 21 |
| `TRAINER_NANCY` | Route114 | 3e → 4e badge | 18 | 21 |
| `TRAINER_NOLAN` | Route114 | 3e → 4e badge | 19 | 22 |
| `TRAINER_SHANE` | Route114 | 3e → 4e badge | 18 | 21 |
| `TRAINER_STEVE_1` | Route114 | 3e → 4e badge | 19 | 22 |
| `TRAINER_STEVE_2` | Route114 | 3e → 4e badge | 27 | 32 |
| `TRAINER_STEVE_3` | Route114 | 3e → 4e badge | 29 | 34 |
| `TRAINER_TYRA_AND_IVY` | Route114 | 3e → 4e badge | 18-20 | 21-23 |
| `TRAINER_ALIX` | Route115 | 3e → 4e badge | 26 | 30 |
| `TRAINER_CYNDY_1` | Route115 | 3e → 4e badge | 18 | 21 |
| `TRAINER_CYNDY_2` | Route115 | 3e → 4e badge | 26 | 30 |
| `TRAINER_CYNDY_3` | Route115 | 3e → 4e badge | 29 | 34 |
| `TRAINER_HECTOR` | Route115 | 3e → 4e badge | 18 | 21 |
| `TRAINER_HELENE` | Route115 | 3e → 4e badge | 26 | 30 |
| `TRAINER_JAIDEN` | Route115 | 3e → 4e badge | 26 | 30 |
| `TRAINER_KOICHI` | Route115 | 3e → 4e badge | 24-28 | 28-33 |
| `TRAINER_KYRA` | Route115 | 3e → 4e badge | 26 | 30 |
| `TRAINER_MARLENE` | Route115 | 3e → 4e badge | 18 | 21 |
| `TRAINER_NOB_1` | Route115 | 3e → 4e badge | 19 | 22 |
| `TRAINER_NOB_2` | Route115 | 3e → 4e badge | 27 | 32 |
| `TRAINER_NOB_3` | Route115 | 3e → 4e badge | 29 | 34 |
| `TRAINER_TIMOTHY_1` | Route115 | 3e → 4e badge | 27 | 32 |
| `TRAINER_JERRY_2` | Route116 | 3e → 4e badge | 26 | 30 |
| `TRAINER_JERRY_3` | Route116 | 3e → 4e badge | 29 | 34 |
| `TRAINER_KAREN_2` | Route116 | 3e → 4e badge | 26 | 30 |
| `TRAINER_KAREN_3` | Route116 | 3e → 4e badge | 29 | 34 |
| `TRAINER_DYLAN_2` | Route117 | 3e → 4e badge | 28 | 33 |
| `TRAINER_ISAAC_3` | Route117 | 3e → 4e badge | 25 | 29 |
| `TRAINER_ISAAC_4` | Route117 | 3e → 4e badge | 28 | 33 |
| `TRAINER_LYDIA_3` | Route117 | 3e → 4e badge | 25 | 29 |
| `TRAINER_LYDIA_4` | Route117 | 3e → 4e badge | 28 | 33 |
| `TRAINER_MARIA_2` | Route117 | 3e → 4e badge | 28 | 33 |
| `TRAINER_DIANA_4` | JaggedPass | 4e → 5e badge | 31 | 35 |
| `TRAINER_ETHAN_4` | JaggedPass | 4e → 5e badge | 31 | 35 |
| `TRAINER_SAWYER_4` | MtChimney | 4e → 5e badge | 30 | 34 |
| `TRAINER_SHELBY_2` | MtChimney | 4e → 5e badge | 30 | 34 |
| `TRAINER_ALEXIA` | PetalburgCity_Gym | 4e → 5e badge | 26 | 29 |
| `TRAINER_BERKE` | PetalburgCity_Gym | 4e → 5e badge | 26 | 29 |
| `TRAINER_GEORGE` | PetalburgCity_Gym | 4e → 5e badge | 26 | 29 |
| `TRAINER_JODY` | PetalburgCity_Gym | 4e → 5e badge | 26 | 29 |
| `TRAINER_MARY` | PetalburgCity_Gym | 4e → 5e badge | 26 | 29 |
| `TRAINER_PARKER` | PetalburgCity_Gym | 4e → 5e badge | 26 | 29 |
| `TRAINER_RANDALL` | PetalburgCity_Gym | 4e → 5e badge | 26 | 29 |
| `TRAINER_JAMES_4` | PetalburgWoods | 4e → 5e badge | 31 | 35 |
| `TRAINER_CALVIN_3` | Route102 | 4e → 5e badge | 28-30 | 32-34 |
| `TRAINER_AMY_AND_LIV_4` | Route103 | 4e → 5e badge | 30 | 34 |
| `TRAINER_CINDY_4` | Route104 | 4e → 5e badge | 30 | 34 |
| `TRAINER_WINSTON_3` | Route104 | 4e → 5e badge | 30 | 34 |
| `TRAINER_ELLIOT_4` | Route106 | 4e → 5e badge | 30-31 | 34-35 |
| `TRAINER_RICKY_3` | Route109 | 4e → 5e badge | 30 | 34 |
| `TRAINER_ABIGAIL_3` | Route110 | 4e → 5e badge | 31 | 35 |
| `TRAINER_BENJAMIN_2` | Route110 | 4e → 5e badge | 30 | 34 |
| `TRAINER_DUSTY_3` | Route111 | 4e → 5e badge | 30 | 34 |
| `TRAINER_TRENT_4` | Route112 | 4e → 5e badge | 30 | 34 |
| `TRAINER_NOB_4` | Route115 | 4e → 5e badge | 31 | 35 |
| `TRAINER_ANNA_AND_MEG_2` | Route117 | 4e → 5e badge | 28-30 | 32-34 |
| `TRAINER_DYLAN_3` | Route117 | 4e → 5e badge | 31 | 35 |
| `TRAINER_ISAAC_5` | Route117 | 4e → 5e badge | 31 | 35 |
| `TRAINER_LYDIA_5` | Route117 | 4e → 5e badge | 31 | 35 |
| `TRAINER_MARIA_3` | Route117 | 4e → 5e badge | 31 | 35 |
| `TRAINER_CHARLIE` | AbandonedShip_Corridors_1F | 5e → 6e badge | 26 | 32 |
| `TRAINER_DUNCAN` | AbandonedShip_Corridors_B1F | 5e → 6e badge | 25 | 31 |
| `TRAINER_GARRISON` | AbandonedShip_Rooms2_1F | 5e → 6e badge | 26 | 32 |
| `TRAINER_JANI` | AbandonedShip_Rooms2_1F | 5e → 6e badge | 26 | 32 |
| `TRAINER_KIRA_AND_DAN_1` | AbandonedShip_Rooms2_1F | 5e → 6e badge | 25 | 31 |
| `TRAINER_KIRA_AND_DAN_2` | AbandonedShip_Rooms2_1F | 5e → 6e badge | 30 | 37 |
| `TRAINER_KIRA_AND_DAN_3` | AbandonedShip_Rooms2_1F | 5e → 6e badge | 33 | 41 |
| `TRAINER_DEMETRIUS` | AbandonedShip_Rooms_1F | 5e → 6e badge | 25 | 31 |
| `TRAINER_THALIA_1` | AbandonedShip_Rooms_1F | 5e → 6e badge | 25 | 31 |
| `TRAINER_ASHLEY` | FortreeCity_Gym | 5e → 6e badge | 27 | 34 |
| `TRAINER_DARIUS` | FortreeCity_Gym | 5e → 6e badge | 30 | 37 |
| `TRAINER_EDWARDO` | FortreeCity_Gym | 5e → 6e badge | 29 | 36 |
| `TRAINER_FLINT` | FortreeCity_Gym | 5e → 6e badge | 29 | 36 |
| `TRAINER_HUMBERTO` | FortreeCity_Gym | 5e → 6e badge | 30 | 37 |
| `TRAINER_JARED` | FortreeCity_Gym | 5e → 6e badge | 27 | 34 |
| `TRAINER_SAWYER_5` | MtChimney | 5e → 6e badge | 33 | 41 |
| `TRAINER_SHELBY_3` | MtChimney | 5e → 6e badge | 33 | 41 |
| `TRAINER_JAMES_5` | PetalburgWoods | 5e → 6e badge | 33 | 41 |
| `TRAINER_CALVIN_4` | Route102 | 5e → 6e badge | 29-33 | 36-41 |
| `TRAINER_AMY_AND_LIV_5` | Route103 | 5e → 6e badge | 33 | 41 |
| `TRAINER_MIGUEL_3` | Route103 | 5e → 6e badge | 32 | 40 |
| `TRAINER_CINDY_5` | Route104 | 5e → 6e badge | 33 | 41 |
| `TRAINER_HALEY_4` | Route104 | 5e → 6e badge | 32 | 40 |
| `TRAINER_WINSTON_4` | Route104 | 5e → 6e badge | 33 | 41 |
| `TRAINER_ANDRES_1` | Route105 | 5e → 6e badge | 25 | 31 |
| `TRAINER_ANDRES_2` | Route105 | 5e → 6e badge | 31 | 39 |
| `TRAINER_ANDRES_3` | Route105 | 5e → 6e badge | 33 | 41 |
| `TRAINER_BEVERLY` | Route105 | 5e → 6e badge | 25 | 31 |
| `TRAINER_DOMINIK` | Route105 | 5e → 6e badge | 26 | 32 |
| `TRAINER_FOSTER` | Route105 | 5e → 6e badge | 25 | 31 |
| `TRAINER_IMANI` | Route105 | 5e → 6e badge | 26 | 32 |
| `TRAINER_JOSUE` | Route105 | 5e → 6e badge | 25 | 31 |
| `TRAINER_LUIS` | Route105 | 5e → 6e badge | 26 | 32 |
| `TRAINER_BETH` | Route107 | 5e → 6e badge | 26 | 32 |
| `TRAINER_CAMRON` | Route107 | 5e → 6e badge | 26 | 32 |
| `TRAINER_DARRIN` | Route107 | 5e → 6e badge | 24 | 30 |
| `TRAINER_DENISE` | Route107 | 5e → 6e badge | 25 | 31 |
| `TRAINER_LISA_AND_RAY` | Route107 | 5e → 6e badge | 25-27 | 31-34 |
| `TRAINER_TONY_1` | Route107 | 5e → 6e badge | 26 | 32 |
| `TRAINER_TONY_2` | Route107 | 5e → 6e badge | 30 | 37 |
| `TRAINER_TONY_3` | Route107 | 5e → 6e badge | 33 | 41 |
| `TRAINER_CAROLINA` | Route108 | 5e → 6e badge | 24 | 30 |
| `TRAINER_CORY_1` | Route108 | 5e → 6e badge | 24 | 30 |
| `TRAINER_CORY_2` | Route108 | 5e → 6e badge | 30 | 37 |
| `TRAINER_CORY_3` | Route108 | 5e → 6e badge | 32 | 40 |
| `TRAINER_JEROME` | Route108 | 5e → 6e badge | 26 | 32 |
| `TRAINER_MATTHEW` | Route108 | 5e → 6e badge | 26 | 32 |
| `TRAINER_MISSY` | Route108 | 5e → 6e badge | 26 | 32 |
| `TRAINER_TARA` | Route108 | 5e → 6e badge | 25 | 31 |
| `TRAINER_LOLA_4` | Route109 | 5e → 6e badge | 32 | 40 |
| `TRAINER_RICKY_4` | Route109 | 5e → 6e badge | 33 | 41 |
| `TRAINER_BENJAMIN_3` | Route110 | 5e → 6e badge | 33 | 41 |
| `TRAINER_EDWIN_4` | Route110 | 5e → 6e badge | 32 | 40 |
| `TRAINER_ISABEL_4` | Route110 | 5e → 6e badge | 32 | 40 |
| `TRAINER_BROOKE_4` | Route111 | 5e → 6e badge | 32 | 40 |
| `TRAINER_DUSTY_4` | Route111 | 5e → 6e badge | 33 | 41 |
| `TRAINER_WILTON_4` | Route111 | 5e → 6e badge | 32 | 40 |
| `TRAINER_TRENT_5` | Route112 | 5e → 6e badge | 33 | 41 |
| `TRAINER_LAO_4` | Route113 | 5e → 6e badge | 30-32 | 37-40 |
| `TRAINER_MADELINE_3` | Route113 | 5e → 6e badge | 32 | 40 |
| `TRAINER_BERNIE_4` | Route114 | 5e → 6e badge | 32 | 40 |
| `TRAINER_STEVE_4` | Route114 | 5e → 6e badge | 32 | 40 |
| `TRAINER_CYNDY_4` | Route115 | 5e → 6e badge | 32 | 40 |
| `TRAINER_NOB_5` | Route115 | 5e → 6e badge | 33 | 41 |
| `TRAINER_TIMOTHY_2` | Route115 | 5e → 6e badge | 33 | 41 |
| `TRAINER_JERRY_4` | Route116 | 5e → 6e badge | 32 | 40 |
| `TRAINER_KAREN_4` | Route116 | 5e → 6e badge | 32 | 40 |
| `TRAINER_ANNA_AND_MEG_3` | Route117 | 5e → 6e badge | 31-33 | 39-41 |
| `TRAINER_BARNY` | Route118 | 5e → 6e badge | 25 | 31 |
| `TRAINER_CHESTER` | Route118 | 5e → 6e badge | 25 | 31 |
| `TRAINER_DALTON_1` | Route118 | 5e → 6e badge | 15 | 19 |
| `TRAINER_DALTON_2` | Route118 | 5e → 6e badge | 25 | 31 |
| `TRAINER_DALTON_3` | Route118 | 5e → 6e badge | 28 | 35 |
| `TRAINER_DALTON_4` | Route118 | 5e → 6e badge | 31 | 39 |
| `TRAINER_DEANDRE` | Route118 | 5e → 6e badge | 14 | 17 |
| `TRAINER_PERRY` | Route118 | 5e → 6e badge | 26 | 32 |
| `TRAINER_ROSE_1` | Route118 | 5e → 6e badge | 14 | 17 |
| `TRAINER_ROSE_2` | Route118 | 5e → 6e badge | 26 | 32 |
| `TRAINER_ROSE_3` | Route118 | 5e → 6e badge | 28 | 35 |
| `TRAINER_ROSE_4` | Route118 | 5e → 6e badge | 31 | 39 |
| `TRAINER_WADE` | Route118 | 5e → 6e badge | 16 | 20 |
| `TRAINER_BRENT` | Route119 | 5e → 6e badge | 26 | 32 |
| `TRAINER_CATHERINE_1` | Route119 | 5e → 6e badge | 26 | 32 |
| `TRAINER_CATHERINE_2` | Route119 | 5e → 6e badge | 30 | 37 |
| `TRAINER_CATHERINE_3` | Route119 | 5e → 6e badge | 33 | 41 |
| `TRAINER_CHRIS` | Route119 | 5e → 6e badge | 20-29 | 25-36 |
| `TRAINER_DAYTON` | Route119 | 5e → 6e badge | 25 | 31 |
| `TRAINER_DONALD` | Route119 | 5e → 6e badge | 24 | 30 |
| `TRAINER_DOUG` | Route119 | 5e → 6e badge | 28 | 35 |
| `TRAINER_FABIAN` | Route119 | 5e → 6e badge | 26 | 32 |
| `TRAINER_GREG` | Route119 | 5e → 6e badge | 25 | 31 |
| `TRAINER_HIDEO` | Route119 | 5e → 6e badge | 25 | 31 |
| `TRAINER_HUGH` | Route119 | 5e → 6e badge | 25 | 31 |
| `TRAINER_JACKSON_1` | Route119 | 5e → 6e badge | 27 | 34 |
| `TRAINER_JACKSON_2` | Route119 | 5e → 6e badge | 31 | 39 |
| `TRAINER_KENT` | Route119 | 5e → 6e badge | 25 | 31 |
| `TRAINER_PHIL` | Route119 | 5e → 6e badge | 26 | 32 |
| `TRAINER_RACHEL` | Route119 | 5e → 6e badge | 26 | 32 |
| `TRAINER_TAKASHI` | Route119 | 5e → 6e badge | 25 | 31 |
| `TRAINER_TAYLOR` | Route119 | 5e → 6e badge | 27 | 34 |
| `TRAINER_YASU` | Route119 | 5e → 6e badge | 26 | 32 |
| `TRAINER_GRUNT_WEATHER_INST_1` | Route119_WeatherInstitute_1F | 5e → 6e badge | 27 | 34 |
| `TRAINER_GRUNT_WEATHER_INST_4` | Route119_WeatherInstitute_1F | 5e → 6e badge | 28 | 35 |
| `TRAINER_GRUNT_WEATHER_INST_2` | Route119_WeatherInstitute_2F | 5e → 6e badge | 27 | 34 |
| `TRAINER_GRUNT_WEATHER_INST_3` | Route119_WeatherInstitute_2F | 5e → 6e badge | 26 | 32 |
| `TRAINER_GRUNT_WEATHER_INST_5` | Route119_WeatherInstitute_2F | 5e → 6e badge | 27 | 34 |
| `TRAINER_ANGELICA` | Route120 | 5e → 6e badge | 30 | 37 |
| `TRAINER_CALLIE` | Route120 | 5e → 6e badge | 28 | 35 |
| `TRAINER_CHIP` | Route120 | 5e → 6e badge | 27 | 34 |
| `TRAINER_CLARISSA` | Route120 | 5e → 6e badge | 28 | 35 |
| `TRAINER_COLIN` | Route120 | 5e → 6e badge | 28 | 35 |
| `TRAINER_JEFFREY_1` | Route120 | 5e → 6e badge | 27 | 34 |
| `TRAINER_JEFFREY_2` | Route120 | 5e → 6e badge | 31 | 39 |
| `TRAINER_JENNA` | Route120 | 5e → 6e badge | 28 | 35 |
| `TRAINER_JENNIFER` | Route120 | 5e → 6e badge | 30 | 37 |
| `TRAINER_KEIGO` | Route120 | 5e → 6e badge | 28 | 35 |
| `TRAINER_LEONEL` | Route120 | 5e → 6e badge | 30 | 37 |
| `TRAINER_LORENZO` | Route120 | 5e → 6e badge | 28 | 35 |
| `TRAINER_RILEY` | Route120 | 5e → 6e badge | 28 | 35 |
| `TRAINER_ROBERT_1` | Route120 | 5e → 6e badge | 29 | 36 |
| `TRAINER_ROBERT_2` | Route120 | 5e → 6e badge | 32 | 40 |
| `TRAINER_KIRA_AND_DAN_4` | AbandonedShip_Rooms2_1F | 6e → 7e badge | 36 | 44 |
| `TRAINER_KIRA_AND_DAN_5` | AbandonedShip_Rooms2_1F | 6e → 7e badge | 39 | 47 |
| `TRAINER_THALIA_2` | AbandonedShip_Rooms_1F | 6e → 7e badge | 34 | 41 |
| `TRAINER_THALIA_3` | AbandonedShip_Rooms_1F | 6e → 7e badge | 36 | 44 |
| `TRAINER_THALIA_4` | AbandonedShip_Rooms_1F | 6e → 7e badge | 38 | 46 |
| `TRAINER_THALIA_5` | AbandonedShip_Rooms_1F | 6e → 7e badge | 40 | 49 |
| `TRAINER_GRUNT_AQUA_HIDEOUT_1` | AquaHideout_1F | 6e → 7e badge | 32 | 39 |
| `TRAINER_GRUNT_AQUA_HIDEOUT_2` | AquaHideout_B1F | 6e → 7e badge | 31 | 38 |
| `TRAINER_GRUNT_AQUA_HIDEOUT_3` | AquaHideout_B1F | 6e → 7e badge | 32 | 39 |
| `TRAINER_GRUNT_AQUA_HIDEOUT_5` | AquaHideout_B1F | 6e → 7e badge | 32 | 39 |
| `TRAINER_GRUNT_AQUA_HIDEOUT_7` | AquaHideout_B1F | 6e → 7e badge | 31 | 38 |
| `TRAINER_GRUNT_AQUA_HIDEOUT_4` | AquaHideout_B2F | 6e → 7e badge | 32 | 39 |
| `TRAINER_GRUNT_AQUA_HIDEOUT_6` | AquaHideout_B2F | 6e → 7e badge | 32 | 39 |
| `TRAINER_GRUNT_AQUA_HIDEOUT_8` | AquaHideout_B2F | 6e → 7e badge | 32 | 39 |
| `TRAINER_DIANA_5` | JaggedPass | 6e → 7e badge | 40 | 49 |
| `TRAINER_ETHAN_5` | JaggedPass | 6e → 7e badge | 34 | 41 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_1` | MagmaHideout_1F | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_2` | MagmaHideout_1F | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_14` | MagmaHideout_2F_1R | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_3` | MagmaHideout_2F_1R | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_4` | MagmaHideout_2F_1R | 6e → 7e badge | 28 | 34 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_5` | MagmaHideout_2F_1R | 6e → 7e badge | 28 | 34 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_15` | MagmaHideout_2F_2R | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_6` | MagmaHideout_2F_2R | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_7` | MagmaHideout_2F_2R | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_8` | MagmaHideout_2F_2R | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_16` | MagmaHideout_3F_1R | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_9` | MagmaHideout_3F_1R | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_10` | MagmaHideout_3F_2R | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_11` | MagmaHideout_4F | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_12` | MagmaHideout_4F | 6e → 7e badge | 29 | 35 |
| `TRAINER_GRUNT_MAGMA_HIDEOUT_13` | MagmaHideout_4F | 6e → 7e badge | 29 | 35 |
| `TRAINER_BLAKE` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_CLIFFORD` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_HANNAH` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_KATHLEEN` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_MACEY` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_MAURA` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_NATE` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_NICHOLAS` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_PRESTON` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_SAMANTHA` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_SYLVIA` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_VIRGIL` | MossdeepCity_Gym | 6e → 7e badge | 36 | 44 |
| `TRAINER_SHELBY_4` | MtChimney | 6e → 7e badge | 36 | 44 |
| `TRAINER_SHELBY_5` | MtChimney | 6e → 7e badge | 39 | 47 |
| `TRAINER_DEZ_AND_LUKE` | MtPyre_2F | 6e → 7e badge | 31 | 38 |
| `TRAINER_LEAH` | MtPyre_2F | 6e → 7e badge | 31 | 38 |
| `TRAINER_MARK` | MtPyre_2F | 6e → 7e badge | 31 | 38 |
| `TRAINER_ZANDER` | MtPyre_2F | 6e → 7e badge | 31 | 38 |
| `TRAINER_GABRIELLE_1` | MtPyre_3F | 6e → 7e badge | 26 | 32 |
| `TRAINER_GABRIELLE_2` | MtPyre_3F | 6e → 7e badge | 31 | 38 |
| `TRAINER_GABRIELLE_3` | MtPyre_3F | 6e → 7e badge | 33 | 40 |
| `TRAINER_GABRIELLE_4` | MtPyre_3F | 6e → 7e badge | 35 | 43 |
| `TRAINER_GABRIELLE_5` | MtPyre_3F | 6e → 7e badge | 37 | 45 |
| `TRAINER_KAYLA` | MtPyre_3F | 6e → 7e badge | 26 | 32 |
| `TRAINER_WILLIAM` | MtPyre_3F | 6e → 7e badge | 26 | 32 |
| `TRAINER_ATSUSHI` | MtPyre_4F | 6e → 7e badge | 32 | 39 |
| `TRAINER_TASHA` | MtPyre_5F | 6e → 7e badge | 32 | 39 |
| `TRAINER_CEDRIC` | MtPyre_6F | 6e → 7e badge | 32 | 39 |
| `TRAINER_VALERIE_1` | MtPyre_6F | 6e → 7e badge | 32 | 39 |
| `TRAINER_VALERIE_2` | MtPyre_6F | 6e → 7e badge | 31 | 38 |
| `TRAINER_VALERIE_3` | MtPyre_6F | 6e → 7e badge | 35 | 43 |
| `TRAINER_VALERIE_4` | MtPyre_6F | 6e → 7e badge | 40 | 49 |
| `TRAINER_VALERIE_5` | MtPyre_6F | 6e → 7e badge | 42 | 51 |
| `TRAINER_GRUNT_MT_PYRE_1` | MtPyre_Summit | 6e → 7e badge | 32 | 39 |
| `TRAINER_GRUNT_MT_PYRE_2` | MtPyre_Summit | 6e → 7e badge | 32 | 39 |
| `TRAINER_GRUNT_MT_PYRE_3` | MtPyre_Summit | 6e → 7e badge | 30 | 36 |
| `TRAINER_GRUNT_MT_PYRE_4` | MtPyre_Summit | 6e → 7e badge | 30 | 36 |
| `TRAINER_CALVIN_5` | Route102 | 6e → 7e badge | 32-36 | 39-44 |
| `TRAINER_AMY_AND_LIV_6` | Route103 | 6e → 7e badge | 36 | 44 |
| `TRAINER_MIGUEL_4` | Route103 | 6e → 7e badge | 35 | 43 |
| `TRAINER_MIGUEL_5` | Route103 | 6e → 7e badge | 38 | 46 |
| `TRAINER_CINDY_6` | Route104 | 6e → 7e badge | 36 | 44 |
| `TRAINER_HALEY_5` | Route104 | 6e → 7e badge | 34 | 41 |
| `TRAINER_WINSTON_5` | Route104 | 6e → 7e badge | 36 | 44 |
| `TRAINER_ANDRES_4` | Route105 | 6e → 7e badge | 35 | 43 |
| `TRAINER_ANDRES_5` | Route105 | 6e → 7e badge | 37 | 45 |
| `TRAINER_ELLIOT_5` | Route106 | 6e → 7e badge | 33-35 | 40-43 |
| `TRAINER_TONY_4` | Route107 | 6e → 7e badge | 34-36 | 41-44 |
| `TRAINER_TONY_5` | Route107 | 6e → 7e badge | 37-39 | 45-47 |
| `TRAINER_CORY_4` | Route108 | 6e → 7e badge | 34 | 41 |
| `TRAINER_CORY_5` | Route108 | 6e → 7e badge | 36 | 44 |
| `TRAINER_LOLA_5` | Route109 | 6e → 7e badge | 35 | 43 |
| `TRAINER_RICKY_5` | Route109 | 6e → 7e badge | 36 | 44 |
| `TRAINER_ABIGAIL_4` | Route110 | 6e → 7e badge | 34 | 41 |
| `TRAINER_ABIGAIL_5` | Route110 | 6e → 7e badge | 37 | 45 |
| `TRAINER_BENJAMIN_4` | Route110 | 6e → 7e badge | 36 | 44 |
| `TRAINER_BENJAMIN_5` | Route110 | 6e → 7e badge | 39 | 47 |
| `TRAINER_EDWIN_5` | Route110 | 6e → 7e badge | 35 | 43 |
| `TRAINER_ISABEL_5` | Route110 | 6e → 7e badge | 35 | 43 |
| `TRAINER_BENNY` | Route110_TrickHousePuzzle6 | 6e → 7e badge | 36 | 44 |
| `TRAINER_SEBASTIAN` | Route110_TrickHousePuzzle6 | 6e → 7e badge | 39 | 47 |
| `TRAINER_SOPHIA` | Route110_TrickHousePuzzle6 | 6e → 7e badge | 38 | 46 |
| `TRAINER_ALEXIS` | Route110_TrickHousePuzzle7 | 6e → 7e badge | 41 | 50 |
| `TRAINER_ALVARO` | Route110_TrickHousePuzzle7 | 6e → 7e badge | 41 | 50 |
| `TRAINER_EVERETT` | Route110_TrickHousePuzzle7 | 6e → 7e badge | 41 | 50 |
| `TRAINER_JOSHUA` | Route110_TrickHousePuzzle7 | 6e → 7e badge | 41 | 50 |
| `TRAINER_MARIELA` | Route110_TrickHousePuzzle7 | 6e → 7e badge | 41 | 50 |
| `TRAINER_PATRICIA` | Route110_TrickHousePuzzle7 | 6e → 7e badge | 41 | 50 |
| `TRAINER_BROOKE_5` | Route111 | 6e → 7e badge | 34 | 41 |
| `TRAINER_DUSTY_5` | Route111 | 6e → 7e badge | 36 | 44 |
| `TRAINER_WILTON_5` | Route111 | 6e → 7e badge | 35 | 43 |
| `TRAINER_LAO_5` | Route113 | 6e → 7e badge | 33-35 | 40-43 |
| `TRAINER_MADELINE_4` | Route113 | 6e → 7e badge | 34 | 41 |
| `TRAINER_MADELINE_5` | Route113 | 6e → 7e badge | 37 | 45 |
| `TRAINER_BERNIE_5` | Route114 | 6e → 7e badge | 35 | 43 |
| `TRAINER_STEVE_5` | Route114 | 6e → 7e badge | 35 | 43 |
| `TRAINER_CYNDY_5` | Route115 | 6e → 7e badge | 35 | 43 |
| `TRAINER_TIMOTHY_3` | Route115 | 6e → 7e badge | 36 | 44 |
| `TRAINER_TIMOTHY_4` | Route115 | 6e → 7e badge | 39 | 47 |
| `TRAINER_TIMOTHY_5` | Route115 | 6e → 7e badge | 42 | 51 |
| `TRAINER_JERRY_5` | Route116 | 6e → 7e badge | 34 | 41 |
| `TRAINER_KAREN_5` | Route116 | 6e → 7e badge | 35 | 43 |
| `TRAINER_ANNA_AND_MEG_4` | Route117 | 6e → 7e badge | 34-36 | 41-44 |
| `TRAINER_ANNA_AND_MEG_5` | Route117 | 6e → 7e badge | 36-38 | 44-46 |
| `TRAINER_DYLAN_4` | Route117 | 6e → 7e badge | 34 | 41 |
| `TRAINER_DYLAN_5` | Route117 | 6e → 7e badge | 37 | 45 |
| `TRAINER_MARIA_4` | Route117 | 6e → 7e badge | 34 | 41 |
| `TRAINER_MARIA_5` | Route117 | 6e → 7e badge | 37 | 45 |
| `TRAINER_DALTON_5` | Route118 | 6e → 7e badge | 34 | 41 |
| `TRAINER_ROSE_5` | Route118 | 6e → 7e badge | 34 | 41 |
| `TRAINER_CATHERINE_4` | Route119 | 6e → 7e badge | 36 | 44 |
| `TRAINER_CATHERINE_5` | Route119 | 6e → 7e badge | 39 | 47 |
| `TRAINER_JACKSON_3` | Route119 | 6e → 7e badge | 34 | 41 |
| `TRAINER_JACKSON_4` | Route119 | 6e → 7e badge | 37 | 45 |
| `TRAINER_JACKSON_5` | Route119 | 6e → 7e badge | 39 | 47 |
| `TRAINER_JEFFREY_3` | Route120 | 6e → 7e badge | 34 | 41 |
| `TRAINER_JEFFREY_4` | Route120 | 6e → 7e badge | 36 | 44 |
| `TRAINER_JEFFREY_5` | Route120 | 6e → 7e badge | 38 | 46 |
| `TRAINER_ROBERT_3` | Route120 | 6e → 7e badge | 35 | 43 |
| `TRAINER_ROBERT_4` | Route120 | 6e → 7e badge | 38 | 46 |
| `TRAINER_ROBERT_5` | Route120 | 6e → 7e badge | 41 | 50 |
| `TRAINER_CALE` | Route121 | 6e → 7e badge | 29 | 35 |
| `TRAINER_CRISTIN_1` | Route121 | 6e → 7e badge | 29 | 35 |
| `TRAINER_CRISTIN_2` | Route121 | 6e → 7e badge | 35 | 43 |
| `TRAINER_CRISTIN_3` | Route121 | 6e → 7e badge | 37 | 45 |
| `TRAINER_CRISTIN_4` | Route121 | 6e → 7e badge | 39 | 47 |
| `TRAINER_CRISTIN_5` | Route121 | 6e → 7e badge | 41 | 50 |
| `TRAINER_JESSICA_1` | Route121 | 6e → 7e badge | 29 | 35 |
| `TRAINER_JESSICA_2` | Route121 | 6e → 7e badge | 35 | 43 |
| `TRAINER_JESSICA_3` | Route121 | 6e → 7e badge | 38 | 46 |
| `TRAINER_JESSICA_4` | Route121 | 6e → 7e badge | 41 | 50 |
| `TRAINER_KATE_AND_JOY` | Route121 | 6e → 7e badge | 30-32 | 36-39 |
| `TRAINER_MARCEL` | Route121 | 6e → 7e badge | 29 | 35 |
| `TRAINER_MYLES` | Route121 | 6e → 7e badge | 25 | 30 |
| `TRAINER_PAT` | Route121 | 6e → 7e badge | 25 | 30 |
| `TRAINER_TAMMY` | Route121 | 6e → 7e badge | 29 | 35 |
| `TRAINER_VANESSA` | Route121 | 6e → 7e badge | 30 | 36 |
| `TRAINER_WALTER_1` | Route121 | 6e → 7e badge | 29 | 35 |
| `TRAINER_WALTER_2` | Route121 | 6e → 7e badge | 34 | 41 |
| `TRAINER_WALTER_3` | Route121 | 6e → 7e badge | 36 | 44 |
| `TRAINER_WALTER_4` | Route121 | 6e → 7e badge | 39 | 47 |
| `TRAINER_WALTER_5` | Route121 | 6e → 7e badge | 41 | 50 |
| `TRAINER_ALBERTO` | Route123 | 6e → 7e badge | 30 | 36 |
| `TRAINER_BRAXTON` | Route123 | 6e → 7e badge | 28 | 34 |
| `TRAINER_CAMERON_1` | Route123 | 6e → 7e badge | 31 | 38 |
| `TRAINER_CAMERON_2` | Route123 | 6e → 7e badge | 33 | 40 |
| `TRAINER_CAMERON_3` | Route123 | 6e → 7e badge | 38 | 46 |
| `TRAINER_CAMERON_4` | Route123 | 6e → 7e badge | 41 | 50 |
| `TRAINER_DAVIS` | Route123 | 6e → 7e badge | 27 | 33 |
| `TRAINER_ED` | Route123 | 6e → 7e badge | 30 | 36 |
| `TRAINER_FERNANDO_1` | Route123 | 6e → 7e badge | 30 | 36 |
| `TRAINER_FERNANDO_2` | Route123 | 6e → 7e badge | 35 | 43 |
| `TRAINER_FERNANDO_3` | Route123 | 6e → 7e badge | 37 | 45 |
| `TRAINER_FERNANDO_4` | Route123 | 6e → 7e badge | 39 | 47 |
| `TRAINER_FERNANDO_5` | Route123 | 6e → 7e badge | 41 | 50 |
| `TRAINER_FREDRICK` | Route123 | 6e → 7e badge | 30 | 36 |
| `TRAINER_JACKI_1` | Route123 | 6e → 7e badge | 30 | 36 |
| `TRAINER_JACKI_2` | Route123 | 6e → 7e badge | 34 | 41 |
| `TRAINER_JACKI_3` | Route123 | 6e → 7e badge | 37 | 45 |
| `TRAINER_JACKI_4` | Route123 | 6e → 7e badge | 40 | 49 |
| `TRAINER_JAZMYN` | Route123 | 6e → 7e badge | 27 | 33 |
| `TRAINER_JONAS` | Route123 | 6e → 7e badge | 31 | 38 |
| `TRAINER_KAYLEY` | Route123 | 6e → 7e badge | 31 | 38 |
| `TRAINER_KINDRA` | Route123 | 6e → 7e badge | 30 | 36 |
| `TRAINER_MIU_AND_YUKI` | Route123 | 6e → 7e badge | 26 | 32 |
| `TRAINER_VIOLET` | Route123 | 6e → 7e badge | 26 | 32 |
| `TRAINER_WENDY` | Route123 | 6e → 7e badge | 29 | 35 |
| `TRAINER_CHAD` | Route124 | 6e → 7e badge | 33 | 40 |
| `TRAINER_DECLAN` | Route124 | 6e → 7e badge | 34 | 41 |
| `TRAINER_GRACE` | Route124 | 6e → 7e badge | 34 | 41 |
| `TRAINER_ISABELLA` | Route124 | 6e → 7e badge | 34 | 41 |
| `TRAINER_JENNY_1` | Route124 | 6e → 7e badge | 34 | 41 |
| `TRAINER_JENNY_2` | Route124 | 6e → 7e badge | 38 | 46 |
| `TRAINER_JENNY_3` | Route124 | 6e → 7e badge | 41 | 50 |
| `TRAINER_LILA_AND_ROY_1` | Route124 | 6e → 7e badge | 33-34 | 40-41 |
| `TRAINER_LILA_AND_ROY_2` | Route124 | 6e → 7e badge | 40-42 | 49-51 |
| `TRAINER_ROLAND` | Route124 | 6e → 7e badge | 34 | 41 |
| `TRAINER_SPENCER` | Route124 | 6e → 7e badge | 33 | 40 |
| `TRAINER_AURON` | Route125 | 6e → 7e badge | 33 | 40 |
| `TRAINER_ERNEST_1` | Route125 | 6e → 7e badge | 33 | 40 |
| `TRAINER_ERNEST_2` | Route125 | 6e → 7e badge | 36 | 44 |
| `TRAINER_ERNEST_3` | Route125 | 6e → 7e badge | 39 | 47 |
| `TRAINER_ERNEST_4` | Route125 | 6e → 7e badge | 42 | 51 |
| `TRAINER_KIM_AND_IRIS` | Route125 | 6e → 7e badge | 32-35 | 39-43 |
| `TRAINER_NOLEN` | Route125 | 6e → 7e badge | 34 | 41 |
| `TRAINER_PRESLEY` | Route125 | 6e → 7e badge | 33 | 40 |
| `TRAINER_SHARON` | Route125 | 6e → 7e badge | 34 | 41 |
| `TRAINER_STAN` | Route125 | 6e → 7e badge | 34 | 41 |
| `TRAINER_TANYA` | Route125 | 6e → 7e badge | 34 | 41 |
| `TRAINER_BARRY` | Route126 | 6e → 7e badge | 34 | 41 |
| `TRAINER_BRENDA` | Route126 | 6e → 7e badge | 34 | 41 |
| `TRAINER_DEAN` | Route126 | 6e → 7e badge | 31 | 38 |
| `TRAINER_ISOBEL` | Route126 | 6e → 7e badge | 34 | 41 |
| `TRAINER_LEONARDO` | Route126 | 6e → 7e badge | 34 | 41 |
| `TRAINER_NIKKI` | Route126 | 6e → 7e badge | 33 | 40 |
| `TRAINER_PABLO_1` | Route126 | 6e → 7e badge | 33 | 40 |
| `TRAINER_PABLO_2` | Route126 | 6e → 7e badge | 37 | 45 |
| `TRAINER_PABLO_3` | Route126 | 6e → 7e badge | 39 | 47 |
| `TRAINER_PABLO_4` | Route126 | 6e → 7e badge | 41 | 50 |
| `TRAINER_SIENNA` | Route126 | 6e → 7e badge | 33 | 40 |
| `TRAINER_AIDAN` | Route127 | 6e → 7e badge | 32 | 39 |
| `TRAINER_ATHENA` | Route127 | 6e → 7e badge | 32 | 39 |
| `TRAINER_CAMDEN` | Route127 | 6e → 7e badge | 33 | 40 |
| `TRAINER_DONNY` | Route127 | 6e → 7e badge | 26-34 | 32-41 |
| `TRAINER_HENRY` | Route127 | 6e → 7e badge | 31-34 | 38-41 |
| `TRAINER_JONAH` | Route127 | 6e → 7e badge | 30-32 | 36-39 |
| `TRAINER_KOJI_1` | Route127 | 6e → 7e badge | 34 | 41 |
| `TRAINER_KOJI_2` | Route127 | 6e → 7e badge | 37 | 45 |
| `TRAINER_KOJI_3` | Route127 | 6e → 7e badge | 39 | 47 |
| `TRAINER_KOJI_4` | Route127 | 6e → 7e badge | 41 | 50 |
| `TRAINER_ROGER` | Route127 | 6e → 7e badge | 15-35 | 18-43 |
| `TRAINER_ALEXA` | Route128 | 6e → 7e badge | 34 | 41 |
| `TRAINER_CARLEE` | Route128 | 6e → 7e badge | 35 | 43 |
| `TRAINER_HARRISON` | Route128 | 6e → 7e badge | 35 | 43 |
| `TRAINER_ISAIAH_1` | Route128 | 6e → 7e badge | 35 | 43 |
| `TRAINER_ISAIAH_2` | Route128 | 6e → 7e badge | 39 | 47 |
| `TRAINER_ISAIAH_3` | Route128 | 6e → 7e badge | 42 | 51 |
| `TRAINER_KATELYN_1` | Route128 | 6e → 7e badge | 35 | 43 |
| `TRAINER_KATELYN_2` | Route128 | 6e → 7e badge | 39 | 47 |
| `TRAINER_KATELYN_3` | Route128 | 6e → 7e badge | 42 | 51 |
| `TRAINER_RUBEN` | Route128 | 6e → 7e badge | 34 | 41 |
| `TRAINER_WAYNE` | Route128 | 6e → 7e badge | 31-36 | 38-44 |
| `TRAINER_GRUNT_SPACE_CENTER_1` | MossdeepCity_SpaceCenter_1F | 7e → 8e badge | 32 | 41 |
| `TRAINER_GRUNT_SPACE_CENTER_2` | MossdeepCity_SpaceCenter_1F | 7e → 8e badge | 26-30 | 33-38 |
| `TRAINER_GRUNT_SPACE_CENTER_3` | MossdeepCity_SpaceCenter_1F | 7e → 8e badge | 31 | 40 |
| `TRAINER_GRUNT_SPACE_CENTER_4` | MossdeepCity_SpaceCenter_1F | 7e → 8e badge | 32 | 41 |
| `TRAINER_GRUNT_SPACE_CENTER_5` | MossdeepCity_SpaceCenter_2F | 7e → 8e badge | 32 | 41 |
| `TRAINER_GRUNT_SPACE_CENTER_6` | MossdeepCity_SpaceCenter_2F | 7e → 8e badge | 32 | 41 |
| `TRAINER_GRUNT_SPACE_CENTER_7` | MossdeepCity_SpaceCenter_2F | 7e → 8e badge | 32 | 41 |
| `TRAINER_KEIRA` | Route110_TrickHousePuzzle8 | 7e → 8e badge | 45 | 58 |
| `TRAINER_LEROY` | Route110_TrickHousePuzzle8 | 7e → 8e badge | 46 | 59 |
| `TRAINER_VINCENT` | Route110_TrickHousePuzzle8 | 7e → 8e badge | 44 | 56 |
| `TRAINER_JESSICA_5` | Route121 | 7e → 8e badge | 44 | 56 |
| `TRAINER_CAMERON_5` | Route123 | 7e → 8e badge | 45 | 58 |
| `TRAINER_JACKI_5` | Route123 | 7e → 8e badge | 43 | 55 |
| `TRAINER_JENNY_4` | Route124 | 7e → 8e badge | 43 | 55 |
| `TRAINER_JENNY_5` | Route124 | 7e → 8e badge | 45 | 58 |
| `TRAINER_LILA_AND_ROY_3` | Route124 | 7e → 8e badge | 43-45 | 55-58 |
| `TRAINER_ERNEST_5` | Route125 | 7e → 8e badge | 45 | 58 |
| `TRAINER_PABLO_5` | Route126 | 7e → 8e badge | 43 | 55 |
| `TRAINER_KOJI_5` | Route127 | 7e → 8e badge | 43 | 55 |
| `TRAINER_ISAIAH_4` | Route128 | 7e → 8e badge | 45 | 58 |
| `TRAINER_KATELYN_4` | Route128 | 7e → 8e badge | 45 | 58 |
| `TRAINER_ALLISON` | Route129 | 7e → 8e badge | 27-33 | 35-42 |
| `TRAINER_CHASE` | Route129 | 7e → 8e badge | 26-34 | 33-44 |
| `TRAINER_CLARENCE` | Route129 | 7e → 8e badge | 34 | 44 |
| `TRAINER_REED` | Route129 | 7e → 8e badge | 33 | 42 |
| `TRAINER_TISHA` | Route129 | 7e → 8e badge | 34 | 44 |
| `TRAINER_KATIE` | Route130 | 7e → 8e badge | 33 | 42 |
| `TRAINER_RODNEY` | Route130 | 7e → 8e badge | 34 | 44 |
| `TRAINER_SANTIAGO` | Route130 | 7e → 8e badge | 33 | 42 |
| `TRAINER_HERMAN` | Route131 | 7e → 8e badge | 33 | 42 |
| `TRAINER_KARA` | Route131 | 7e → 8e badge | 34 | 44 |
| `TRAINER_KEVIN` | Route131 | 7e → 8e badge | 34 | 44 |
| `TRAINER_RELI_AND_IAN` | Route131 | 7e → 8e badge | 33-35 | 42-45 |
| `TRAINER_RICHARD` | Route131 | 7e → 8e badge | 34 | 44 |
| `TRAINER_SUSIE` | Route131 | 7e → 8e badge | 34 | 44 |
| `TRAINER_TALIA` | Route131 | 7e → 8e badge | 34 | 44 |
| `TRAINER_DANA` | Route132 | 7e → 8e badge | 34 | 44 |
| `TRAINER_DARCY` | Route132 | 7e → 8e badge | 33 | 42 |
| `TRAINER_GILBERT` | Route132 | 7e → 8e badge | 34 | 44 |
| `TRAINER_JONATHAN` | Route132 | 7e → 8e badge | 33 | 42 |
| `TRAINER_KIYO` | Route132 | 7e → 8e badge | 34 | 44 |
| `TRAINER_MAKAYLA` | Route132 | 7e → 8e badge | 33 | 42 |
| `TRAINER_PAXTON` | Route132 | 7e → 8e badge | 33 | 42 |
| `TRAINER_RONALD` | Route132 | 7e → 8e badge | 19-35 | 24-45 |
| `TRAINER_BECK` | Route133 | 7e → 8e badge | 34 | 44 |
| `TRAINER_CONOR` | Route133 | 7e → 8e badge | 33 | 42 |
| `TRAINER_DEBRA` | Route133 | 7e → 8e badge | 34 | 44 |
| `TRAINER_FRANKLIN` | Route133 | 7e → 8e badge | 34 | 44 |
| `TRAINER_LINDA` | Route133 | 7e → 8e badge | 33 | 42 |
| `TRAINER_MOLLIE` | Route133 | 7e → 8e badge | 33 | 42 |
| `TRAINER_WARREN` | Route133 | 7e → 8e badge | 33 | 42 |
| `TRAINER_AARON` | Route134 | 7e → 8e badge | 34 | 44 |
| `TRAINER_ALEX` | Route134 | 7e → 8e badge | 33 | 42 |
| `TRAINER_HITOSHI` | Route134 | 7e → 8e badge | 32 | 41 |
| `TRAINER_HUDSON` | Route134 | 7e → 8e badge | 34 | 44 |
| `TRAINER_JACK` | Route134 | 7e → 8e badge | 34 | 44 |
| `TRAINER_KELVIN` | Route134 | 7e → 8e badge | 33 | 42 |
| `TRAINER_LAUREL` | Route134 | 7e → 8e badge | 33 | 42 |
| `TRAINER_MARLEY` | Route134 | 7e → 8e badge | 34 | 44 |
| `TRAINER_REYNA` | Route134 | 7e → 8e badge | 33 | 42 |
| `TRAINER_GRUNT_SEAFLOOR_CAVERN_1` | SeafloorCavern_Room1 | 7e → 8e badge | 36 | 46 |
| `TRAINER_GRUNT_SEAFLOOR_CAVERN_2` | SeafloorCavern_Room1 | 7e → 8e badge | 36 | 46 |
| `TRAINER_GRUNT_SEAFLOOR_CAVERN_5` | SeafloorCavern_Room3 | 7e → 8e badge | 35 | 45 |
| `TRAINER_GRUNT_SEAFLOOR_CAVERN_3` | SeafloorCavern_Room4 | 7e → 8e badge | 36 | 46 |
| `TRAINER_GRUNT_SEAFLOOR_CAVERN_4` | SeafloorCavern_Room4 | 7e → 8e badge | 36 | 46 |
| `TRAINER_ANDREA` | SootopolisCity_Gym_B1F | 7e → 8e badge | 40 | 51 |
| `TRAINER_ANNIKA` | SootopolisCity_Gym_B1F | 7e → 8e badge | 39 | 50 |
| `TRAINER_BETHANY` | SootopolisCity_Gym_B1F | 7e → 8e badge | 35-39 | 45-50 |
| `TRAINER_BRIANNA` | SootopolisCity_Gym_B1F | 7e → 8e badge | 40 | 51 |
| `TRAINER_BRIDGET` | SootopolisCity_Gym_B1F | 7e → 8e badge | 40 | 51 |
| `TRAINER_CONNIE` | SootopolisCity_Gym_B1F | 7e → 8e badge | 40 | 51 |
| `TRAINER_CRISSY` | SootopolisCity_Gym_B1F | 7e → 8e badge | 39 | 50 |
| `TRAINER_DAPHNE` | SootopolisCity_Gym_B1F | 7e → 8e badge | 39 | 50 |
| `TRAINER_OLIVIA` | SootopolisCity_Gym_B1F | 7e → 8e badge | 35-39 | 45-50 |
| `TRAINER_TIFFANY` | SootopolisCity_Gym_B1F | 7e → 8e badge | 39 | 50 |
| `TRAINER_JOHN_AND_JAY_1` | MeteorFalls_1F_2R | Route Victoire | 39 | 55 |
| `TRAINER_JOHN_AND_JAY_2` | MeteorFalls_1F_2R | Route Victoire | 43 | 60 |
| `TRAINER_JOHN_AND_JAY_3` | MeteorFalls_1F_2R | Route Victoire | 46 | 64 |
| `TRAINER_JOHN_AND_JAY_4` | MeteorFalls_1F_2R | Route Victoire | 49 | 69 |
| `TRAINER_JOHN_AND_JAY_5` | MeteorFalls_1F_2R | Route Victoire | 52 | 73 |
| `TRAINER_NICOLAS_1` | MeteorFalls_1F_2R | Route Victoire | 37 | 52 |
| `TRAINER_NICOLAS_2` | MeteorFalls_1F_2R | Route Victoire | 41 | 57 |
| `TRAINER_NICOLAS_3` | MeteorFalls_1F_2R | Route Victoire | 44 | 62 |
| `TRAINER_NICOLAS_4` | MeteorFalls_1F_2R | Route Victoire | 46 | 64 |
| `TRAINER_NICOLAS_5` | MeteorFalls_1F_2R | Route Victoire | 49 | 69 |
| `TRAINER_LILA_AND_ROY_4` | Route124 | Route Victoire | 46-48 | 64-67 |
| `TRAINER_LILA_AND_ROY_5` | Route124 | Route Victoire | 49-51 | 69-71 |
| `TRAINER_ISAIAH_5` | Route128 | Route Victoire | 48 | 67 |
| `TRAINER_KATELYN_5` | Route128 | Route Victoire | 48 | 67 |
| `TRAINER_ALBERT` | VictoryRoad_1F | Route Victoire | 43 | 60 |
| `TRAINER_EDGAR` | VictoryRoad_1F | Route Victoire | 43 | 60 |
| `TRAINER_HOPE` | VictoryRoad_1F | Route Victoire | 45 | 63 |
| `TRAINER_KATELYNN` | VictoryRoad_1F | Route Victoire | 43 | 60 |
| `TRAINER_QUINCY` | VictoryRoad_1F | Route Victoire | 43 | 60 |
| `TRAINER_HALLE` | VictoryRoad_B1F | Route Victoire | 43 | 60 |
| `TRAINER_MICHELLE` | VictoryRoad_B1F | Route Victoire | 42 | 59 |
| `TRAINER_MITCHELL` | VictoryRoad_B1F | Route Victoire | 43 | 60 |
| `TRAINER_SAMUEL` | VictoryRoad_B1F | Route Victoire | 42 | 59 |
| `TRAINER_SHANNON` | VictoryRoad_B1F | Route Victoire | 45 | 63 |
| `TRAINER_CAROLINE` | VictoryRoad_B2F | Route Victoire | 43 | 60 |
| `TRAINER_DIANNE` | VictoryRoad_B2F | Route Victoire | 43 | 60 |
| `TRAINER_FELIX` | VictoryRoad_B2F | Route Victoire | 43 | 60 |
| `TRAINER_JULIE` | VictoryRoad_B2F | Route Victoire | 42 | 59 |
| `TRAINER_OWEN` | VictoryRoad_B2F | Route Victoire | 42 | 59 |
| `TRAINER_VITO` | VictoryRoad_B2F | Route Victoire | 42 | 59 |

## Pokémon sauvages

| Map | Table | Zone | Avant | Après |
|---|---|---|---|---|
| Route101 | `gRoute101` | herbes | 2-3 | 2-3 |
| Route101 | `gRoute101_Night` | herbes | 2-3 | 2-3 |
| Route102 | `gRoute102` | herbes | 3-4 | 3-4 |
| Route102 | `gRoute102` | Surf | 5-35 | 6-43 |
| Route102 | `gRoute102` | pêche | 5-45 | 5-55 |
| Route102 | `gRoute102_Night` | herbes | 3-4 | 3-4 |
| Route103 | `gRoute103` | herbes | 2-4 | 2-4 |
| Route103 | `gRoute103` | Surf | 5-35 | 6-43 |
| Route103 | `gRoute103` | pêche | 5-45 | 5-55 |
| Route104 | `gRoute104` | herbes | 3-5 | 3-5 |
| Route104 | `gRoute104` | Surf | 10-30 | 12-37 |
| Route104 | `gRoute104` | pêche | 5-45 | 5-55 |
| Route104 | `gRoute104_Night` | herbes | 3-5 | 3-5 |
| Route105 | `gRoute105` | Surf | 5-35 | 6-43 |
| Route105 | `gRoute105` | pêche | 5-45 | 6-55 |
| Route110 | `gRoute110` | herbes | 12-13 | 14-15 |
| Route110 | `gRoute110` | Surf | 5-35 | 6-43 |
| Route110 | `gRoute110` | pêche | 5-45 | 6-55 |
| Route111 | `gRoute111` | herbes | 19-22 | 21-25 |
| Route111 | `gRoute111` | Surf | 5-35 | 6-43 |
| Route111 | `gRoute111` | Éclate-Roc | 5-20 | 6-23 |
| Route111 | `gRoute111` | pêche | 5-45 | 6-55 |
| Route112 | `gRoute112` | herbes | 14-16 | 16-19 |
| Route113 | `gRoute113` | herbes | 14-16 | 16-19 |
| Route114 | `gRoute114` | herbes | 15-18 | 18-21 |
| Route114 | `gRoute114` | Surf | 5-35 | 6-43 |
| Route114 | `gRoute114` | Éclate-Roc | 5-20 | 6-23 |
| Route114 | `gRoute114` | pêche | 5-45 | 6-55 |
| Route114 | `gRoute114_Night` | herbes | 15-18 | 18-21 |
| Route116 | `gRoute116` | herbes | 6-8 | 6-9 |
| Route117 | `gRoute117` | herbes | 13-14 | 15-16 |
| Route117 | `gRoute117` | Surf | 5-35 | 6-43 |
| Route117 | `gRoute117` | pêche | 5-45 | 6-55 |
| Route118 | `gRoute118` | herbes | 24-27 | 30-34 |
| Route118 | `gRoute118` | Surf | 5-35 | 6-43 |
| Route118 | `gRoute118` | pêche | 5-45 | 6-55 |
| Route124 | `gRoute124` | Surf | 5-35 | 6-43 |
| Route124 | `gRoute124` | pêche | 5-45 | 6-55 |
| PetalburgWoods | `gPetalburgWoods` | herbes | 5-6 | 5-6 |
| RusturfTunnel | `gRusturfTunnel` | herbes | 5-8 | 5-8 |
| GraniteCave_1F | `gGraniteCave_1F` | herbes | 6-10 | 6-11 |
| GraniteCave_B1F | `gGraniteCave_B1F` | herbes | 9-11 | 9-12 |
| MtPyre_1F | `gMtPyre_1F` | herbes | 22-29 | 27-35 |
| VictoryRoad_1F | `gVictoryRoad_1F` | herbes | 36-40 | 50-56 |
| Underwater_Route126 | `gUnderwater_Route126` | Surf | 20-35 | 26-45 |
| AbandonedShip_Rooms_B1F | `gAbandonedShip_Rooms_B1F` | Surf | 5-35 | 6-43 |
| AbandonedShip_Rooms_B1F | `gAbandonedShip_Rooms_B1F` | pêche | 5-35 | 6-43 |
| GraniteCave_B2F | `gGraniteCave_B2F` | herbes | 10-12 | 11-13 |
| GraniteCave_B2F | `gGraniteCave_B2F` | Éclate-Roc | 5-20 | 6-23 |
| FieryPath | `gFieryPath` | herbes | 14-16 | 16-19 |
| MeteorFalls_B1F_2R | `gMeteorFalls_B1F_2R` | herbes | 25-40 | 35-56 |
| MeteorFalls_B1F_2R | `gMeteorFalls_B1F_2R` | Surf | 5-35 | 7-49 |
| MeteorFalls_B1F_2R | `gMeteorFalls_B1F_2R` | pêche | 5-45 | 7-63 |
| MeteorFalls_B1F_2R | `gMeteorFalls_B1F_2R_Night` | herbes | 25-40 | 35-56 |
| MeteorFalls_B1F_2R | `gMeteorFalls_B1F_2R_Night` | Surf | 5-35 | 7-49 |
| JaggedPass | `gJaggedPass` | herbes | 20-22 | 23-26 |
| Route106 | `gRoute106` | Surf | 5-35 | 6-43 |
| Route106 | `gRoute106` | pêche | 5-45 | 5-55 |
| Route107 | `gRoute107` | Surf | 5-35 | 6-43 |
| Route107 | `gRoute107` | pêche | 5-45 | 6-55 |
| Route108 | `gRoute108` | Surf | 5-35 | 6-43 |
| Route108 | `gRoute108` | pêche | 5-45 | 6-55 |
| Route109 | `gRoute109` | Surf | 5-35 | 6-43 |
| Route109 | `gRoute109` | pêche | 5-45 | 6-55 |
| Route115 | `gRoute115` | herbes | 23-26 | 27-30 |
| Route115 | `gRoute115` | Surf | 5-35 | 6-43 |
| Route115 | `gRoute115` | pêche | 5-45 | 6-55 |
| NewMauville_Inside | `gNewMauville_Inside` | herbes | 22-26 | 27-32 |
| Route119 | `gRoute119` | herbes | 24-27 | 30-34 |
| Route119 | `gRoute119` | Surf | 5-35 | 6-43 |
| Route119 | `gRoute119` | pêche | 5-45 | 6-55 |
| Route120 | `gRoute120` | herbes | 25-27 | 31-34 |
| Route120 | `gRoute120` | Surf | 5-35 | 6-43 |
| Route120 | `gRoute120` | pêche | 5-45 | 6-55 |
| ScorchedSlab | `gScorchedSlab` | herbes | 25-27 | 31-34 |
| Route121 | `gRoute121` | herbes | 25-28 | 30-34 |
| Route121 | `gRoute121` | Surf | 5-35 | 6-43 |
| Route121 | `gRoute121` | pêche | 5-45 | 6-55 |
| Route122 | `gRoute122` | Surf | 5-35 | 6-43 |
| Route122 | `gRoute122` | pêche | 5-45 | 6-55 |
| Route123 | `gRoute123` | herbes | 25-28 | 30-34 |
| Route123 | `gRoute123` | Surf | 5-35 | 6-43 |
| Route123 | `gRoute123` | pêche | 5-45 | 6-55 |
| MtPyre_2F | `gMtPyre_2F` | herbes | 22-29 | 27-35 |
| MtPyre_3F | `gMtPyre_3F` | herbes | 22-29 | 27-35 |
| MtPyre_4F | `gMtPyre_4F` | herbes | 22-29 | 27-35 |
| MtPyre_5F | `gMtPyre_5F` | herbes | 22-29 | 27-35 |
| MtPyre_6F | `gMtPyre_6F` | herbes | 22-29 | 27-35 |
| MtPyre_Exterior | `gMtPyre_Exterior` | herbes | 25-29 | 30-35 |
| MtPyre_Summit | `gMtPyre_Summit` | herbes | 24-30 | 29-36 |
| GraniteCave_StevensRoom | `gGraniteCave_StevensRoom` | herbes | 6-10 | 6-11 |
| Route125 | `gRoute125` | Surf | 5-35 | 6-43 |
| Route125 | `gRoute125` | pêche | 5-45 | 6-55 |
| Route126 | `gRoute126` | Surf | 5-35 | 6-43 |
| Route126 | `gRoute126` | pêche | 5-45 | 6-55 |
| Route127 | `gRoute127` | Surf | 5-35 | 6-43 |
| Route127 | `gRoute127` | pêche | 5-45 | 6-55 |
| Route128 | `gRoute128` | Surf | 5-35 | 6-43 |
| Route128 | `gRoute128` | pêche | 5-45 | 6-55 |
| Route129 | `gRoute129` | Surf | 5-35 | 6-45 |
| Route129 | `gRoute129` | pêche | 5-45 | 6-58 |
| Route130 | `gRoute130` | herbes | 5-50 | 6-64 |
| Route130 | `gRoute130` | Surf | 5-35 | 6-45 |
| Route130 | `gRoute130` | pêche | 5-45 | 6-58 |
| Route131 | `gRoute131` | Surf | 5-35 | 6-45 |
| Route131 | `gRoute131` | pêche | 5-45 | 6-58 |
| Route132 | `gRoute132` | Surf | 5-35 | 6-45 |
| Route132 | `gRoute132` | pêche | 5-45 | 6-58 |
| Route133 | `gRoute133` | Surf | 5-35 | 6-45 |
| Route133 | `gRoute133` | pêche | 5-45 | 6-58 |
| Route134 | `gRoute134` | Surf | 5-35 | 6-45 |
| Route134 | `gRoute134` | pêche | 5-45 | 6-58 |
| AbandonedShip_HiddenFloorCorridors | `gAbandonedShip_HiddenFloorCorridors` | Surf | 5-35 | 6-43 |
| AbandonedShip_HiddenFloorCorridors | `gAbandonedShip_HiddenFloorCorridors` | pêche | 5-35 | 6-43 |
| SeafloorCavern_Room1 | `gSeafloorCavern_Room1` | herbes | 28-36 | 36-46 |
| SeafloorCavern_Room2 | `gSeafloorCavern_Room2` | herbes | 28-36 | 36-46 |
| SeafloorCavern_Room3 | `gSeafloorCavern_Room3` | herbes | 28-36 | 36-46 |
| SeafloorCavern_Room4 | `gSeafloorCavern_Room4` | herbes | 28-36 | 36-46 |
| SeafloorCavern_Room5 | `gSeafloorCavern_Room5` | herbes | 28-36 | 36-46 |
| SeafloorCavern_Room6 | `gSeafloorCavern_Room6` | herbes | 28-36 | 36-46 |
| SeafloorCavern_Room6 | `gSeafloorCavern_Room6` | Surf | 5-35 | 6-45 |
| SeafloorCavern_Room6 | `gSeafloorCavern_Room6` | pêche | 5-45 | 6-58 |
| SeafloorCavern_Room7 | `gSeafloorCavern_Room7` | herbes | 28-36 | 36-46 |
| SeafloorCavern_Room7 | `gSeafloorCavern_Room7` | Surf | 5-35 | 6-45 |
| SeafloorCavern_Room7 | `gSeafloorCavern_Room7` | pêche | 5-45 | 6-58 |
| SeafloorCavern_Room8 | `gSeafloorCavern_Room8` | herbes | 28-36 | 36-46 |
| SeafloorCavern_Entrance | `gSeafloorCavern_Entrance` | Surf | 5-35 | 6-45 |
| SeafloorCavern_Entrance | `gSeafloorCavern_Entrance` | pêche | 5-45 | 6-58 |
| CaveOfOrigin_Entrance | `gCaveOfOrigin_Entrance` | herbes | 28-36 | 36-46 |
| CaveOfOrigin_1F | `gCaveOfOrigin_1F` | herbes | 30-36 | 38-46 |
| CaveOfOrigin_UnusedRubySapphireMap1 | `gCaveOfOrigin_UnusedRubySapphireMap1` | herbes | 30-36 | 38-46 |
| CaveOfOrigin_UnusedRubySapphireMap2 | `gCaveOfOrigin_UnusedRubySapphireMap2` | herbes | 30-36 | 38-46 |
| CaveOfOrigin_UnusedRubySapphireMap3 | `gCaveOfOrigin_UnusedRubySapphireMap3` | herbes | 30-36 | 38-46 |
| NewMauville_Entrance | `gNewMauville_Entrance` | herbes | 22-26 | 27-32 |
| VictoryRoad_B1F | `gVictoryRoad_B1F` | herbes | 38-42 | 53-59 |
| VictoryRoad_B1F | `gVictoryRoad_B1F` | Éclate-Roc | 30-40 | 42-56 |
| VictoryRoad_B2F | `gVictoryRoad_B2F` | herbes | 40-44 | 56-62 |
| VictoryRoad_B2F | `gVictoryRoad_B2F` | Surf | 25-40 | 35-56 |
| VictoryRoad_B2F | `gVictoryRoad_B2F` | pêche | 5-45 | 7-63 |
| MeteorFalls_1F_1R | `gMeteorFalls_1F_1R` | herbes | 14-20 | 16-23 |
| MeteorFalls_1F_1R | `gMeteorFalls_1F_1R` | Surf | 5-35 | 6-43 |
| MeteorFalls_1F_1R | `gMeteorFalls_1F_1R` | pêche | 5-45 | 6-55 |
| MeteorFalls_1F_1R | `gMeteorFalls_1F_1R_Night` | herbes | 14-20 | 16-23 |
| MeteorFalls_1F_1R | `gMeteorFalls_1F_1R_Night` | Surf | 5-35 | 6-43 |
| MeteorFalls_1F_2R | `gMeteorFalls_1F_2R` | herbes | 33-40 | 46-56 |
| MeteorFalls_1F_2R | `gMeteorFalls_1F_2R` | Surf | 5-35 | 7-49 |
| MeteorFalls_1F_2R | `gMeteorFalls_1F_2R` | pêche | 5-45 | 7-63 |
| MeteorFalls_1F_2R | `gMeteorFalls_1F_2R_Night` | herbes | 33-40 | 46-56 |
| MeteorFalls_1F_2R | `gMeteorFalls_1F_2R_Night` | Surf | 5-35 | 7-49 |
| MeteorFalls_B1F_1R | `gMeteorFalls_B1F_1R` | herbes | 33-40 | 46-56 |
| MeteorFalls_B1F_1R | `gMeteorFalls_B1F_1R` | Surf | 5-35 | 7-49 |
| MeteorFalls_B1F_1R | `gMeteorFalls_B1F_1R` | pêche | 5-45 | 7-63 |
| MeteorFalls_B1F_1R | `gMeteorFalls_B1F_1R_Night` | herbes | 33-40 | 46-56 |
| MeteorFalls_B1F_1R | `gMeteorFalls_B1F_1R_Night` | Surf | 5-35 | 7-49 |
| ShoalCave_LowTideStairsRoom | `gShoalCave_LowTideStairsRoom` | herbes | 26-32 | 32-39 |
| ShoalCave_LowTideLowerRoom | `gShoalCave_LowTideLowerRoom` | herbes | 26-32 | 32-39 |
| ShoalCave_LowTideInnerRoom | `gShoalCave_LowTideInnerRoom` | herbes | 26-32 | 32-39 |
| ShoalCave_LowTideInnerRoom | `gShoalCave_LowTideInnerRoom` | Surf | 5-35 | 6-43 |
| ShoalCave_LowTideInnerRoom | `gShoalCave_LowTideInnerRoom` | pêche | 5-45 | 6-55 |
| ShoalCave_LowTideEntranceRoom | `gShoalCave_LowTideEntranceRoom` | herbes | 26-32 | 32-39 |
| ShoalCave_LowTideEntranceRoom | `gShoalCave_LowTideEntranceRoom` | Surf | 5-35 | 6-43 |
| ShoalCave_LowTideEntranceRoom | `gShoalCave_LowTideEntranceRoom` | pêche | 5-45 | 6-55 |
| LilycoveCity | `gLilycoveCity` | Surf | 5-35 | 6-43 |
| LilycoveCity | `gLilycoveCity` | pêche | 5-45 | 6-55 |
| DewfordTown | `gDewfordTown` | Surf | 5-35 | 6-43 |
| DewfordTown | `gDewfordTown` | pêche | 5-45 | 5-55 |
| SlateportCity | `gSlateportCity` | Surf | 5-35 | 6-43 |
| SlateportCity | `gSlateportCity` | pêche | 5-45 | 6-55 |
| MossdeepCity | `gMossdeepCity` | Surf | 5-35 | 6-43 |
| MossdeepCity | `gMossdeepCity` | pêche | 5-45 | 6-55 |
| PacifidlogTown | `gPacifidlogTown` | Surf | 5-35 | 6-45 |
| PacifidlogTown | `gPacifidlogTown` | pêche | 5-45 | 6-58 |
| EverGrandeCity | `gEverGrandeCity` | Surf | 5-35 | 7-49 |
| EverGrandeCity | `gEverGrandeCity` | pêche | 5-45 | 7-63 |
| PetalburgCity | `gPetalburgCity` | Surf | 5-35 | 6-43 |
| PetalburgCity | `gPetalburgCity` | pêche | 5-45 | 5-55 |
| Underwater_Route124 | `gUnderwater_Route124` | Surf | 20-35 | 26-45 |
| ShoalCave_LowTideIceRoom | `gShoalCave_LowTideIceRoom` | herbes | 26-32 | 32-39 |
| SkyPillar_1F | `gSkyPillar_1F` | herbes | 33-38 | 42-49 |
| SootopolisCity | `gSootopolisCity` | Surf | 5-35 | 6-45 |
| SootopolisCity | `gSootopolisCity` | pêche | 5-45 | 6-58 |
| SkyPillar_3F | `gSkyPillar_3F` | herbes | 33-38 | 42-49 |
| SkyPillar_5F | `gSkyPillar_5F` | herbes | 33-39 | 42-50 |
| MagmaHideout_1F | `gMagmaHideout_1F` | herbes | 27-33 | 33-40 |
| MagmaHideout_2F_1R | `gMagmaHideout_2F_1R` | herbes | 27-33 | 33-40 |
| MagmaHideout_2F_2R | `gMagmaHideout_2F_2R` | herbes | 27-33 | 33-40 |
| MagmaHideout_3F_1R | `gMagmaHideout_3F_1R` | herbes | 27-33 | 33-40 |
| MagmaHideout_3F_2R | `gMagmaHideout_3F_2R` | herbes | 27-33 | 33-40 |
| MagmaHideout_4F | `gMagmaHideout_4F` | herbes | 27-33 | 33-40 |
| MagmaHideout_3F_3R | `gMagmaHideout_3F_3R` | herbes | 27-33 | 33-40 |
| MagmaHideout_2F_3R | `gMagmaHideout_2F_3R` | herbes | 27-33 | 33-40 |
| MirageTower_1F | `gMirageTower_1F` | herbes | 20-24 | 23-27 |
| MirageTower_2F | `gMirageTower_2F` | herbes | 20-24 | 23-27 |
| MirageTower_3F | `gMirageTower_3F` | herbes | 20-24 | 23-27 |
| MirageTower_4F | `gMirageTower_4F` | herbes | 20-24 | 23-27 |
