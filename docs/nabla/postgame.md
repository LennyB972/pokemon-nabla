# Post-game (phase 7)

Conception validée avec l'utilisateur (2026-10-29). Chaque partie est construite comme une étape à part ; les équipes des dresseurs sont composées par l'utilisateur (`docs/nabla/trainers.md`).

## Ligue après la première victoire (7.1)

- **Conseil 4 et Marc** : leurs équipes actuelles, au niveau 100 et avec l'IA intelligente, dès que le joueur est Maître (`FLAG_IS_CHAMPION`). Règle par classe de dresseur (Conseil 4, Maître) : `IsNablaPostGameLeagueTrainer` (`src/battle_setup.c`), utilisée pour le niveau et pour l'IA (`src/battle_ai_main.c`), en Normal comme en Difficile.
- **Pierre** (Chutes Météore) : niveau 100 (`TRAINER_STEVEN`).
- **Cadeau de la Ligue** : au réveil après le premier Panthéon, Maman annonce un colis de la Ligue, déposé dans le PC du joueur (stockage d'objets) : 150 Bonbons Exp. XL et 50 Super Bonbons (150 XL ≈ une équipe de 6 Pokémon à croissance lente du niveau 72 au niveau 100).
- **Générique** : complet la première fois ; ensuite, B le passe (Émeraude se contentait de l'accélérer).
- **Revanches des Champions et de Timmy** : tout au niveau 100, une équipe par personnage (composée par l'utilisateur, sets de Claude), en **simple** sauf Lévy & Tatia (duo), **IA intelligente**. L'équipe est sur la revanche 2 ; les revanches 3 à 5 la reprennent (`Copy Pool`). Fiche : fin de `docs/nabla/trainers.md`.

## Défense du titre (7.2)

- **Déroulé** : le joueur refait le Conseil 4 ; la salle du Maître est vide, un challenger arrive ; combat au niveau 100 ; le joueur entre **seul** au Panthéon (pas de Marc, ni de May ni du Prof. Seko). Variante des scènes de la salle du Maître et du Panthéon, à tester en jeu.
- **Challengers** (13) : Timmy (`TRAINER_WALLY_VR_5`), Pierre (`TRAINER_STEVEN`), Marc, les 8 Champions (leur revanche 5), Max et Arthur. Équipes au niveau 100, prêtes (7.1b). Marc, Max et Arthur ont leur propre dresseur, repris d'un dresseur inutilisé d'Émeraude : `TRAINER_NABLA_WALLACE_TITLE_DEFENSE`, `_MAXIE_`, `_ARCHIE_` (`include/constants/opponents.h`).
- **Ordre** : Timmy, puis Pierre, puis Marc ; ensuite tirage au hasard parmi les 13, sans retomber sur le même deux fois de suite. Une var compte les défenses.
- **Récompenses** :
  - Timmy : une **GS Ball** (nouvel objet rare) ; au vieil arbre du sanctuaire de la Forêt Émeraude, Celebi apparaît au niveau 80 ;
  - Pierre : le **Charme Chroma** ;
  - Marc : une **Master Ball** ;
  - ensuite, tirage : Master Ball, Patch Talent, Bouchon d'Or, 5 Bouchons d'Argent, 10 PP Max, Charme Exp. et Charme Ovale (une seule fois chacun). Rien d'achetable.
- **Entraînement ultime** : un PNJ qui utilise les Bouchons (fonctions natives `CanHyperTrain` / `HyperTrain`), au Centre Pokémon de la Ligue par exemple.

## Pierre et la Flûte Éon (7.3)

- Au réveil après le premier Panthéon, Maman dit aussi qu'un homme élégant, STEVEN, attend le joueur chez lui à Algatia (ajouté avec cette étape).
- Chez lui, Pierre donne la **Flûte Éon** (nouvel objet rare) et explique les mirages, puis repart aux Chutes Météore. Terhal et la lettre d'origine restent.
- **Flûte** : depuis le sac, en extérieur ; Latios crie, la liste des mirages débloqués s'affiche, fondu, arrivée. Rejouer de la Flûte ramène là où on était.

## Légendaires (7.4)

- **Niveau 80**, tous après la Ligue. Avant la Ligue, seuls Rayquaza et Deoxys (Pilier Céleste) sont capturables, plus Latios (cadeau de l'événement du 5ᵉ badge). La Chambre Scellée (Regis) est fermée jusqu'à la Ligue.
- **Sur place** : tous les légendaires d'un lieu sont visibles en même temps (`OBJ_EVENT_GFX_SPECIES`). On leur parle pour combattre. Capturé : disparaît pour de bon ; K.O. ou fuite : revient à la visite suivante.
- **Débloquer un mirage** (il apparaît dans la liste de la Flûte) : avoir **capturé** les Pokémon demandés (Pokédex).
- **Pokémon caché d'un mirage** : avoir les Pokémon demandés **dans l'équipe**, puis parler à l'autel du mirage (vérifié au moment où on parle : rien à recharger).
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
| 1 | Îlot des Oiseaux | Artikodin, Électhor, Sulfura le jour ; formes de Galar la nuit | — | — | île |
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
