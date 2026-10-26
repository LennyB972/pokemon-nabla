# État du projet — Pokémon Nabla (au 2026-10-25)

Point de reprise d'une nouvelle session. À lire en premier, puis `CLAUDE.md` (règles permanentes), `ROADMAP.md` (plan) et `PROGRESS.md` (journal détaillé et décisions datées).

## Prompt de reprise (à envoyer en début de session)

> Pokémon Nabla. Lis d'abord `ETAT_DU_PROJET.md`, puis `CLAUDE.md` et `PROGRESS.md`, et repars de là. Dernières choses faites : phase 5 (name box automatique, plusieurs objets d'un coup, menus en boucle, vitamines +32 EV à 5 000 ₽), West Beach v2 validée en jeu, rencontres des zones jusqu'au 8e badge (lots 1 à 8), vendeur d'objets d'évolution au marché de Poivressel, événement Rayquaza/Deoxys du Pilier Céleste après la 8e arène. Prochaine chose : je t'envoie le lot de rencontres suivant (Route Victoire et zones d'après la Ligue), même méthode que les lots précédents (mes pourcentages en noms français, tu les traduis en emplacements, couverture, fiche des rencontres, build, commit).

## Où on en est

Romhack d'Émeraude sur pokeemerald-expansion 1.17.2 (RHH), distribué en patch BPS.
- **Phases 0 à 5 terminées.**
  - 4.1 Pokémon sauvages ;
  - 4.2 dresseurs importants (Champions, Conseil 4, Maître, rival, Timmy, Team Aqua/Magma, Pierre Rochard) ;
  - 4.3 niveaux des dresseurs ordinaires et des sauvages ;
  - 5.1 name box ;
  - 5.2 plusieurs objets d'un coup et menus en boucle ;
  - 5.3 vitamines.
- **Rencontres des routes, refaites par l'utilisateur par lots** :
  - lot 1 : avant le 1er badge ;
  - lot 2 : 1er → 2e badge ;
  - lot 3 : 2e → 3e badge ;
  - lot 4 : 3e → 4e badge (Chemin Ardent, Chutes Météore, Sentier Sinuroc, Routes 112 à 115) ;
  - lot 5 : 4e → 5e badge (désert de la Route 111, Tour Mirage) ;
  - lot 6 : 5e → 6e badge (Routes 105, 107, 108 en Surf et pêche, Routes 118 à 120, Épave, Grotte Zénith avec une table ajoutée) ;
  - lot 7 : 6e → 7e badge (New Lavandia, Nénucrique, Planque Magma, Mont Mémoria, Routes 121 à 128, Grotte Tréfonds ; Forêt Émeraude notée pour plus tard) ;
  - lot 8 : 7e → 8e badge (Grotte Originelle, Caverne Fondmer, Routes 129 à 134, Pilier Céleste, Atalanopolis) ;
  - **lot suivant attendu** (Route Victoire, puis la suite). Les Surf des zones des lots précédents restent inchangés (demande de l'utilisateur).
- **Phase 6 (monde étendu)** : **West Beach v2** faite et validée en jeu (plage entourée par la mer, îlots de hautes herbes, bosquets, rochers marins irréguliers). Reste la Forêt Émeraude, les îles par Plongée, et les objets et l'événement de West Beach (`docs/nabla/world.md`).
- **Événement du Pilier Céleste** (scénario de l'utilisateur, fait, à tester) : Pierre à la sortie de l'arène d'Atalanopolis, Route Victoire bloquée jusqu'à la fin, Rayquaza (mange la Météorite, Draco Ascension, Méga sans gemme) puis Deoxys au sommet, niveau 65 ; Cozmo laisse la Météorite ; rocher blanc d'Algatia pour les formes de Deoxys.
- **Partie complète de l'utilisateur en v1** : elle servira à l'équilibrage final (niveaux, équipes, level caps). Il a déjà dit vouloir relever un peu les niveaux, à faire après sa partie de test en cours.

## Méthode de travail avec l'utilisateur

- **Langue** : français avec l'utilisateur, recommandations franches et conclusion claire. Code, commits et textes du jeu en anglais (traduction française plus tard).
- **Avant chaque étape** :
  - présenter ce qui va être fait (quoi, où, comment on vérifie) ;
  - poser les questions de conception ;
  - **attendre son feu vert**.

  Ne pas décider à sa place ce qui n'est pas couvert par `VISION.md` ou `PROGRESS.md`. Quand il donne des valeurs explicites (lots de rencontres, prix), on applique directement et on signale les approximations.
- **Fin d'étape** :
  - build vert ;
  - `make check` si du code C ou une config est touchée (0 FAIL attendu) ;
  - un commit en anglais, avec la ligne `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, puis `git push origin master` ;
  - mise à jour de `PROGRESS.md` (journal et décisions) et de ce fichier.
- **Ses tests** : il teste sur `pokeemerald.gba` (build debug) avec mGBA. Sa sauvegarde `pokeemerald.sav` est à la racine (jamais commitée). Toujours **recompiler la ROM** après un changement, y compris un changement fait dans Porymap, avant qu'il teste. Il envoie des captures d'écran quand quelque chose ne va pas : les regarder attentivement.
- **Tâches longues** : il veut des messages courts d'avancement.
- **Dresseurs importants** : c'est **l'utilisateur qui compose les équipes** (fiche `docs/nabla/trainers.md`, format Showdown). Claude intègre dans `src/data/trainers.party` et complète :
  - talents : le meilleur en compétitif ;
  - capacités absentes : 4 capacités apprises par niveau, variées ; sets compétitifs pour le dernier combat d'un personnage ;
  - IV absents : ceux des équipes d'origine ;
  - noms à la Showdown ;
  - objets tenus seulement dans les sets des combats finaux.

  Règles : Méga-Évolution à partir de la 6ᵉ arène. **Difficile = mêmes équipes, niveaux × 1,1 (arrondi inférieur, au moins +1)**, automatique, aussi pour les level caps et les partenaires (Pierre).
- **Rencontres (circuit des lots)** :
  1. Il écrit, zone par zone, des pourcentages avec des **noms français** (lexique plus bas), en précisant jour/nuit et Surf/pêche.
  2. Claude traduit en emplacements :
     - herbes : 20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1 ;
     - Surf et Éclate-Roc : 60, 30, 5, 4, 1 ;
     - Canne : 70, 30 ; Super Canne : 60, 20, 20 ; Méga Canne : 40, 40, 15, 4, 1.
  3. Niveaux : ceux des emplacements actuels. Pour la nuit, une table `_Night` qui copie la table de jour (`scale_levels.py` lui donne les niveaux de jour).
  4. Approximation quand un pourcentage est impossible avec les emplacements (exemple : Canne 60/40 → 70/30), signalée à l'utilisateur.
  5. Ensuite : `python3 dev_scripts/nabla/coverage.py` (984 / 984), `python3 dev_scripts/nabla/list_encounters.py` (`docs/nabla/rencontres.md`), build, commit.
  6. Lui dire ce que l'évolution selon le niveau change (exemple : Barpau 40+ → Milobellus à la Méga Canne). Il a accepté ces cas, ainsi que le Bargantua motif rouge par défaut.

  Ne changer que les espèces des emplacements existants. Scripts de lot : petit script Python qui édite `src/data/wild_encounters.json` (`json.dumps(indent=2, ensure_ascii=False)`), comme pour les lots 1 à 3.
- **Maps** :
  - il a Porymap 6.3.1 et doit **le fermer** avant que Claude modifie des maps (vérifiable avec `pgrep -fl -i porymap`) ;
  - quand il a modifié quelque chose : vérifier `git diff`, annuler les réécritures cosmétiques de Porymap (`git checkout` de `layouts.json`, `heal_locations.json`, `map.json`, `name_clone` dans `region_map_sections.json` si le contenu est identique), garder ses vrais changements, recompiler, committer ;
  - Claude dessine les zones par script (voir « Dessin de maps »), montre une image (`render_map.py`, avec la route voisine pour le raccord), puis l'utilisateur teste en jeu.

## Environnement et commandes

- `export DEVKITPRO=/opt/devkitpro DEVKITARM=/opt/devkitpro/devkitARM`, puis `make -j$(sysctl -n hw.ncpu)` → `pokeemerald.gba`.
- `make check` (~8 min). Référence :
  - **0 FAIL**, 5 393 réussis (5 874 au total) ;
  - 33 `ASSUMPTION_FAIL` (Grêle → Neige, normal), 18 known failing, 9 expect failing, 421 TO_DO.
  - `make check TESTS="Nabla"` : tests Nabla seuls (`test/nabla_*.c`).
- Patch : `./make_bps.sh` (ROM propre `../rom/emerald_us.gba`, Flips `../tools/flips`).
- `test/save.c` : garde-fou des tailles de sauvegarde.
- **Menu debug** (R + START) :
  - un dresseur : *Trainers… → Trainer 1* (numéro), puis *Try Battle* ;
  - un duo : *Trainer 2* et *Partner*, ou *Utilities → Steven Multi* pour le Centre Spatial ;
  - Difficile : *Flags & Vars → Set Var* `0x404E` = 2 (Normal = 1) ;
  - Maître de la Ligue : *Set Flag* `0x87F` ;
  - argent : *Give → Max Money*.

## Ce qui est fait

| Étape | Contenu |
|---|---|
| 0 | Docs, patch BPS, README + crédits RHH, intro RHH retirée |
| 1 | Combat moderne (Gelure, Neige, pas d'affection, types affichés) ; QoL (CT réutilisables, Multi Exp Gen 6, IV/EV chiffrés, texte MID/FAST/INSTANT) ; doubles sauvages 8 % ; jour/nuit + éclairages ; évolutions dans le résumé (START sur la page INFO) |
| 2 | Menu du camion (difficulté Normal/Difficile, level caps on/off) ; level caps durs (`src/caps.c`) ; évolutions par échange (Fil de Liaison) ; style de combat SHIFT/SET/BLIND ; messages de level cap ; sac agrandi |
| 3 | Suiveurs ; CS sans les apprendre ; course automatique ; objets de progression et boutiques à paliers de badges ; événement Latios façon ROSA (Méga-Bracelet après le 5ᵉ badge) ; Méga-Gemmes |
| 4.1 | Jour/nuit 12 h/12 h + rencontres selon l'heure ; Safari moderne par région (8 régions, zones spéciales après la Ligue) ; couverture complète (`coverage.py`) |
| 4.2 | Champions (caps 16/20/27/34/35/41/51/59), Conseil 4 (66-70), Marc (72), rival (`STARTER`), Timmy (+ combat de la Forêt Émeraude, dresseur 857 prêt), Team Aqua/Magma (10 combats), Pierre Rochard dans les duos ; Difficile +10 % pour adversaires, partenaires et caps |
| 4.3 | Niveaux de 728 dresseurs ordinaires, des tables sauvages et de 4 Pokémon fixes relevés par étape (`scale_levels.py`, `docs/nabla/levels.md`) ; Pokémon de dresseurs et sauvages évoluent selon leur niveau (échange, objet, bonheur… au niveau 40) ; Safari 38-42 / 48-52 / 53-57 / 68-72 selon les badges |
| 5.1 | Name box native ; nom des dresseurs sur leur réplique d'avant-combat ; nom repris des 830 textes d'Émeraude qui commencent par « NOM: » (textes inchangés ; « DAD » → « NORMAN ») |
| 5.2 | Hors combat, choix de la quantité d'objets à utiliser (Super Bonbon, Bonbons Exp, vitamines, plumes, baies EV, soins partiels ; maximum = utilisations utiles) ; tous les menus et listes bouclent (↑ en haut → en bas) |
| 5.3 | Vitamines : +32 EV chacune, 5 000 ₽ |
| 6 | **West Beach v2** (validée) ; outils et règles de dessin des zones |
| Rencontres | Lots 1 à 8 (zones jusqu'au 8e badge) : voir `PROGRESS.md` et `docs/nabla/rencontres.md` |
| Boutiques | Objets d'évolution aussi au marché de Poivressel (vendeur ajouté, tente en bas à droite) |
| Scénario | Événement du Pilier Céleste : Pierre après Juan, Rayquaza et Deoxys (niveau 65), Route Victoire bloquée jusqu'à la fin ; Cozmo laisse la Météorite au joueur ; rocher blanc d'Algatia (formes de Deoxys) |

## En attente côté utilisateur

- **Lot suivant de rencontres** (Route Victoire, zones d'après la Ligue). Il l'envoie en message ou en fichier texte.
- **Test de l'événement du Pilier Céleste** (menu debug) :
  - *Set Flag* `0x86E` (8e badge), *Give* Météorite, Méga-Bracelet, Poké Balls ; warp devant l'arène d'Atalanopolis (ou dedans, puis sortir) : Pierre.
  - Éternara : l'entrée de la Route Victoire refuse le joueur tant que l'événement n'est pas fini.
  - Pilier Céleste (sols intacts) jusqu'au sommet : scène, Rayquaza à capturer (le combat recommence), Deoxys ; Méga-Rayquaza en combat.
  - Après la Ligue (*Set Flag* `0x864`) : Deoxys au sommet s'il n'a pas été capturé. Algatia : rocher blanc avec un Deoxys. Autéquia : Cozmo et la Météorite.
- **Relever un peu les niveaux** après sa partie de test : changer les facteurs `PARTS` de `scale_levels.py` et relancer. Pour West Beach (zone Nabla, hors script), régler à la main.
- **Tests encore à faire** (il fera surtout sa partie complète) :
  - 4.2c rival et Timmy, 4.2d Aqua/Magma (numéros dans `include/constants/opponents.h` et `docs/nabla/trainers.md`) ;
  - 4.3 niveaux ;
  - 5.2 (Super Bonbons ×N, Potions ×N, vitamines ×N ; menus en boucle) ;
  - inscriptions de Tutétékri (Route 111) ;
  - vendeur d'objets d'évolution du marché de Poivressel.
- **Décision ouverte** : ajouter le nom à la main (`setspeaker`) dans les dialogues sans nom des personnages principaux (Pierre dans la Grotte Granite…).
- **West Beach** : il ajoutera des objets plus tard, et peut-être un événement pour y attirer le joueur (un dresseur qui propose un échange contre un Pokémon de West Beach).
- Il retouchera parfois des maps dans Porymap (et préviendra).

## Prochaines étapes (dans l'ordre)

1. **Lots de rencontres** suivants (Route Victoire et après), au fil de ses envois.
2. **Phase 6 Zones** (`docs/nabla/world.md`, niveaux calés sur les zones voisines) :
   - Forêt Émeraude au sud du Mont Mémoria (rencontres déjà choisies, dans `docs/nabla/world.md`). Scénario : après le Mont Mémoria, Timmy signale des activités suspectes ; ennemis ; Timmy obtient Celebi ; combat obligatoire (dresseur 857 prêt).
   - Îles accessibles par Plongée (hors scénario).
   - Objets et événement de West Beach.
3. **Phase 7 Post-game** : revanches des Champions, zones d'après la Ligue, Conseil 4 renforcé, défense du titre, légendaires via des îles mirages façon Flûte Éon.
4. **Phase 8 Release 1.0**, après sa partie complète et l'équilibrage.

À proposer un jour en amont (expansion) : correctif `AreMultiPartiesFullTeams` (`src/battle_util.c`).

## Lexique des noms français déjà rencontrés (→ constantes `SPECIES_*`)

| Français | Constante | Français | Constante | Français | Constante |
|---|---|---|---|---|---|
| Rocabot (Tempo Perso) | ROCKRUFF (_OWN_TEMPO) | Araqua | DEWPIDER | Passerouge | FLETCHLING |
| Étourmi | STARLY | Minisange | ROOKIDEE | Manglouton | YUNGOOS |
| Pâtachiot | FIDOUGH | Venipatte | VENIPEDE | Taupikeau | WIGLETT |
| Concombaffe | PYUKUMUKU | Bacabouh | SANDYGAST | Babimanta | MANTYKE |
| Flingouste | CLAUNCHER | Crabicoque | DWEBBLE | Vorastérie | MAREANIE |
| Coupenotte | AXEW | Griknot | GIBLE | Embrylex | LARVITAR |
| Terhal | BELDUM | Solochi | DEINO | Charbi | ROLYCOLY |
| Chovsourir | WOOBAT | Nodulithe | ROGGENROLA | Ténéfix | SABLEYE |
| Galekid | ARON | Embrochet | ARROKUDA | Bargantua | BASCULIN (motif rouge) |
| Minidraco | DRATINI | Dynavolt | ELECTRIKE | Gloupti | GULPIN |
| Négapi / Posipi | MINUN / PLUSLE | Mystherbe | ODDISH | Selutin | NACLI |
| Barloche | BARBOACH | Zébibron | BLITZLE | Hélionceau | LITLEO |
| Motorizard | CYCLIZAR | Sinistrail | DHELMISE | Écrapince | CLOBBOPUS |
| Barpau | FEEBAS | Medhyèna | POOCHYENA | Zigzaton | ZIGZAGOON |
| Chamallot | NUMEL | Limagma | SLUGMA | Chartor | TORKOAL |
| Charbambin | CHARCADET | Caninos de Hisui | GROWLITHE_HISUI | Pyronille | LARVESTA |
| Séléroc | LUNATONE | Solaroc | SOLROCK | Lewsor | ELGYEM |
| Météno | MINIOR | Draby | BAGON | Germéclat | GLIMMET |
| Nigirigon | TATSUGIRI (_CURLY, _DROOPY, _STRETCHY) | Kangourex | KANGASKHAN | Ossatueur d'Alola | MAROWAK_ALOLA |
| Wagomine | CARKOL | Vostourno | VULLABY | Évoli | EEVEE |
| Pohm (« pawm ») | PAWMI | Frison | BOUFFALANT | Tiboudet | MUDBRAY |
| Malosse | HOUNDOUR | Darumarond | DARUMAKA | Pimito | CAPSAKID |
| Héliatronc | SUNFLORA | Airmure | SKARMORY | Tylton | SWABLU |
| Mangriff | ZANGOOSE | Scorplane | GLIGAR | Lestombaile | BOMBIRDIER |
| Bébécaille | JANGMO_O | Férosinge | MANKEY | Doudouvet | COTTONEE |
| Lixy | SHINX | Sepiatop | INKAY | Toutombe | GREAVARD |
| Ramoloss | SLOWPOKE | Spoink | SPOINK | Groret | GRUMPIG |
| Kraknoix | TRAPINCH | Dunaja | SILICOBRA | Sabelette | SANDSHREW |
| Mascaïman | SANDILE | Virovent | BRAMBLIN | Tutafeh | YAMASK |
| Balbuto | BALTOY | Archéomire | BRONZOR | Gringolem | GOLETT |
| Monorpale | HONEDGE | Cacnea | CACNEA | Cacturne | CACTURNE |
| Hypocéan | SEADRA | Viskuse | FRILLISH | Mamanbo | ALOMOMOLA |
| Oyacata | DONDOZO | Mimantis | FOMANTIS | Insécateur | SCYTHER |
| Lilliterelle | NYMBLE | Léopardus | LIEPARD | Ixon | OBSTAGOON |
| Migalos | ARIADOS | Tengalice | SHIFTRY | Roublenard | THIEVUL |
| Gromago (« gromagot ») | GHOLDENGO | Corayon de Galar | CORSOLA_GALAR | Forgerette | TINKATINK |
| Mimiqui | MIMIKYU | Mucuscule | GOOMY | Rhinocorne | RHYHORN |

| Magnéton | MAGNETON | Élekable | ELECTIVIRE | Salarsen | TOXTRICITY_AMPED / _LOW_KEY |
| Ampibidou | TADBULB | Motisma | ROTOM | Maganon | MAGMORTAR |
| Tritox | SALANDIT | Carmadura | ARMAROUGE | Malvalame | CERULEDGE |
| Branette | BANETTE | Funécire | LITWICK | Guériaigle | BRAVIARY |
| Rapasdepic | FEAROW | Grodrive | DRIFBLIM | Téraclope | DUSCLOPS |
| Méditikka | MEDITITE | Charmina | MEDICHAM | Zéblitz | ZEBSTRIKA |
| Galopa de Galar | RAPIDASH_GALAR | Farigiraf | FARIGIRAF | Cerbyllin | WYRDEER |
| Chapignon | BRELOOM | Terraiste | CLODSIRE | Noarfang | NOCTOWL |
| Tissenboule | TAROUNTULA | Paragruel (« paragrêle ») | BASCULEGION_M / _F | Hyporoi | KINGDRA |
| Otaria | SEEL | Obalie | SPHEAL | Colimucus | SLIGGOO |
| Terracool | TOEDSCOOL | Tritosor | GASTRODON_WEST / _EAST | Frigodo | FRIGIBAX |
| Marcacrin | SWINUB | Goupix d'Alola | VULPIX_ALOLA | Stalgamin | SNORUNT |
| Sabelette d'Alola | SANDSHREW_ALOLA | Grimalin | IMPIDIMP | Brocélôme | PHANTUMP |
| Magirêve | MISMAGIUS | Mushana | MUSHARNA | Bombydou | CUTIEFLY |
| Rexillius | TYRANTRUM | Dragmara | AURORUS | Kranidos | CRANIDOS |
| Amonistar | OMASTAR | Carapagos | TIRTOUGA | Kravarech | DRAGALGE |
| Gamblast | CLAWITZER | Aéroptéryx | ARCHEOPS | Ptéra | AERODACTYL |
| Golemastoc | GOLURK | Cryptéro | SIGILYPH | Milobellus | MILOTIC |

Lieux : New Lavandia = `NewMauville` ; Nénucrique = `LilycoveCity` ; Planque Magma = `MagmaHideout` ; Algatia = `MossdeepCity` ; Mont Mémoria = `MtPyre` ; Grotte Tréfonds = `ShoalCave` ; Grotte Originelle = `CaveOfOrigin` ; Caverne Fondmer = `SeafloorCavern` ; Pilier Céleste = `SkyPillar` ; Atalanopolis = `SootopolisCity` ; Pacifiville = `PacifidlogTown` ; Grotte Zénith = `ScorchedSlab` ; Épave = `AbandonedShip` ; Sentier Sinuroc = `JaggedPass` ; Chemin Ardent = `FieryPath`.

Formes régionales : `_ALOLA`, `_GALAR`, `_HISUI` (exemples : RATTATA_ALOLA, ZIGZAGOON_GALAR, ZORUA_HISUI, QWILFISH_HISUI). En cas de doute sur un nom, vérifier dans `include/constants/species.h` et demander plutôt que deviner.

## Repères techniques

- **Dresseurs** : `src/data/trainers.party`. Une version `Difficulty: Hard` faite à la main est utilisée telle quelle ; sinon la règle +10 % s'applique (`GetDifficultyTrainerMonLevel`, `src/battle_setup.c` ; `FillPartnerParty`, `src/battle_partner.c` ; formule `GetDifficultyLevel`, `src/caps.c`). Partenaires : `src/data/battle_partners.party`. Nouveaux dresseurs : `TRAINER_NABLA_*` 855-857 (`include/constants/opponents.h`, place pour 6 de plus).
- **Niveaux (4.3)** : `dev_scripts/nabla/scale_levels.py`.
  - Réglages : `PARTS` (facteurs par étape), `MAP_PARTS` (étape de chaque map), `EXCLUDED` (dresseurs de la 4.2).
  - Il repart toujours des dresseurs d'expansion (commit 87cc74b5ec) et des tables sauvages de la 4.1 (commit 476e2584ec). Une table `_Night` ajoutée depuis prend les niveaux de sa table de jour.
  - Table ajoutée par Nabla dans une map d'origine (Grotte Zénith) : `LEVELS_FROM` lui donne les niveaux d'origine d'une table voisine, et la map doit être dans `MAP_PARTS` (sinon `scale_levels.py` et `list_encounters.py` s'arrêtent).
  - Évolution des sauvages dans le jeu : `GetNablaWildEvolution` (`src/wild_encounter.c`), `NABLA_OTHER_EVOLUTIONS_LEVEL` = 40 (`include/constants/nabla.h`). Même règle en Python : `scale_levels.wild_forms`, utilisée par `coverage.py` et `list_encounters.py`.
- **Rencontres** : `src/data/wild_encounters.json`. Fiche lisible : `python3 dev_scripts/nabla/list_encounters.py` → `docs/nabla/rencontres.md` (parts par espèce, niveaux, « → en jeu », changements depuis Émeraude). Couverture : `coverage.py` → `docs/nabla/couverture.md`.
- **Name box (5.1)** : `include/config/name_box.h` (`OW_NAME_BOX_NPC_TRAINER` TRUE) ; `TryTakeSpeakerFromMessage` et `sMessageSpeakerAliases` dans `src/field_message_box.c` ; test `test/nabla_name_box.c`. Convention pour les nouveaux textes : « NOM: » au début de la réplique (voir `CLAUDE.md`).
- **Plusieurs objets d'un coup (5.2)** : `GetItemUseMaxQuantity`, `TryChooseItemUseQuantity`, `UseItemAgainAsChosen` dans `src/party_menu.c` ; texte `gText_UseHowManyVar1s` (`src/strings.c`) ; test `test/nabla_item_quantity.c`.
- **Menus en boucle (5.2)** : `Menu_ProcessInputNoWrap` et `Menu_ProcessInputNoWrapAround_other` (`src/menu.c`), `TryWrapListMenuSelection` (`src/list_menu.c`).
- **Vitamines (5.3)** : `ITEM6_ADD_VITAMIN_EV` = 32 (`include/constants/item_effects.h`, utilisé dans `src/data/pokemon/item_effects.h`) ; prix dans `src/data/items.h`.
- **Safari** : `VAR_NABLA_SAFARI_REGION` (0x4083), `src/nabla_safari_zone.c` (régions, prix, niveaux), `dev_scripts/nabla/safari_tables.py`, `docs/nabla/safari.md`.
- **Zones** :
  - groupe `gMapGroup_Nabla`, maps `Nabla*` ;
  - scripts inclus avant `.if IS_FRLG` dans `data/event_scripts.s` ;
  - sections de carte en fin de `region_map_sections.json` ;
  - marche à suivre dans `docs/nabla/zones.md` ;
  - image : `python3 dev_scripts/nabla/render_map.py <Map> out.png --grid` (blocs animés en gris).
- **Dessin de maps** :
  - West Beach est dessinée par `python3 dev_scripts/nabla/draw_west_beach.py` (plan en formes → blocs ; le relancer écrase les retouches Porymap).
  - Règles des tuiles dans `docs/nabla/zones.md` : rivage `11b`-`12d` et coins `13d 13e 145 146`, herbe dans le sable `118`-`12a`, arbres `1ce`…, dômes, rochers marins de trois sortes, bloc `e` interdit seul, bords de carte fermés.
  - À réutiliser pour les prochaines plages et côtes. Après un dessin, vérifier qu'aucune case accessible ne touche un bord sans connexion (parcours des cases depuis l'entrée).
- **Flags Nabla** : 0x20 Multi Exp, 0x21 level caps, 0x22-0x28 régions du Safari, 0x29-0x2B zones spéciales, 0x264-0x27E objets cachés, 0x280 et 0x286-0x295 Méga-Gemmes au sol, 0x281-0x285 événement Latios, 0x296-0x29D événement du Pilier Céleste.
- **Événement du Pilier Céleste** : `data/scripts/nabla/rayquaza_event.inc` (appels ajoutés dans les scripts d'Atalanopolis, d'Éternara, du Pilier, de Cozmo et du rocher blanc d'Algatia) ; `src/nabla_white_rock.c` (formes de Deoxys, test `test/nabla_white_rock.c`) ; niveau `NABLA_SKY_PILLAR_LEGENDARIES_LEVEL`.
- **Vars Nabla** : `VAR_NABLA_DIFFICULTY` 0x404E (1 Normal, 2 Difficile), `VAR_NABLA_SAFARI_REGION` 0x4083.
- **Outils** (`dev_scripts/nabla/`) : `hidden_item_spots.py`, `list_items.py`, `safari_tables.py`, `coverage.py`, `render_map.py`, `scale_levels.py`, `list_encounters.py`, `draw_west_beach.py`.
- **Docs de référence** (`docs/nabla/`) : `items.md`, `safari.md`, `couverture.md`, `zones.md`, `world.md`, `trainers.md`, `levels.md`, `rencontres.md`.
- **Fichiers d'expansion modifiés** (attention aux merges upstream ; `pokedex_plus_hgss.c` est le plus risqué) :
  - `src/{battle_message,battle_partner,battle_script_commands,battle_setup,battle_util,caps,field_message_box,field_move,field_player_avatar,item_menu,list_menu,menu,new_game,option_menu,party_menu,pokedex_plus_hgss,pokemon,pokemon_summary_screen,scrcmd,shop_criteria,strings,wild_encounter}.c` ;
  - `data/specials.inc`, `data/event_scripts.s` ;
  - `src/data/{items.h,trainers.party,battle_partners.party,wild_encounters.json}`, `src/data/pokemon/item_effects.h`, `src/data/pokemon/species_info/gen_*_families.h`, `src/data/pokemon/level_up_learnsets/gen_9.h`, `src/data/region_map/*` ;
  - `data/maps/map_groups.json`, `data/layouts/layouts.json` ;
  - `include/{global.h,caps.h,field_message_box.h,field_move.h,party_menu.h,pokedex_plus_hgss.h,strings.h,wild_encounter.h}`, `include/constants/{flags,vars,global,opponents,battle_partner,battle_string_ids,item_effects}.h`, `include/config/*.h` ;
  - `test/battle/{evolution_tracker,ability/ball_fetch}.c` ;
  - nombreuses maps et scripts.

## Pièges déjà rencontrés

- Ne jamais réattribuer un flag ou une var Nabla libéré (sauvegardes de l'utilisateur).
- Relancer `scale_levels.py` écrase les niveaux des dresseurs ordinaires et des sauvages, y compris une retouche faite dans Porymap. Pour rééquilibrer, changer un facteur ou l'étape d'une map dans le script.
- Objets de map : ajouter en fin de liste uniquement (sinon `addobject` casse, cas de Latios). Listes numérotées (maps, layouts, sections de carte, dresseurs) : ajouter toujours **à la fin**.
- `wild_encounters.json` contient aussi les tables de RFVF (labels `_FireRed`/`_LeafGreen`) : les ignorer, et ne pas en parler à l'utilisateur, qui ne s'occupe que d'Émeraude.
- Tests d'expansion qui supposent un comportement que Nabla change : les adapter avec un commentaire « Pokémon Nabla » (Ball Fetch, Evolution Tracker, prix et EV des vitamines dans nos tests).
- **Dessin** :
  - le bloc `e` est le haut d'un petit arbre, pas une frange d'herbe ;
  - pas de ligne d'arbres collée à la mer : faire descendre la plage jusqu'à l'eau ;
  - pas de dôme contre l'eau ou l'herbe (angles jaunes) ;
  - les bords de carte sans connexion doivent être fermés (rochers), sinon le joueur bute sur un mur invisible.
- **Rencontres** :
  - la Canne n'a que deux emplacements (70/30) ;
  - un Pokémon sauvage de niveau 40 ou plus prend ses évolutions par échange ou par objet (exemples : Méga Canne → Milobellus, Hastacuda, Qwilpik) ;
  - le lieu ne fait pas évoluer un sauvage (`IsEvolutionByLocation` : Magnéton à New Lavandia), sauf au niveau 40 ;
  - lot qui ne fait pas 100 % : la place qui manque va à une espèce qui perdrait sa seule source (décision du 2026-10-26) ;
  - le Rocabot Tempo Perso est une espèce à part (`SPECIES_ROCKRUFF_OWN_TEMPO`), qui évolue en Lougaroc Crépusculaire entre 17 h et 18 h ;
  - `coverage.py` compte les formes avec leur espèce : une forme qui demande une pré-évolution particulière peut lui échapper.
- Placement d'objets : `hidden_item_spots.py`. Édition de la sauvegarde de l'utilisateur : possible (format Gen 3), toujours avec une copie avant (copies hors repo : `../pokeemerald_backup_before_latios_edit.sav`, `../pokeemerald_backup_before_gardevoirite_fix.sav`).
