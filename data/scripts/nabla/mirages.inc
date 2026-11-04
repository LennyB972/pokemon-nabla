@ Legendary Pokémon of the places the Eon Flute leads to (docs/nabla/postgame.md). Each one is an object, visible
@ until it is caught (one FLAG_NABLA_*_CAUGHT each), hidden by a temporary flag set when entering the map.
@ The following Pokémon stays in its ball there: the whole sheet of each sprite in view is loaded, and big ones
@ (64 x 64) would not fit with it (dev_scripts/nabla/reach.py checks the maps).

@ Battle with the legendary Pokémon the player talked to (species in VAR_0x8004), at level 80. Returns if it was
@ caught (the caller sets its flag and releases); otherwise it flies away until the next visit.
Nabla_EventScript_MirageLegendary::
	lock
	faceplayer
	copyvar VAR_TEMP_9, VAR_0x8004
	waitse
	playmoncry VAR_0x8004, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setvar VAR_0x8005, NABLA_POST_GAME_LEGENDARIES_LEVEL
	setvar VAR_0x8006, ITEM_NONE
	special CreateEnemyEventMon
	special BattleSetup_StartLegendaryBattle
	specialvar VAR_RESULT, GetBattleOutcome
	copyvar VAR_0x8004, VAR_TEMP_9
	goto_if_ne VAR_RESULT, B_OUTCOME_CAUGHT, Common_EventScript_LegendaryFlewAway
	removeobject VAR_LAST_TALKED
	return

@ Bird Islet: Articuno, Zapdos and Moltres by day, their forms of Galar at night
Nabla_BirdIslet_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ Articuno
	setflag FLAG_TEMP_12  @ Zapdos
	setflag FLAG_TEMP_13  @ Moltres
	setflag FLAG_TEMP_14  @ Articuno (Galar)
	setflag FLAG_TEMP_15  @ Zapdos (Galar)
	setflag FLAG_TEMP_16  @ Moltres (Galar)
	specialvar VAR_RESULT, NablaMirage_IsNight
	goto_if_eq VAR_RESULT, TRUE, Nabla_BirdIslet_EventScript_SetUpNight
	call_if_unset FLAG_NABLA_ARTICUNO_CAUGHT, Nabla_BirdIslet_EventScript_ShowArticuno
	call_if_unset FLAG_NABLA_ZAPDOS_CAUGHT, Nabla_BirdIslet_EventScript_ShowZapdos
	call_if_unset FLAG_NABLA_MOLTRES_CAUGHT, Nabla_BirdIslet_EventScript_ShowMoltres
	return

Nabla_BirdIslet_EventScript_SetUpNight:
	call_if_unset FLAG_NABLA_ARTICUNO_GALAR_CAUGHT, Nabla_BirdIslet_EventScript_ShowArticunoGalar
	call_if_unset FLAG_NABLA_ZAPDOS_GALAR_CAUGHT, Nabla_BirdIslet_EventScript_ShowZapdosGalar
	call_if_unset FLAG_NABLA_MOLTRES_GALAR_CAUGHT, Nabla_BirdIslet_EventScript_ShowMoltresGalar
	return

Nabla_BirdIslet_EventScript_ShowArticuno:
	clearflag FLAG_TEMP_11
	return

Nabla_BirdIslet_EventScript_ShowZapdos:
	clearflag FLAG_TEMP_12
	return

Nabla_BirdIslet_EventScript_ShowMoltres:
	clearflag FLAG_TEMP_13
	return

Nabla_BirdIslet_EventScript_ShowArticunoGalar:
	clearflag FLAG_TEMP_14
	return

Nabla_BirdIslet_EventScript_ShowZapdosGalar:
	clearflag FLAG_TEMP_15
	return

Nabla_BirdIslet_EventScript_ShowMoltresGalar:
	clearflag FLAG_TEMP_16
	return

Nabla_BirdIslet_EventScript_Articuno::
	setvar VAR_0x8004, SPECIES_ARTICUNO
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_ARTICUNO_CAUGHT
	release
	end

Nabla_BirdIslet_EventScript_Zapdos::
	setvar VAR_0x8004, SPECIES_ZAPDOS
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_ZAPDOS_CAUGHT
	release
	end

Nabla_BirdIslet_EventScript_Moltres::
	setvar VAR_0x8004, SPECIES_MOLTRES
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_MOLTRES_CAUGHT
	release
	end

Nabla_BirdIslet_EventScript_ArticunoGalar::
	setvar VAR_0x8004, SPECIES_ARTICUNO_GALAR
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_ARTICUNO_GALAR_CAUGHT
	release
	end

Nabla_BirdIslet_EventScript_ZapdosGalar::
	setvar VAR_0x8004, SPECIES_ZAPDOS_GALAR
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_ZAPDOS_GALAR_CAUGHT
	release
	end

Nabla_BirdIslet_EventScript_MoltresGalar::
	setvar VAR_0x8004, SPECIES_MOLTRES_GALAR
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_MOLTRES_GALAR_CAUGHT
	release
	end

@ Moon Island: Cresselia by day, Darkrai at night, in the clearing
Nabla_MoonIsland_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ Cresselia
	setflag FLAG_TEMP_12  @ Darkrai
	specialvar VAR_RESULT, NablaMirage_IsNight
	goto_if_eq VAR_RESULT, TRUE, Nabla_MoonIsland_EventScript_SetUpNight
	goto_if_set FLAG_NABLA_CRESSELIA_CAUGHT, Common_EventScript_NopReturn
	clearflag FLAG_TEMP_11
	return

Nabla_MoonIsland_EventScript_SetUpNight:
	goto_if_set FLAG_NABLA_DARKRAI_CAUGHT, Common_EventScript_NopReturn
	clearflag FLAG_TEMP_12
	return

Nabla_MoonIsland_EventScript_Cresselia::
	setvar VAR_0x8004, SPECIES_CRESSELIA
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_CRESSELIA_CAUGHT
	release
	end

Nabla_MoonIsland_EventScript_Darkrai::
	setvar VAR_0x8004, SPECIES_DARKRAI
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_DARKRAI_CAUGHT
	release
	end

@ Liberty Island: Victini and Meloetta, on the ring of sand
Nabla_LibertyIsland_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ Victini
	setflag FLAG_TEMP_12  @ Meloetta
	call_if_unset FLAG_NABLA_VICTINI_CAUGHT, Nabla_LibertyIsland_EventScript_ShowVictini
	call_if_unset FLAG_NABLA_MELOETTA_CAUGHT, Nabla_LibertyIsland_EventScript_ShowMeloetta
	return

Nabla_LibertyIsland_EventScript_ShowVictini:
	clearflag FLAG_TEMP_11
	return

Nabla_LibertyIsland_EventScript_ShowMeloetta:
	clearflag FLAG_TEMP_12
	return

Nabla_LibertyIsland_EventScript_Victini::
	setvar VAR_0x8004, SPECIES_VICTINI
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_VICTINI_CAUGHT
	release
	end

Nabla_LibertyIsland_EventScript_Meloetta::
	setvar VAR_0x8004, SPECIES_MELOETTA
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_MELOETTA_CAUGHT
	release
	end

@ Tapu Islands: one islet for each Tapu, Zeraora and Marshadow on the main island
Nabla_TapuIslands_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ TapuKoko
	setflag FLAG_TEMP_12  @ TapuLele
	setflag FLAG_TEMP_13  @ TapuBulu
	setflag FLAG_TEMP_14  @ TapuFini
	setflag FLAG_TEMP_15  @ Marshadow
	setflag FLAG_TEMP_16  @ Zeraora
	call_if_unset FLAG_NABLA_TAPU_KOKO_CAUGHT, Nabla_TapuIslands_EventScript_ShowTapuKoko
	call_if_unset FLAG_NABLA_TAPU_LELE_CAUGHT, Nabla_TapuIslands_EventScript_ShowTapuLele
	call_if_unset FLAG_NABLA_TAPU_BULU_CAUGHT, Nabla_TapuIslands_EventScript_ShowTapuBulu
	call_if_unset FLAG_NABLA_TAPU_FINI_CAUGHT, Nabla_TapuIslands_EventScript_ShowTapuFini
	call_if_unset FLAG_NABLA_MARSHADOW_CAUGHT, Nabla_TapuIslands_EventScript_ShowMarshadow
	call_if_unset FLAG_NABLA_ZERAORA_CAUGHT, Nabla_TapuIslands_EventScript_ShowZeraora
	return

Nabla_TapuIslands_EventScript_ShowTapuKoko:
	clearflag FLAG_TEMP_11
	return

Nabla_TapuIslands_EventScript_ShowTapuLele:
	clearflag FLAG_TEMP_12
	return

Nabla_TapuIslands_EventScript_ShowTapuBulu:
	clearflag FLAG_TEMP_13
	return

Nabla_TapuIslands_EventScript_ShowTapuFini:
	clearflag FLAG_TEMP_14
	return

Nabla_TapuIslands_EventScript_ShowMarshadow:
	clearflag FLAG_TEMP_15
	return

Nabla_TapuIslands_EventScript_ShowZeraora:
	clearflag FLAG_TEMP_16
	return

Nabla_TapuIslands_EventScript_TapuKoko::
	setvar VAR_0x8004, SPECIES_TAPU_KOKO
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_TAPU_KOKO_CAUGHT
	release
	end

Nabla_TapuIslands_EventScript_TapuLele::
	setvar VAR_0x8004, SPECIES_TAPU_LELE
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_TAPU_LELE_CAUGHT
	release
	end

Nabla_TapuIslands_EventScript_TapuBulu::
	setvar VAR_0x8004, SPECIES_TAPU_BULU
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_TAPU_BULU_CAUGHT
	release
	end

Nabla_TapuIslands_EventScript_TapuFini::
	setvar VAR_0x8004, SPECIES_TAPU_FINI
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_TAPU_FINI_CAUGHT
	release
	end

Nabla_TapuIslands_EventScript_Marshadow::
	setvar VAR_0x8004, SPECIES_MARSHADOW
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_MARSHADOW_CAUGHT
	release
	end

Nabla_TapuIslands_EventScript_Zeraora::
	setvar VAR_0x8004, SPECIES_ZERAORA
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_ZERAORA_CAUGHT
	release
	end

@ Cerulean Cave: Mewtwo, on the peninsula of the lake (the cave is in the list of the Eon Flute once Mew is caught)
Nabla_CeruleanCave_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ Mewtwo
	call_if_unset FLAG_NABLA_MEWTWO_CAUGHT, Nabla_CeruleanCave_EventScript_ShowMewtwo
	return

Nabla_CeruleanCave_EventScript_ShowMewtwo:
	clearflag FLAG_TEMP_11
	return

Nabla_CeruleanCave_EventScript_Mewtwo::
	setvar VAR_0x8004, SPECIES_MEWTWO
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_MEWTWO_CAUGHT
	release
	end

@ Burned Tower: Raikou, Entei and Suicune, in the hall (the tower is in the list of the Eon Flute once Ho-Oh is caught)
Nabla_BurnedTower_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ Raikou
	setflag FLAG_TEMP_12  @ Entei
	setflag FLAG_TEMP_13  @ Suicune
	call_if_unset FLAG_NABLA_RAIKOU_CAUGHT, Nabla_BurnedTower_EventScript_ShowRaikou
	call_if_unset FLAG_NABLA_ENTEI_CAUGHT, Nabla_BurnedTower_EventScript_ShowEntei
	call_if_unset FLAG_NABLA_SUICUNE_CAUGHT, Nabla_BurnedTower_EventScript_ShowSuicune
	return

Nabla_BurnedTower_EventScript_ShowRaikou:
	clearflag FLAG_TEMP_11
	return

Nabla_BurnedTower_EventScript_ShowEntei:
	clearflag FLAG_TEMP_12
	return

Nabla_BurnedTower_EventScript_ShowSuicune:
	clearflag FLAG_TEMP_13
	return

Nabla_BurnedTower_EventScript_Raikou::
	setvar VAR_0x8004, SPECIES_RAIKOU
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_RAIKOU_CAUGHT
	release
	end

Nabla_BurnedTower_EventScript_Entei::
	setvar VAR_0x8004, SPECIES_ENTEI
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_ENTEI_CAUGHT
	release
	end

Nabla_BurnedTower_EventScript_Suicune::
	setvar VAR_0x8004, SPECIES_SUICUNE
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_SUICUNE_CAUGHT
	release
	end

@ Three Lakes: Uxie, Mesprit and Azelf, on the banks of the three ponds
Nabla_ThreeLakes_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ Uxie
	setflag FLAG_TEMP_12  @ Mesprit
	setflag FLAG_TEMP_13  @ Azelf
	call_if_unset FLAG_NABLA_UXIE_CAUGHT, Nabla_ThreeLakes_EventScript_ShowUxie
	call_if_unset FLAG_NABLA_MESPRIT_CAUGHT, Nabla_ThreeLakes_EventScript_ShowMesprit
	call_if_unset FLAG_NABLA_AZELF_CAUGHT, Nabla_ThreeLakes_EventScript_ShowAzelf
	return

Nabla_ThreeLakes_EventScript_ShowUxie:
	clearflag FLAG_TEMP_11
	return

Nabla_ThreeLakes_EventScript_ShowMesprit:
	clearflag FLAG_TEMP_12
	return

Nabla_ThreeLakes_EventScript_ShowAzelf:
	clearflag FLAG_TEMP_13
	return

Nabla_ThreeLakes_EventScript_Uxie::
	setvar VAR_0x8004, SPECIES_UXIE
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_UXIE_CAUGHT
	release
	end

Nabla_ThreeLakes_EventScript_Mesprit::
	setvar VAR_0x8004, SPECIES_MESPRIT
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_MESPRIT_CAUGHT
	release
	end

Nabla_ThreeLakes_EventScript_Azelf::
	setvar VAR_0x8004, SPECIES_AZELF
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_AZELF_CAUGHT
	release
	end

@ Spear Pillar: Dialga, Palkia and Giratina on the roof and its ledge (the place is in the list of the Eon Flute
@ once Uxie, Mesprit and Azelf are caught); Arceus appears at the altar when the three are in the party
Nabla_SpearPillar_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ Dialga
	setflag FLAG_TEMP_12  @ Palkia
	setflag FLAG_TEMP_13  @ Giratina
	setflag FLAG_TEMP_14  @ Arceus
	call_if_unset FLAG_NABLA_DIALGA_CAUGHT, Nabla_SpearPillar_EventScript_ShowDialga
	call_if_unset FLAG_NABLA_PALKIA_CAUGHT, Nabla_SpearPillar_EventScript_ShowPalkia
	call_if_unset FLAG_NABLA_GIRATINA_CAUGHT, Nabla_SpearPillar_EventScript_ShowGiratina
	return

Nabla_SpearPillar_EventScript_ShowDialga:
	clearflag FLAG_TEMP_11
	return

Nabla_SpearPillar_EventScript_ShowPalkia:
	clearflag FLAG_TEMP_12
	return

Nabla_SpearPillar_EventScript_ShowGiratina:
	clearflag FLAG_TEMP_13
	return

Nabla_SpearPillar_EventScript_Dialga::
	setvar VAR_0x8004, SPECIES_DIALGA
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_DIALGA_CAUGHT
	release
	end

Nabla_SpearPillar_EventScript_Palkia::
	setvar VAR_0x8004, SPECIES_PALKIA
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_PALKIA_CAUGHT
	release
	end

Nabla_SpearPillar_EventScript_Giratina::
	setvar VAR_0x8004, SPECIES_GIRATINA
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_GIRATINA_CAUGHT
	release
	end

Nabla_SpearPillar_EventScript_Arceus::
	setvar VAR_0x8004, SPECIES_ARCEUS
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_ARCEUS_CAUGHT
	release
	end

@ The altar: with Dialga, Palkia and Giratina in the party, Arceus appears behind it (until the player leaves)
Nabla_SpearPillar_EventScript_Altar::
	lock
	goto_if_set FLAG_NABLA_ARCEUS_CAUGHT, Nabla_SpearPillar_EventScript_AltarQuiet
	goto_if_unset FLAG_TEMP_14, Nabla_SpearPillar_EventScript_AltarQuiet
	setvar VAR_0x8004, SPECIES_DIALGA
	specialvar VAR_RESULT, NablaMirage_PartyHasSpecies
	goto_if_eq VAR_RESULT, FALSE, Nabla_SpearPillar_EventScript_AltarWaits
	setvar VAR_0x8004, SPECIES_PALKIA
	specialvar VAR_RESULT, NablaMirage_PartyHasSpecies
	goto_if_eq VAR_RESULT, FALSE, Nabla_SpearPillar_EventScript_AltarWaits
	setvar VAR_0x8004, SPECIES_GIRATINA
	specialvar VAR_RESULT, NablaMirage_PartyHasSpecies
	goto_if_eq VAR_RESULT, FALSE, Nabla_SpearPillar_EventScript_AltarWaits
	msgbox Nabla_Text_SpearPillarAltarAwakens, MSGBOX_DEFAULT
	closemessage
	playmoncry SPECIES_ARCEUS, CRY_MODE_ENCOUNTER
	fadescreenswapbuffers FADE_TO_WHITE
	clearflag FLAG_TEMP_14
	addobject LOCALID_SPEAR_PILLAR_ARCEUS
	fadescreenswapbuffers FADE_FROM_WHITE
	waitmoncry
	release
	end

Nabla_SpearPillar_EventScript_AltarWaits:
	msgbox Nabla_Text_SpearPillarAltarWaits, MSGBOX_DEFAULT
	release
	end

Nabla_SpearPillar_EventScript_AltarQuiet:
	msgbox Nabla_Text_SpearPillarAltar, MSGBOX_DEFAULT
	release
	end

@ Stark Mountain: Heatran by the lava, Volcanion on the ledge to the east
Nabla_StarkMountain_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ Heatran
	setflag FLAG_TEMP_12  @ Volcanion
	call_if_unset FLAG_NABLA_HEATRAN_CAUGHT, Nabla_StarkMountain_EventScript_ShowHeatran
	call_if_unset FLAG_NABLA_VOLCANION_CAUGHT, Nabla_StarkMountain_EventScript_ShowVolcanion
	return

Nabla_StarkMountain_EventScript_ShowHeatran:
	clearflag FLAG_TEMP_11
	return

Nabla_StarkMountain_EventScript_ShowVolcanion:
	clearflag FLAG_TEMP_12
	return

Nabla_StarkMountain_EventScript_Heatran::
	setvar VAR_0x8004, SPECIES_HEATRAN
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_HEATRAN_CAUGHT
	release
	end

Nabla_StarkMountain_EventScript_Volcanion::
	setvar VAR_0x8004, SPECIES_VOLCANION
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_VOLCANION_CAUGHT
	release
	end
