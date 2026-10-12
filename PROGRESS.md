# PROGRESS — Pokémon Nabla

## État actuel

- **Base** : pokeemerald-expansion **1.17.2** (master, commit non tagué, `git describe` = `expansion/1.17.1-11-g87cc74b5ec`).
- **Build** : ✅ `make` passe sur macOS (devkitARM). ROM utilisée à 79,7 % (26,7 Mo / 32 Mo), EWRAM 86 %, IWRAM 87 %.
- **Jeu** : expansion + Gelure, Neige à la place de la Grêle, sans affection, types adverses affichés ; CT réutilisables, Multi Exp moderne, IV/EV chiffrés, texte instantané, 8 % de combats sauvages en double ; sans l'intro RHH.
- **Étape en cours** : 1.4 terminée (jour/nuit + éclairages), en attente de ton test. Prochaine : 2.1 — menu de début de partie.

## Journal

### Session 1 — 2026-10-12
- Lecture de VISION.md, build vérifié, exploration des configs `include/config/`.
- Créé : `CLAUDE.md` (règles permanentes), `ROADMAP.md` (correspondance VISION ↔ expansion + phases), `PROGRESS.md`.
- Constats :
  - Déjà actifs par défaut : mécaniques Gen 9, Dex Gen 1-9 complet, Méga activée (mais Anneau Méga jamais donné), course en intérieur, poison sans dégâts hors combat, jour/nuit (DNS), dernière Ball utilisée, option texte « Instant ».
  - Réglables en config : Gelure (`B_USE_FROSTBITE`), doubles sauvages, level caps, CT réutilisables, Multi Exp moderne, IV/EV, followers, name box.
  - Évolutions par échange : alternatives par objet déjà présentes (Fil de Liaison…), sauf Carabing/Escargaume.
  - À coder : Nuzlocke, Choix à l'aveugle, CS sans slot, menu de début de partie.
  - Ressources libres : 381 flags `FLAG_UNUSED_*`, 29 vars `VAR_UNUSED_*`.
- Note technique : le shell de Claude doit exporter `DEVKITPRO`/`DEVKITARM` avant `make` (voir CLAUDE.md).
- Retours sur la roadmap intégrés : Nuzlocke retiré, 2 difficultés, phase 6 « Monde étendu » (nouvelles zones + ajouts narratifs) créée, post-game devient la phase 7, événement Latios/Méga-Bracelet façon ROSA en 3.4, crédits RHH en 0.2.

### Session 2 — 2026-10-12
- Étape 0.2 :
  - ROM de base vérifiée (SHA1 Émeraude US correct), rangée dans `../rom/`.
  - Flips compilé depuis les sources officielles (Alcaro/Flips) dans `../tools/flips`.
  - `make_bps.sh` : build release → patch `build/pokemon_nabla.bps` (16,8 Mo) → ré-application et comparaison SHA1 ✅.
  - `README.md` remplacé : présentation de Nabla, comment jouer, crédits RHH (pokeemerald-expansion 1.17.2) + pret.
  - `EXPANSION_INTRO` = FALSE ; code de l'intro absent de la ROM (vérifié dans les symboles).
  - **À tester par toi** : appliquer le patch sur la ROM propre, le jeu démarre sur l'écran de copyright puis l'intro Game Freak, sans la scène RHH.

- Étape 0.2 validée par l'utilisateur (le jeu se lance normalement).
- Étape 1.1 — combat moderne (`include/config/battle.h`) :
  - `B_USE_FROSTBITE` = TRUE : la Gelure remplace le Gel (VISION).
  - `B_AFFECTION_MECHANICS` = FALSE : plus d'effets d'affection en combat (comme Gen 9).
  - `B_PREFERRED_ICE_WEATHER` = SNOW : Grêle et Alerte Neige donnent la Neige (comme Gen 9).
  - `B_SHOW_TYPES` = SEEN : types de l'adversaire affichés si l'espèce a déjà été vue (même règle que l'efficacité).
  - Inchangé car déjà moderne : tout le reste de `battle.h` est à `GEN_LATEST` ; Dynamax, Téracristal et Capacités Z restent inaccessibles (leurs objets ne sont jamais donnés).
  - Tests : 0 échec ; 33 tests ignorés, tous parce qu'ils supposent la Grêle (attendu). Référence avant changement : 5 417 réussis, 0 échec.

- Étape 1.1 validée par l'utilisateur (types affichés correctement).
- Étape 1.2 — qualité de vie :
  - `I_REUSABLE_TMS` = TRUE : les CT ne s'usent plus ; les boutiques ne vendent une CT que si on ne l'a pas déjà (natif).
  - Multi Exp moderne : `I_EXP_SHARE_ITEM` = GEN_LATEST + flag `FLAG_NABLA_EXP_SHARE` (ex-`FLAG_UNUSED_0x020`). Le Multi Exp donné par M. Rochard devient un objet clé à activer/désactiver depuis le Sac (désactivé à la réception, comportement natif).
  - Résumé : page Stats → IV → EV avec valeurs chiffrées, et libellé de la page qui change (`P_SUMMARY_SCREEN_IV_EV_*`).
  - Vitesse du texte : le menu Options propose MID / FAST / INSTANT (SLOW retiré), FAST par défaut (`src/option_menu.c`, `src/new_game.c`). Une ancienne sauvegarde en SLOW s'affiche en MID.
  - Laissés tels quels (déjà présents dans expansion) : réapprendre des capacités et renommer depuis le résumé.
  - Correction : la roadmap disait à tort que « Instantané » existait déjà dans le menu.
  - Tests : 0 échec, mêmes 33 tests ignorés (Grêle) ; 1 test de l'ancien Multi Exp Gen 5 n'est plus compilé (attendu).
- Étape 1.2 validée par l'utilisateur.
- Étape 1.3 — combats sauvages en double : `WE_DOUBLE_WILD_CHANCE` = 8, `WE_DOUBLE_WILD_REQUIRE_2_MONS` = TRUE (jamais de double avec un seul Pokémon valide). Concerne les herbes et le Surf, pas la pêche ni le Parc Safari. Capture impossible tant que deux Pokémon sauvages sont sur le terrain (comportement Gen 5+, natif). Tests : 0 échec.
- Étape 1.5 — évolutions dans le résumé (demande de l'utilisateur) :
  - Rien de natif dans le résumé ; le Pokédex HGSS d'expansion sait déjà décrire chaque méthode d'évolution. Ce code a été extrait dans une fonction partagée `BufferEvolutionMethodText` (`src/pokedex_plus_hgss.c`), utilisée par le Pokédex HGSS et par le résumé.
  - Page INFO : invite « START EVOLUTION » en haut à droite (même emplacement que « START RELEARN » sur les pages d'attaques) ; START fait défiler mémo → évolutions (3 par page, la 4ᵉ ligne débordait) → mémo. Rien pour les Œufs. « Does not evolve. » si aucune évolution.
  - ⚠️ Merge upstream : l'extraction ré-indente ~290 lignes de `pokedex_plus_hgss.c` ; un conflit est probable si upstream modifie ces textes (résolution : garder notre fonction et y reporter leur changement).
  - Tests : 0 échec.
- Étape 1.5 validée par l'utilisateur après passage à 3 évolutions par page.
- Étape 1.4 — jour/nuit :
  - Config déjà correcte : `OW_ENABLE_DNS` = TRUE, vraie horloge, plages horaires Gen 9.
  - Éclairages nocturnes restaurés (accord de l'utilisateur) : patch inverse du commit expansion `a5b079d833` (93 fichiers : objets lumière sur les maps de villes, palettes `.pal`/`.pla`, tilesets, `headers.h`, correctif des Lavaridge old ladies). Appliqué sans conflit avant toute modification de map.
  - Rappel : l'heure du jeu = horloge de la cartouche + réglage de la pendule de la chambre du joueur au début (comme Émeraude).
  - Build OK. Pas de `make check` : seules des données de maps/tilesets ont changé.

## Décisions prises

| Date | Décision |
|---|---|
| 2026-10-12 | Docs de projet en français, code et commits en anglais. |
| 2026-10-12 | Nouveaux textes regroupés dans `data/text/nabla/` (scripts) et un fichier dédié (C). |
| 2026-10-12 | **Nuzlocke retiré** du projet. |
| 2026-10-12 | **2 difficultés** : Normal / Difficile, choisies en début de partie. |
| 2026-10-12 | **Level caps activables** en début de partie ; valeurs définies à la main par l'utilisateur. |
| 2026-10-12 | **CS → objets clés** obtenus aux mêmes moments de l'histoire, sans Pokémon qui connaît l'attaque. |
| 2026-10-12 | **Vraie horloge (RTC)** pour le jour/nuit. |
| 2026-10-12 | **Intro RHH retirée** ; crédit RHH dans le README, les notes de version et le générique de fin. |
| 2026-10-12 | **Nouvelles zones** : quelques zones facultatives pendant l'aventure + des zones nouvelles en post-game. Maps dessinées par l'utilisateur (Porymap) **et** par Claude. |
| 2026-10-12 | En-tête de ROM inchangé (titre `POKEMON EMER`, code `BPEE`) : les émulateurs s'en servent pour détecter la sauvegarde et l'horloge. |
| 2026-10-12 | README public en anglais (le jeu est en anglais d'abord). |
| 2026-10-12 | Combat : Gelure, Neige à la place de la Grêle, affection désactivée, types adverses affichés pour les espèces vues. |
| 2026-10-12 | QoL : CT réutilisables, Multi Exp Gen 6+ (on/off), IV/EV en valeurs chiffrées, texte MID / FAST / INSTANT (FAST par défaut). |
| 2026-10-12 | Les cases non cochées de VISION.md = « je te laisse choisir » : Claude tranche les petits réglages et les signale ; les choix qui changent l'expérience de jeu restent soumis à l'utilisateur. |
| 2026-10-13 | Éclairages nocturnes de Hoenn restaurés (patch officiel d'expansion). |
| 2026-10-12 | **Méga-Bracelet** donné comme dans ROSA : événement Latios après le **5ᵉ badge**, Île du Sud, combat en duo avec Steven. |

## Questions ouvertes

1. **Level caps** : valeurs à fournir avant l'étape 2.2 (sinon valeurs provisoires).
