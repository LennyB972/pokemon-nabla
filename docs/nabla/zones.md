# Zones ajoutées par Nabla

## Liste

| Zone | Map | Accès | Carte de la région | Contenu |
|---|---|---|---|---|
| WEST BEACH (Plage de l'Ouest) | `NablaWestBeach` (30 × 26) | Route 115 : bande de sable vers l'ouest au sud de la route (connexion est ↔ ouest, sans Surf) | case du bas de la route 115 (`MAPSEC_NABLA_WEST_BEACH`) | v2 (avant le 1er badge) : grande plage de sable entourée par la mer au nord, à l'ouest et au sud (rivage arrondi, rangée de rochers dans l'eau au bord de la carte : pas de mur invisible), îlots d'herbe aux bords arrondis avec hautes herbes, bosquets, dômes de rochers au milieu du sable, liseré de plage à l'est qui prolonge la côte de la Route 115. Herbes 5-8 : Taupikeau, Crabicoque, Concombaffe, Bacabouh, Krabby, Babimanta, Flingouste, Stari ; Surf et pêche : Vorastérie, Tentacool |
| EMERALD FOREST (Forêt Émeraude) | `NablaEmeraldForest_Entrance` (24 × 22), `NablaEmeraldForest` (48 × 56), `NablaEmeraldForest_Sanctuary` (22 × 18) | Route 123 : chemin vers le sud dans l'encoche des arbres du bas, colonnes 102-107 (connexions continues Route 123 → lisière → forêt → sanctuaire) | deux cases sous la Route 123 (`MAPSEC_NABLA_EMERALD_FOREST`) | Lisière en petits arbres comme la Route 123, puis grands arbres du Bois Clémenti ; forêt sinueuse (clairière avec un îlot, recoin à l'est, couloir ouest avec un rebord et une boucle, prairie, couloir est avec une poche cachée, chemin vers le sanctuaire) ; sanctuaire : clairière, vieil arbre entouré de fleurs. Ombre et musique du Bois Clémenti (lisière ensoleillée). Herbes 30-34 (lisière et forêt) : Grimalin, Brocélôme, Mushana, Florges, Magirêve, Bombydou. Dessinée par `dev_scripts/nabla/draw_emerald_forest.py` |

## Créer une zone

1. **Map** : Porymap, *File → New Map*. Nom préfixé `Nabla` (ex. `NablaWestBeach`), groupe `gMapGroup_Nabla`. Porymap l'ajoute à la fin du groupe : les numéros des maps existantes ne bougent pas (les sauvegardes les retiennent).
2. **Script de la map** : vérifier que `data/maps/<Map>/scripts.inc` est inclus dans `data/event_scripts.s` **avant** le bloc `.if IS_FRLG` (sinon : « undefined reference to `<Map>_MapScripts` »).
3. **Liaison** :
   - connexion (passage continu) : onglet *Connections*, case *Mirror to Connecting Maps*, puis *Save All* ;
   - warp (porte, grotte) : un événement *Warp* dans chaque map, chacun pointant vers le numéro du warp d'arrivée.
   - Une map d'origine ne se modifie que pour ajouter le passage.
4. **Nom et carte de la région** : nouvelle section ajoutée **à la fin** de `src/data/region_map/region_map_sections.json` (les numéros de sections sont gardés dans les Pokémon comme lieu de rencontre), case(s) dans `src/data/region_map/region_map_layout.h` (ou *Tools → Region Map Editor*), puis la section dans le champ *Location* du Header de la map.
5. **Niveaux** : dresseurs et Pokémon sauvages calés sur les zones qui entourent la nouvelle zone (niveaux après l'étape 4.3 : `docs/nabla/levels.md`). Les Pokémon sauvages évoluent selon leur niveau (échange, objet, bonheur… au niveau 40) : choisir les espèces en conséquence.
6. **Vérifier** : `python3 dev_scripts/nabla/render_map.py <Map> image.png --grid` pour une image de la map, build, test en jeu ; rencontres sauvages → relancer `dev_scripts/nabla/coverage.py`.

## Porymap

Porymap réécrit à sa façon certains fichiers qu'il enregistre (ordre des clés de `layouts.json`, `heal_locations.json`, `map.json`, et il retire `name_clone` de `region_map_sections.json`). Le contenu ne change pas : avant chaque commit, ces réécritures sont annulées (`git checkout` du fichier) pour garder un historique lisible et des merges upstream simples. Les blocs animés (eau peu profonde, fleurs) apparaissent en gris dans `render_map.py` mais s'affichent normalement en jeu.

## Dessiner une côte (leçons de West Beach v2)

West Beach est dessinée par `python3 dev_scripts/nabla/draw_west_beach.py` (plan en formes → blocs, bords choisis selon les voisins, valeurs des blocs reprises d'Émeraude) : base à réutiliser pour d'autres plages. Le relancer écrase les retouches faites dans Porymap.


- Rivage sable/eau (jeu General) : `11b 11c 11d / 123 124 125 / 12b 12c 12d`, coins intérieurs `13d 13e 145 146`. Les bords côté eau (`11b 11d 123 125 12b 12c 12d 145 146`) sont des cases d'eau (Surf, hauteur 1) dessinées avec du sable ; `11c 13d 13e` sont du sable.
- Herbe dans le sable : bords `118 119 11a / 120 122 / 128 129 12a` posés sur le sable ; là où l'herbe ne touche qu'en diagonale, sable plein `124` (comme sur la Route 118). Pas de bloc pour une case de sable entre deux herbes opposées : laisser au moins 2 cases de sable entre deux zones d'herbe.
- Hautes herbes `d` entourées d'herbe `1`. Le bloc `e` n'est pas une frange d'herbe mais le haut d'un petit arbre : ne pas l'utiliser seul.
- Arbre rond (2 × 3) : `1ce 1cf / 1d6 1d7 / 1e6 1e7` ; empilés : `1dc 1dd` et `1d4 1d5` entre les deux. Dôme de rocher sur le sable (3 × 3) : `80 81 82 / 88 71 8a / 90 79 92`. Rocher dans l'eau (2 × 2) : `150 151 / 158 159`. Petit rocher : `e2` (sable), `e0` (herbe). Fleurs : `4`.
- Bords de la carte : aucune case accessible ne doit toucher le bord sans connexion (mur invisible) ; border la mer de rochers en motif irrégulier (rochers décalés d'une case, trois sortes mélangées : `150 151 / 158 159` à écume, `175 176 / 17d 17e` bruns, `348 349 / 350 351` moussus du jeu Fallarbor), deux rochers voisins se touchant toujours par un côté, coins fermés au ras du bord. Vérifier par un parcours des cases accessibles depuis l'entrée qu'aucune ne touche un bord sans connexion. Hors de la carte, c'est le bloc de bordure (ici la mer) : faire descendre la plage jusqu'à l'eau plutôt que d'arrêter une ligne d'arbres net contre la mer.
- Les dômes ont des coins de sable : les entourer de sable de tous les côtés (sinon, angles jaunes contre l'eau ou l'herbe).
- Valeurs des blocs (collision, hauteur) : reprendre celles des maps d'Émeraude (valeur la plus fréquente de chaque bloc).

## Dessiner une forêt (leçons de la Forêt Émeraude)

La Forêt Émeraude est dessinée par `python3 dev_scripts/nabla/draw_emerald_forest.py` (plans en caractères, un caractère pour deux colonnes ; le relancer écrase les retouches faites dans Porymap). Blocs du jeu General :

- Grands arbres (Bois Clémenti), deux cases de large, alignés sur les colonnes paires : haut `1ce 1cf`, puis `1d4 1d5` et `1dc 1dd` en alternance, pied `1e4 1e5` ; la rangée sous le haut et le pied ont des pièces de bord côté herbe (`1d6`/`1d7`, `1e6`/`1e7`). Entre deux rangées d'herbe, une colonne d'arbres fait donc 3, 5, 7… rangées : les bandes d'arbres qui séparent deux passages ont une épaisseur impaire (le script le vérifie).
- Petits arbres (Route 123), une case de large : haut `e`, rangées `c6`/`c7`, pied `16` (au moins 2 rangées).
- Herbe `1`, hautes herbes `d`, fleurs `4`, petit rocher `e0`, rebord à sauter vers le bas `d5 87 … d6`.
- Raccord avec une map voisine : seuls les blocs du jeu General s'affichent bien de l'autre côté d'une connexion (les maps peuvent avoir des jeux secondaires différents) ; les forêts n'utilisent que lui.
- Bordure : grands arbres (`1d4 1d5 / 1dc 1dd`) ou petits arbres comme la Route 123 (`c6 c7 / c7 c6`).
