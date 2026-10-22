# État du projet — Pokémon Nabla (au 2026-10-18)

Point de reprise pour une nouvelle session. À lire en premier, puis `CLAUDE.md` (règles), `ROADMAP.md` (plan) et `PROGRESS.md` (journal détaillé et décisions).

## En une phrase
Romhack d'Émeraude sur pokeemerald-expansion 1.17.2 (RHH). Phases 0 à 3 terminées. Phase 4 en cours : **4.2c (rival et Timmy) : fiche prête, en attente des équipes de l'utilisateur**, à présenter avant de commencer.

## Méthode de travail (rappel des règles clés)
- Communication en français, recommandations franches. Code et commits en anglais.
- **Avant chaque étape : présenter le plan (quoi, où, comment on vérifie) et attendre le feu vert.**
- Un commit par étape (ou par sujet), build vert, `git push origin master`. Mettre à jour `PROGRESS.md`.
- Décision non couverte par VISION.md / PROGRESS.md → demander.
- L'utilisateur teste sur `pokeemerald.gba` (build debug, menu debug R+START, quickstart SELECT) avec mGBA ; sa sauvegarde est `pokeemerald.sav` à la racine (jamais commitée).
- L'utilisateur a Porymap 6.3.1 : il doit le **fermer** pendant que Claude modifie le projet (sinon un enregistrement écrase les changements), et le rouvrir ensuite.

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
| 4.1b-3 | Après la Ligue, à 100 000 ₽ : STARTER ZONE (27 starters, niveau 5), AREA ZERO (20 Paradoxes), ULTRA SPACE (10 Ultra-Chimères) ; Beast Ball 1 000 ₽ dans les Boutiques une fois Maître |
| 4.1c | Outil `dev_scripts/nabla/coverage.py` (→ `docs/nabla/couverture.md`) ; Arakdo, Méditikka, Mangriff, Séléroc (nuit) sur les routes ; Bargantua blanc (Galar & Hisui) ; tous les objets d'évolution à Nénucrique ; Scalproie sauvages avec Emblème du Général ; capacités ajoutées pour Cerbyllin et Pomdorochi ; inscriptions des Ruines du Désert (Tutétékri) |

## En attente côté utilisateur
- 4.1b-2 testée et validée (refus sans argent, sauvegarde, Raichu d'Alola).
- 4.1b-3 testée et validée (niveau 5 des starters, Beast Balls) ; starters retirés des rochers à sa demande.
- 4.1c testée et validée (Méditikka, Arakdo, Séléroc, vendeur de Nénucrique). Inscriptions de Tutétékri (Route 111, Ruines du Désert) pas encore testées en jeu.
- Relire la répartition dans `docs/nabla/safari.md` (facultatif : l'utilisateur voulait surtout savoir si tout est obtenable).
- Retouches des routes sauvages (4.1d) : il les fera lui-même dans Porymap (onglet Wild Pokémon) ou par listes.

## Zone en cours : WEST BEACH v1
- Livrée (passage de sable au sud de la route 115 → île de sable avec hautes herbes ; nom « WEST BEACH » ; case du bas de la route 115 sur la carte). En attente du test de l'utilisateur et de ses retouches éventuelles dans Porymap. Contenu (Pokémon, dresseurs, objets) à définir plus tard.
- Méthode : `docs/nabla/zones.md`. Outil d'image de map : `dev_scripts/nabla/render_map.py`.

## Plan du monde étendu (6.2)
- `docs/nabla/world.md` : forêt au sud de la route 123 (intrigue juste après le Mont Mémoria, Timmy/Wally), îles accessibles par Plongée, îles mirages des légendaires après la Ligue. Niveaux : réglés plus tard avec les level caps (choix de l'utilisateur).

## 4.2a et 4.2b faites (IDs Conseil 4 : Damien 261, Spectra 262, Glacia 263, Aragon 264, Marc 335 ; cap après le 8ᵉ badge : 72) ; 4.2c rival et Timmy en cours (fiche prête, en attente des équipes ; `STARTER` → 3 versions générées par Claude ; IDs rival `TRAINER_{MAY,BRENDAN}_{ROUTE_103,RUSTBORO,ROUTE_110,ROUTE_119,LILYCOVE}_{TREECKO,TORCHIC,MUDKIP}` où le suffixe est le starter du joueur ; Timmy : `TRAINER_WALLY_MAUVILLE` 656, `TRAINER_WALLY_VR_1` 519)
- Champions : équipes de l'utilisateur dans `src/data/trainers.party` (fiche : `docs/nabla/trainers.md`), talents choisis par Claude, level caps 16/20/27/34/35/41/51/59, puis 72 jusqu'au titre de Maître.
- Difficile : `GetDifficultyLevel` (`src/caps.c`) = niveau × 1,1 arrondi à l'inférieur, au moins +1 ; appliqué aux équipes Normal des dresseurs adverses (`src/battle_setup.c`) et aux level caps. Une équipe `Difficulty: Hard` faite à la main est utilisée telle quelle.
- Test : menu debug *Trainers… → Trainer 1* (Roxanne 265 … Juan 272 ; Lévy & Tatia en *Double Battle*) → *Try Battle* ; Difficile : *Flags & Vars → Set Var XYZ…* `0x404E` = 2 (Normal = 1).
- Ensuite : 4.2c rival et Timmy, 4.2d Aqua/Magma ; 4.3 calibrage (niveaux des sauvages et des autres dresseurs) ; phases 5 à 8.

## Repères techniques
- **Safari** : `VAR_NABLA_SAFARI_REGION` (0x4083) ; constantes `NABLA_SAFARI_REGION_*`, prix et ids de menu (`include/constants/nabla.h`) ; `src/nabla_safari_zone.c` (table `sSafariZoneRegions` : nom, flag, prix, condition après la Ligue, régions d'évolution ; specials du comptoir ; niveaux `GetSafariZoneRegionWildLevel` ; `IsPlayerInEvolutionRegion` appelé par `IF_REGION`/`IF_NOT_REGION` dans `src/pokemon.c`) ; dans `src/wild_encounter.c`, `GetCurrentMapWildMonHeaderId` saute à la table de la région (11 tables placées juste après celle d'origine de chaque zone, comme la Grotte Altérée) ; évolution `CreateSafariZoneRegionWildMon`. Scripts : `data/scripts/nabla/safari_zone.inc` (menus du comptoir), entrée `Route121_SafariZoneEntrance`, sortie `SafariZone_South`. Test : `test/nabla_safari_zone.c` (`make check TESTS="Nabla"`).
- **Flags Nabla** : `FLAG_NABLA_EXP_SHARE` 0x20, `FLAG_NABLA_LEVEL_CAPS` 0x21, régions du Safari 0x22-0x28 (Johto → Paldea), zones spéciales 0x29-0x2B, objets cachés 0x264-0x27E, Méga-Gemmes au sol 0x280 et 0x286-0x295, événement Latios 0x281-0x285. **Vars** : `VAR_NABLA_DIFFICULTY` 0x404E, `VAR_NABLA_SAFARI_REGION` 0x4083.
- **Dresseurs ajoutés** : `TRAINER_NABLA_MATT_SOUTHERN_ISLAND` 855, `TRAINER_NABLA_GRUNT_SOUTHERN_ISLAND` 856 ; partenaire `PARTNER_STEVEN_SOUTHERN_ISLAND` 2.
- **Outils** (`dev_scripts/nabla/`) : `hidden_item_spots.py` (cases valides pour un objet), `list_items.py` (tableaux de `docs/nabla/items.md`), `safari_tables.py` (tables du Safari + `docs/nabla/safari.md`), `coverage.py` (espèces obtenables + `docs/nabla/couverture.md`), `render_map.py` (image d'une map).
- **Docs de référence** : `docs/nabla/items.md` (tous les objets ajoutés, boutiques, Méga-Gemmes), `docs/nabla/safari.md`, `docs/nabla/couverture.md`.
- **Correctif d'expansion à proposer en amont** : `AreMultiPartiesFullTeams` (`src/battle_util.c`) lisait les drapeaux du combat précédent → sélection d'équipe ignorée dans les combats en duo scriptés.
- **Fichiers d'expansion modifiés** (attention aux merges upstream ; `pokedex_plus_hgss.c` le plus risqué) : `src/{battle_message,battle_script_commands,battle_util,caps,field_move,field_player_avatar,item_menu,new_game,option_menu,party_menu,pokedex_plus_hgss,pokemon,pokemon_summary_screen,scrcmd,shop_criteria,strings,wild_encounter}.c`, `data/specials.inc`, `src/data/{items.h,trainers.party,battle_partners.party,wild_encounters.json}`, `src/data/pokemon/species_info/gen_*_families.h`, `src/data/pokemon/level_up_learnsets/gen_9.h`, `include/{global.h,field_move.h,pokedex_plus_hgss.h,strings.h}`, `include/constants/{flags,vars,global,opponents,battle_partner,battle_string_ids}.h`, `include/config/*.h`, nombreuses maps et scripts (`data/maps/*`, `data/scripts/players_house.inc`, `data/battle_scripts_1.s`).

## Pièges déjà rencontrés (et règles qui en découlent, dans CLAUDE.md)
- **Ne jamais réattribuer un flag/var Nabla libéré** : la sauvegarde de test de l'utilisateur peut l'avoir posé (cas de la Gardevoirite invisible).
- **Objets de map ajoutés en fin de liste uniquement** : la sauvegarde garde la liste d'objets de la map courante ; changer l'ordre casse `addobject` (cas de Latios invisible).
- Placement d'objets : passer par `hidden_item_spots.py` (évite ponts, cases isolées, voisins d'objets).
- Édition de la sauvegarde de l'utilisateur : faisable (format Gen 3, sommes de contrôle). Les offsets de SaveBlock1 se calculent en compilant un petit fichier C avec `offsetof` (toolchain devkitARM, `-iquote include -DMODERN=1 -DTESTING=0 -DEMERALD`) ; toujours faire une copie de sauvegarde d'abord et vérifier qu'aucun émulateur n'est ouvert.
- Copies de sauvegarde de l'utilisateur hors repo : `../pokeemerald_backup_before_latios_edit.sav`, `../pokeemerald_backup_before_gardevoirite_fix.sav`.
