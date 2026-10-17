# État du projet — Pokémon Nabla (au 2026-10-17, soir)

Point de reprise pour une nouvelle session. À lire en premier, puis `CLAUDE.md` (règles), `ROADMAP.md` (plan) et `PROGRESS.md` (journal détaillé et décisions).

## En une phrase
Romhack d'Émeraude sur pokeemerald-expansion 1.17.2 (RHH). Phases 0 à 3 terminées. Phase 4 en cours : **4.1b-2 (déblocage des régions du Safari + 7 régions + évolutions régionales) livrée, en attente du test de l'utilisateur ; prochaine étape 4.1b-3 (zones spéciales du Safari après la Ligue)**, à présenter avant de commencer.

## Méthode de travail (rappel des règles clés)
- Communication en français, recommandations franches. Code et commits en anglais.
- **Avant chaque étape : présenter le plan (quoi, où, comment on vérifie) et attendre le feu vert.**
- Un commit par étape (ou par sujet), build vert, `git push origin master`. Mettre à jour `PROGRESS.md`.
- Décision non couverte par VISION.md / PROGRESS.md → demander.
- L'utilisateur teste sur `pokeemerald.gba` (build debug, menu debug R+START, quickstart SELECT) avec mGBA ; sa sauvegarde est `pokeemerald.sav` à la racine (jamais commitée).

## Environnement
- `export DEVKITPRO=/opt/devkitpro DEVKITARM=/opt/devkitpro/devkitARM` avant `make -j$(sysctl -n hw.ncpu)`.
- `make check` (~8 min) après tout changement de config ou de code de combat. Référence actuelle : **0 FAIL**, 5382 réussis, 33 `ASSUMPTION_FAIL` (tests qui supposent la Grêle, normal), 18 known failing, 9 expect failing, 421 TO_DO.
- Patch BPS : `./make_bps.sh` (ROM propre `../rom/emerald_us.gba`, Flips `../tools/flips`).
- `test/save.c` : garde-fou des tailles de sauvegarde (SaveBlock1 = 14916 dans le build de test).

## Ce qui est fait
| Phase | Contenu |
|---|---|
| 0 | Docs, patch BPS, README + crédits RHH, intro RHH retirée |
| 1 | Combat moderne (Gelure, Neige, pas d'affection, types affichés) ; QoL (CT réutilisables, Multi Exp Gen 6, IV/EV chiffrés, texte MID/FAST/INSTANT) ; doubles sauvages 8 % ; jour/nuit + éclairages nocturnes ; évolutions dans le résumé (START sur la page INFO) |
| 2 | Menu de début de partie dans le camion (difficulté Normal/Difficile, level caps on/off) ; level caps durs par badge (`src/caps.c`) ; évolutions par échange (Fil de Liaison 4 000 ₽, vendeur d'objets d'évolution à Nénucrique 3ᵉ) ; style de combat SHIFT/SET/BLIND ; messages de level cap ; sac agrandi + défilement haut/bas |
| 3 | Suiveurs ; CS utilisables si possédées (sans les apprendre) ; course automatique (menu Options défilant) ; objets de progression (27 objets cachés, boutiques à paliers de badges communes à toutes les Boutiques) ; événement Latios façon ROSA (scène d'origine de Steven Route 118 → Île du Sud, combat en duo, Latios + Méga-Bracelet) ; Méga-Gemmes (objet rare des sauvages, 17 au sol, Steven donne celle du starter Route 120, vendeur de 65 gemmes à 5 000 ₽ à Nénucrique 4ᵉ) |
| 4.1a | Jour/nuit 12 h / 12 h (horaires Soleil/Lune) + rencontres selon l'heure activées (tables `_Night` possibles, repli sur la table normale) |
| 4.1b-1 | Safari moderne : entrée gratuite, vrais combats, pas de limite de pas ; tables par région ; niveaux selon badges ; évolution dynamique ; Kanto (71 Pokémon) |
| 4.1b-2 | Comptoir : choix parmi les régions ouvertes + déblocage à 30 000 ₽ (n'importe quel ordre, on reste dans la liste d'achat, B = retour) ; 7 régions générées ; évolutions régionales selon la région du Safari (Raichu d'Alola, Typhlosion de Hisui…) ; générateur corrigé (macros d'expansion, variété minimale, aquatiques non-Eau dans l'eau) |

## En attente côté utilisateur
- Tester le Safari (4.1b-1 + 4.1b-2) : comptoir (refus sans argent, achat, plusieurs achats d'affilée, B), entrée dans une région débloquée, persistance après sauvegarde ; évolution régionale (Pikachu + Pierre Foudre dans le Safari Alola).
- Relire la répartition des 8 régions dans `docs/nabla/safari.md`.
- Retouches des routes sauvages (4.1d) : il les fera lui-même dans Porymap (onglet Wild Pokémon) ou par listes.

## Prochaine étape : 4.1b-3 (à présenter, feu vert à obtenir)
- Zones spéciales du Safari, débloquables **après la Ligue** (`FLAG_SYS_GAME_CLEAR`) à **100 000 ₽** chacune : Starters (27 lignées, **tous au niveau 5**), Zone Zéro (Paradoxes), Ultra-Espace (Ultra-Chimères).
- À faire : 3 entrées dans `sSafariZoneRegions` (`src/nabla_safari_zone.c`) avec flag + prix + condition post-Ligue ; générer `Starters`, `Paradox`, `UltraBeasts` (dans cet ordre) ; niveau fixe 5 pour les Starters dans `GetSafariZoneRegionWildLevel` ; textes du prix.
- Ensuite : 4.1c outil de couverture (dont objets d'évolution introuvables, ex. Bloc de Tourbe) ; 4.1d routes ; 4.2 équipes Normal/Difficile ; 4.3 calibrage ; phases 5 à 8 (voir ROADMAP).

## Repères techniques
- **Safari** : `VAR_NABLA_SAFARI_REGION` (0x4083) ; constantes `NABLA_SAFARI_REGION_*`, prix et ids de menu (`include/constants/nabla.h`) ; `src/nabla_safari_zone.c` (table `sSafariZoneRegions` : nom, flag, régions d'évolution ; specials du comptoir ; `IsPlayerInEvolutionRegion` appelé par `IF_REGION`/`IF_NOT_REGION` dans `src/pokemon.c`) ; dans `src/wild_encounter.c`, `GetCurrentMapWildMonHeaderId` saute à la table de la région (tables placées juste après celle d'origine de chaque zone, comme la Grotte Altérée) ; niveaux `GetSafariZoneRegionWildLevel` ; évolution `CreateSafariZoneRegionWildMon`. Scripts : `data/scripts/nabla/safari_zone.inc` (menus du comptoir), entrée `Route121_SafariZoneEntrance`, sortie `SafariZone_South`. Test : `test/nabla_safari_zone.c` (`make check TESTS="Nabla"`).
- **Flags Nabla** : `FLAG_NABLA_EXP_SHARE` 0x20, `FLAG_NABLA_LEVEL_CAPS` 0x21, régions du Safari 0x22-0x28 (Johto → Paldea), objets cachés 0x264-0x27E, Méga-Gemmes au sol 0x280 et 0x286-0x295, événement Latios 0x281-0x285. **Vars** : `VAR_NABLA_DIFFICULTY` 0x404E, `VAR_NABLA_SAFARI_REGION` 0x4083.
- **Dresseurs ajoutés** : `TRAINER_NABLA_MATT_SOUTHERN_ISLAND` 855, `TRAINER_NABLA_GRUNT_SOUTHERN_ISLAND` 856 ; partenaire `PARTNER_STEVEN_SOUTHERN_ISLAND` 2.
- **Outils** (`dev_scripts/nabla/`) : `hidden_item_spots.py` (cases valides pour un objet), `list_items.py` (tableaux de `docs/nabla/items.md`), `safari_tables.py` (tables du Safari + `docs/nabla/safari.md`).
- **Docs de référence** : `docs/nabla/items.md` (tous les objets ajoutés, boutiques, Méga-Gemmes), `docs/nabla/safari.md`.
- **Correctif d'expansion à proposer en amont** : `AreMultiPartiesFullTeams` (`src/battle_util.c`) lisait les drapeaux du combat précédent → sélection d'équipe ignorée dans les combats en duo scriptés.
- **Fichiers d'expansion modifiés** (attention aux merges upstream ; `pokedex_plus_hgss.c` le plus risqué) : `src/{battle_message,battle_script_commands,battle_util,caps,field_move,field_player_avatar,item_menu,new_game,option_menu,party_menu,pokedex_plus_hgss,pokemon,pokemon_summary_screen,scrcmd,shop_criteria,strings,wild_encounter}.c`, `data/specials.inc`, `src/data/{items.h,trainers.party,battle_partners.party,wild_encounters.json}`, `src/data/pokemon/species_info/gen_*_families.h`, `include/{global.h,field_move.h,pokedex_plus_hgss.h,strings.h}`, `include/constants/{flags,vars,global,opponents,battle_partner,battle_string_ids}.h`, `include/config/*.h`, nombreuses maps et scripts (`data/maps/*`, `data/scripts/players_house.inc`, `data/battle_scripts_1.s`).

## Pièges déjà rencontrés (et règles qui en découlent, dans CLAUDE.md)
- **Ne jamais réattribuer un flag/var Nabla libéré** : la sauvegarde de test de l'utilisateur peut l'avoir posé (cas de la Gardevoirite invisible).
- **Objets de map ajoutés en fin de liste uniquement** : la sauvegarde garde la liste d'objets de la map courante ; changer l'ordre casse `addobject` (cas de Latios invisible).
- Placement d'objets : passer par `hidden_item_spots.py` (évite ponts, cases isolées, voisins d'objets).
- Édition de la sauvegarde de l'utilisateur : faisable (format Gen 3, sommes de contrôle). Les offsets de SaveBlock1 se calculent en compilant un petit fichier C avec `offsetof` (toolchain devkitARM, `-iquote include -DMODERN=1 -DTESTING=0 -DEMERALD`) ; toujours faire une copie de sauvegarde d'abord et vérifier qu'aucun émulateur n'est ouvert.
- Copies de sauvegarde de l'utilisateur hors repo : `../pokeemerald_backup_before_latios_edit.sav`, `../pokeemerald_backup_before_gardevoirite_fix.sav`.
