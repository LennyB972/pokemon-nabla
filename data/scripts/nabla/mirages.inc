@ Legendary Pokémon of the places the Eon Flute leads to (docs/nabla/postgame.md). Each one is an object, visible
@ until it is caught (one FLAG_NABLA_*_CAUGHT each), hidden by a temporary flag set when entering the map.

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
