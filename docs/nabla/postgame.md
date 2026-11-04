# Post-game (phase 7)

Conception validée avec l'utilisateur (2026-10-29). Chaque partie est construite comme une étape à part ; les équipes des dresseurs sont composées par l'utilisateur (`docs/nabla/trainers.md`).

## Ligue après la première victoire (7.1)

- **Conseil 4 et Marc** : leurs équipes actuelles, au niveau 100 et avec l'IA intelligente, dès que le joueur est Maître (`FLAG_IS_CHAMPION`). Règle par classe de dresseur (Conseil 4, Maître) : `IsNablaPostGameLeagueTrainer` (`src/battle_setup.c`), utilisée pour le niveau et pour l'IA (`src/battle_ai_main.c`), en Normal comme en Difficile.
- **Pierre** (Chutes Météore) : niveau 100 (`TRAINER_STEVEN`).
- **Cadeau de la Ligue** : au réveil après le premier Panthéon, Maman annonce un colis de la Ligue, déposé dans le PC du joueur (stockage d'objets) : 150 Bonbons Exp. XL et 50 Super Bonbons (150 XL ≈ une équipe de 6 Pokémon à croissance lente du niveau 72 au niveau 100).
- **Générique** : complet la première fois ; ensuite, B le passe (Émeraude se contentait de l'accélérer).
- **Revanches des Champions et de Timmy** : tout au niveau 100, une équipe par personnage (composée par l'utilisateur, sets de Claude), en **simple** sauf Lévy & Tatia (duo), **IA intelligente**. L'équipe est sur la revanche 2 ; les revanches 3 à 5 la reprennent (`Copy Pool`). Fiche : fin de `docs/nabla/trainers.md`.

## Défense du titre (7.2, faite)

Scripts : `data/scripts/nabla/title_defense.inc` (textes `data/text/nabla/title_defense.inc`), appelés depuis les scènes d'origine de la salle du Maître et du Panthéon quand `FLAG_IS_CHAMPION` est posé. Marc (salle du Maître et Panthéon) a ce flag comme flag d'objet : il n'est plus là une fois le joueur Maître. Le challenger (et le 2ᵉ jumeau pour Lévy & Tatia) : objets ajoutés en fin de liste de la salle du Maître, sprites `VAR_OBJ_GFX_ID_1` / `_2`, cachés par `FLAG_TEMP_11`. Suivi : `VAR_NABLA_TITLE_DEFENSE` (0x408B) et les constantes `NABLA_CHALLENGER_*` (`include/constants/nabla.h`) ; challenger de la visite dans `VAR_TEMP_2`.


- **Déroulé** : le joueur refait le Conseil 4 ; la salle du Maître est vide, un challenger arrive ; combat au niveau 100 ; le joueur entre **seul** au Panthéon (pas de Marc, ni de May ni du Prof. Seko). Variante des scènes de la salle du Maître et du Panthéon, à tester en jeu.
- **Challengers** (13) : Timmy (`TRAINER_WALLY_VR_5`), Pierre (`TRAINER_STEVEN`), Marc, les 8 Champions (leur revanche 5), Max et Arthur. Équipes au niveau 100, prêtes (7.1b). Marc, Max et Arthur ont leur propre dresseur, repris d'un dresseur inutilisé d'Émeraude : `TRAINER_NABLA_WALLACE_TITLE_DEFENSE`, `_MAXIE_`, `_ARCHIE_` (`include/constants/opponents.h`).
- **Ordre** : Timmy, puis Pierre, puis Marc ; ensuite tirage au hasard parmi les 13, sans retomber sur le même deux fois de suite. Une var compte les défenses.
- **Récompenses** :
  - Timmy : une **GS Ball** (nouvel objet rare) ; au vieil arbre du sanctuaire de la Forêt Émeraude, Celebi apparaît au niveau 80 ;
  - Pierre : le **Charme Chroma** ;
  - Marc : une **Master Ball** ;
  - ensuite, tirage : Master Ball, Patch Talent, Bouchon d'Or, 5 Bouchons d'Argent, 10 PP Max, Charme Exp. et Charme Ovale (une seule fois chacun). Rien d'achetable.
- **Entraînement ultime** : PNJ au Centre Pokémon de la Ligue (1er étage), commandes natives `canhypertrain` / `hypertrain` (`data/scripts/nabla/hyper_training.inc`).
- **Celebi** : au vieil arbre du sanctuaire de la Forêt Émeraude (4 cases de l'arbre, `Nabla_EmeraldForest_Sanctuary_EventScript_OldTree`), avec la GS Ball : Celebi niveau 80 (`NABLA_POST_GAME_LEGENDARIES_LEVEL`), qui revient tant qu'il n'est pas capturé ; la GS Ball disparaît à la capture.

## Pierre et la Flûte Éon (7.3a et 7.3b, faites)

- Au réveil après le premier Panthéon, Maman dit aussi qu'un homme élégant, STEVEN, attend le joueur chez lui à Algatia (`data/scripts/nabla/post_game.inc`). Le personnage d'origine de Pierre est chez lui dès que la Ligue est gagnée, tant que le joueur n'a pas la Flûte (`Nabla_StevensHouse_EventScript_SetUp`), même sans la scène de Maman.
- Chez lui, Pierre donne la **Flûte Éon** (`ITEM_EON_FLUTE`, objet rare ajouté par Nabla) et explique les mirages, puis repart aux Chutes Météore. Terhal et la lettre d'origine restent.
- **Flûte** (`data/scripts/nabla/eon_flute.inc`, `src/nabla_eon_flute.c`, `ItemUseOutOfBattle_EonFlute` dans `src/item_use.c`) : depuis le sac, là où le Vol est possible ; Latios crie, la liste des destinations s'affiche, fondu, arrivée. Depuis une destination (repérée par sa section de carte, `sEonFluteDestinations`), la Flûte ramène là où on était (point gardé dans le warp dynamique de la sauvegarde).
- **Destinations** : Île Lointaine, Rocher Nombril, Île Aurore (îles d'événement d'Émeraude, qu'on atteignait avec des tickets). Leurs bateaux et marins sont cachés (flag d'objet `FLAG_SYS_GAME_CLEAR`). Mew, Lugia, Ho-Oh au niveau 80, et ils reviennent à la visite suivante s'ils sont vaincus (plus de `FLAG_DEFEATED_*`). Île Aurore : Jirachi (`FLAG_NABLA_JIRACHI_CAUGHT`), visible au centre de l'île, sans l'énigme du triangle de Deoxys (Deoxys et le triangle sont cachés).
- **Îlot des Oiseaux** (7.3b, premier mirage, `NablaBirdIslet`, dans la liste de la Flûte une fois Lugia capturé, demande de l'utilisateur du 2026-11-04) : Artikodin (ouest), Électhor (nord), Sulfura (est) le jour, leurs formes de Galar la nuit (`NablaMirage_IsNight`, nuit de 18 h à 6 h comme les rencontres), niveau 80. Un flag par oiseau (`FLAG_NABLA_*_CAUGHT`, 0x2A2-0x2A7).
- **Île Lune** (`NablaMoonIsland`) : Cresselia le jour, Darkrai la nuit, niveau 80, dans la clairière (`FLAG_NABLA_CRESSELIA_CAUGHT`, `_DARKRAI_`, 0x2A8-0x2A9) ; Darkraïte au sol (0x2B5).
- **Île Liberté** (`NablaLibertyIsland`, reprise du Rocher Nombril) : Victini et Meloetta, niveau 80 (`FLAG_NABLA_VICTINI_CAUGHT`, `_MELOETTA_`, 0x2AA-0x2AB).
- **Archipel des Tokos** (`NablaTapuIslands`, archipel de plages : un îlot par Tokos, Zeraora et Marshadow sur l'île centrale) : Tokorico, Tokopiyon, Tokotoro, Tokopisco, Marshadow, Zeraora, niveau 80 (`FLAG_NABLA_*_CAUGHT`, 0x2AC-0x2B1) ; Zéraoraïte au sol (0x2B6).
- **Grotte Azurée** (`NablaCeruleanCave`, reprise du sous-sol des Chutes Météore) : Mewtwo, niveau 80 (`FLAG_NABLA_MEWTWO_CAUGHT`, 0x2B2) ; Méga-Gemmes X et Y au sol, sur le plateau et sur l'estrade du bas (0x2B3-0x2B4). Premier mirage à débloquer : dans la liste de la Flûte une fois Mew capturé.
- **Tour Cendrée** (`NablaBurnedTower`, reprise du rez-de-chaussée du Mont Mémoria) : Raikou, Entei, Suicune, niveau 80 (`FLAG_NABLA_*_CAUGHT`, 0x2B7-0x2B9). Dans la liste de la Flûte une fois Ho-Oh capturé.
- **Lacs** (`NablaThreeLakes`, reprise de l'Île du Sud) : Créhelf, Créfollet, Créfadet, niveau 80 (`FLAG_NABLA_*_CAUGHT`, 0x2C-0x2E : les flags libres de 0x2C à 0x4F servent aux légendaires suivants).
- **Colonnes Lances** (`NablaSpearPillar`, reprise du toit du Pilier Céleste) : Dialga, Palkia, Giratina, Arceus, niveau 80 (`FLAG_NABLA_*_CAUGHT`, 0x2F-0x32). Dans la liste de la Flûte une fois Créhelf, Créfollet et Créfadet capturés. Premier autel : Arceus (autel et Arceus au nord-ouest, loin de Palkia et Giratina : sprites).
- **Volcan** (`NablaStarkMountain`, « STARK MOUNTAIN », reprise du sommet du Mont Chimnée) : Heatran, Volcanion, niveau 80 (`FLAG_NABLA_*_CAUGHT`, 0x33-0x34) ; Heatranite au sol (0x2BA).
- **Jardin Fleuri** (`NablaFlowerParadise`, « FLOWER PARADISE ») : Shaymin, Zarude, niveau 80 (`FLAG_NABLA_*_CAUGHT`, 0x35-0x36).
- **Temple de la Mer** (`NablaSeaTemple`, « SEA TEMPLE », sous l'eau) : Manaphy, niveau 80 (`FLAG_NABLA_MANAPHY_CAUGHT`, 0x37) ; Phione vient de son œuf (natif).
- **Brancher un mirage** : dessiner sa map (`dev_scripts/nabla/draw_*.py`, avec son entrée dans `layouts.json`), puis `add_mirage.add(...)` (`dev_scripts/nabla/add_mirage.py`) : map, section de carte, objets et scripts des légendaires, objets au sol, entrée de la Flûte (avec ses conditions de déblocage) ; vérifier avec `reach.py` et `seams.py`.
- **Autel d'un Pokémon caché** (modèle : `Nabla_SpearPillar_EventScript_Altar`) : un objet (statue `OBJ_EVENT_GFX_TRICK_HOUSE_STATUE`) avec le script de l'autel ; le Pokémon caché est un objet comme les autres, caché à l'arrivée par son flag temporaire. Pour chaque Pokémon demandé : `setvar VAR_0x8004, SPECIES_X` puis `specialvar VAR_RESULT, NablaMirage_PartyHasSpecies` (dans l'équipe, toutes formes : Giratina Originel compte ; `checkspecies` d'expansion ne voit qu'une forme exacte). S'ils y sont tous : message, cri, flash blanc, `clearflag` + `addobject` ; on lui parle ensuite comme aux autres. Déjà là ou capturé : l'autel ne fait rien. Vaincu ou en fuite : l'autel peut le rappeler.
- **Mirage à débloquer** : dans `Nabla_EventScript_EonFlute`, `getcaughtmon` (commande native, lit le Pokédex : capturé une fois suffit, même si le Pokémon a été relâché ou échangé) puis un `call_if_eq` vers un petit script qui fait son `dynmultipush`. Les numéros de la liste ne bougent pas quand une entrée manque.
- **Sprites des légendaires** : chaque Pokémon à l'écran charge toutes ses poses en mémoire vidéo ; deux gros sprites (64 × 64) au plus à l'écran, et le Pokémon qui suit le joueur reste dans sa Ball sur les mirages (`setflag FLAG_TEMP_HIDE_FOLLOWER` au début de chaque `SetUp`). Placer les gros légendaires à plus de 20 cases les uns des autres quand il y en a plus de deux ; `reach.py` le vérifie (bug vu en jeu : Palkia en morceaux, avec Dialga et un suiveur Yveltal à l'écran).
- **Légendaire d'un mirage** (modèle commun, `data/scripts/nabla/mirages.inc`) : un objet par légendaire (sprite `OBJ_EVENT_GFX_SPECIES`, animé sur place avec `MOVEMENT_TYPE_WALK_SLOWLY_IN_PLACE_*`), caché à l'arrivée par un flag temporaire s'il est capturé ou si ce n'est pas son heure ; son script met l'espèce dans `VAR_0x8004`, appelle `Nabla_EventScript_MirageLegendary` (cri, combat niveau 80 ; vaincu ou en fuite : il s'envole jusqu'à la visite suivante) et pose son flag s'il est capturé. `coverage.py` reconnaît ce modèle.
- **Ajouter une destination** : une entrée dans `Nabla_EventScript_EonFlute` (`dynmultipush`, sous condition pour un mirage à débloquer) et sa section de carte dans `sEonFluteDestinations`.

## Légendaires (7.4)

- **Niveau 80**, tous après la Ligue. Avant la Ligue, seuls Rayquaza et Deoxys (Pilier Céleste) sont capturables, plus Latios (cadeau de l'événement du 5ᵉ badge). La Chambre Scellée (Regis) est fermée jusqu'à la Ligue.
- **Sur place** : tous les légendaires d'un lieu sont visibles en même temps (`OBJ_EVENT_GFX_SPECIES`). On leur parle pour combattre. Capturé : disparaît pour de bon ; K.O. ou fuite : revient à la visite suivante.
- **Débloquer un mirage** (il apparaît dans la liste de la Flûte) : avoir **capturé** les Pokémon demandés (Pokédex).
- **Pokémon caché d'un mirage** : avoir les Pokémon demandés **dans l'équipe**, puis parler à l'autel du mirage (vérifié au moment où on parle : rien à recharger). Le Pokémon apparaît devant l'autel (cri), puis on lui parle pour le combattre, comme aux autres (décision du 2026-11-04).
- **Méga-Gemmes des légendaires** : au sol dans leur mirage, accessibles à pied (vérifié avec `dev_scripts/nabla/reach.py`).
- **Jour / nuit** : vérifié à l'arrivée sur le mirage.
- **Cadeaux** (sans combat) : Cosmog, Type:0, Wushours, Meltan.
- **Œufs** : la lignée de Cosmog (groupe Amorphe) et celle de Wushours (groupe Humanoïde) peuvent se reproduire ; l'œuf donne Cosmog ou Wushours. Phione vient de l'œuf de Manaphy (natif).

### Lieux existants

| Lieu | Légendaires |
|---|---|
| Île Lointaine | Mew |
| Rocher Nombril | Lugia, Ho-Oh |
| Île Aurore | Jirachi |
| Sanctuaire de la Forêt Émeraude | Celebi (avec la GS Ball) |
| Chambre Scellée | Regigigas (Regirock, Regice, Registeel dans l'équipe), Regieleki, Regidrago |

### Mirages (noms provisoires)

Construits avec les tuiles d'Émeraude ; une carte peut être redessinée plus tard avec un tileset communautaire (crédité dans le README) sans toucher aux scripts.

| # | Mirage | Légendaires | Débloqué par (capturés) | Caché (dans l'équipe) | Tuiles |
|---|---|---|---|---|---|
| 1 | Îlot des Oiseaux | Artikodin, Électhor, Sulfura le jour ; formes de Galar la nuit | Lugia | — | île |
| 2 | Grotte Azurée | Mewtwo | Mew | — | Chutes Météore |
| 3 | Tour Cendrée | Raikou, Entei, Suicune | Ho-Oh | — | Mont Mémoria |
| 4 | Lacs | Créhelf, Créfollet, Créfadet | — | — | île, grotte |
| 5 | Colonnes Lances | Dialga, Palkia, Giratina | Créhelf, Créfollet, Créfadet | Arceus : Dialga, Palkia, Giratina | Pilier Céleste |
| 6 | Volcan | Heatran, Volcanion | — | — | Mont Chimnée, Chemin Ardent |
| 7 | Île Lune | Cresselia le jour, Darkrai la nuit | — | — | île |
| 8 | Jardin Fleuri | Shaymin, Zarude | — | — | forêt, prairie |
| 9 | Temple de la Mer | Manaphy | — | — | Grotte Originelle |
| 10 | Île Liberté | Victini, Meloetta | — | — | île |
| 11 | Forêt de la Justice | Cobaltium, Terrakium, Viridium | — | Keldeo : les 3 | forêt |
| 12 | Plateau des Forces | Boréas, Fulguris | — | Démétéros : Boréas, Fulguris ; Amovénus : les 3 | sommet |
| 13 | Tour Dragospire | Reshiram, Zekrom | — | Kyurem : les 2 | Pilier Céleste |
| 14 | Usine Abandonnée | Genesect, Magearna ; Meltan (trouvé) | — | Melmetal : Meltan | New Lavandia |
| 15 | Sanctuaire de Kalos | Xerneas, Yveltal | — | Zygarde : les 2 | ruines |
| 16 | Mine de Diamants | Diancie, Hoopa | — | — | Grotte Granite |
| 17 | Archipel des Tokos | Tokorico, Tokopiyon, Tokotoro, Tokopisco, Marshadow, Zeraora | — | — | île |
| 18 | Autel du Soleil et de la Lune | Cosmog et Type:0 (cadeaux) | — | Necrozma : Solgaleo ou Lunala | ruines |
| 19 | Bastion de Galar | Zacian, Zamazenta ; Wushours (cadeau) | — | Éthernatos : les 2 | ruines |
| 20 | Toundra Couronnée | Sylveroy, Blizzeval, Spectreval | — | — | glace de la Grotte Tréfonds, ou tileset de neige |
| 21 | Ruines du Fléau | Chongjian, Baojian, Dinglu, Yuyu | — | — | désert, Tour Mirage |
| 22 | Cratère de Paldea | Koraidon, Miraidon | — | Terapagos : les 2 | désert |
| 23 | Kitakami | Félicanis, Fortusimia, Favianos, Ogerpon | — | Pêchaminus : les 3 Loyaux | forêt |

## Assistant du labo (7.5)

Au labo du Prof. Seko : il parle d'objets qui appartiennent à des Pokémon surpuissants ; on choisit un Pokémon de l'équipe et il donne ses objets de forme et ses Méga-Gemmes (et, si besoin, apprend Lame Ointe à Keldeo ou Chant Antique à Meloetta).

## Ordre de construction

1. 7.1 Ligue au niveau 100, Pierre, cadeau de la Ligue, générique ; puis revanches des Champions et de Timmy (équipes de l'utilisateur).
2. 7.2 Défense du titre.
3. 7.3 Flûte Éon et premiers mirages.
4. 7.4 Légendaires, par lots.
5. 7.5 Assistant du labo.
