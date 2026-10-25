# Zones ajoutées par Nabla

## Liste

| Zone | Map | Accès | Carte de la région | Contenu |
|---|---|---|---|---|
| WEST BEACH (Plage de l'Ouest) | `NablaWestBeach` (30 × 26) | Route 115 : bande de sable vers l'ouest au sud de la route (connexion est ↔ ouest, sans Surf) | case du bas de la route 115 (`MAPSEC_NABLA_WEST_BEACH`) | v2 (avant le 1er badge) : grande plage de sable entourée par la mer au nord, à l'ouest et au sud (rivage arrondi, rangée de rochers dans l'eau au bord de la carte : pas de mur invisible), îlots d'herbe aux bords arrondis avec hautes herbes, bosquets, dômes de rochers au milieu du sable, liseré de plage à l'est qui prolonge la côte de la Route 115. Herbes 5-8 : Taupikeau, Crabicoque, Concombaffe, Bacabouh, Krabby, Babimanta, Flingouste, Stari ; Surf et pêche : Vorastérie, Tentacool |

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

- Rivage sable/eau (jeu General) : `11b 11c 11d / 123 124 125 / 12b 12c 12d`, coins intérieurs `13d 13e 145 146`. Les bords côté eau (`11b 11d 123 125 12b 12c 12d 145 146`) sont des cases d'eau (Surf, hauteur 1) dessinées avec du sable ; `11c 13d 13e` sont du sable.
- Herbe dans le sable : bords `118 119 11a / 120 122 / 128 129 12a` posés sur le sable ; là où l'herbe ne touche qu'en diagonale, sable plein `124` (comme sur la Route 118). Pas de bloc pour une case de sable entre deux herbes opposées : laisser au moins 2 cases de sable entre deux zones d'herbe.
- Hautes herbes `d` entourées d'herbe `1`. Le bloc `e` n'est pas une frange d'herbe mais le haut d'un petit arbre : ne pas l'utiliser seul.
- Arbre rond (2 × 3) : `1ce 1cf / 1d6 1d7 / 1e6 1e7` ; empilés : `1dc 1dd` et `1d4 1d5` entre les deux. Dôme de rocher sur le sable (3 × 3) : `80 81 82 / 88 71 8a / 90 79 92`. Rocher dans l'eau (2 × 2) : `150 151 / 158 159`. Petit rocher : `e2` (sable), `e0` (herbe). Fleurs : `4`.
- Bords de la carte : aucune case accessible ne doit toucher le bord sans connexion (mur invisible) ; border la mer de rochers en motif irrégulier (rochers décalés d'une case, trois sortes mélangées : `150 151 / 158 159` à écume, `175 176 / 17d 17e` bruns, `348 349 / 350 351` moussus du jeu Fallarbor), deux rochers voisins se touchant toujours par un côté, coins fermés au ras du bord. Vérifier par un parcours des cases accessibles depuis l'entrée qu'aucune ne touche un bord sans connexion. Hors de la carte, c'est le bloc de bordure (ici la mer) : faire descendre la plage jusqu'à l'eau plutôt que d'arrêter une ligne d'arbres net contre la mer.
- Les dômes ont des coins de sable : les entourer de sable de tous les côtés (sinon, angles jaunes contre l'eau ou l'herbe).
- Valeurs des blocs (collision, hauteur) : reprendre celles des maps d'Émeraude (valeur la plus fréquente de chaque bloc).
