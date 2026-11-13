@ The Sealed Chamber after the League (docs/nabla/postgame.md): closed until then by a current under Route 134
@ (Underwater_SealedChamber, coord event on the way up), which also keeps the caves of the three Regis closed.
@ Regieleki and Regidrago wait in its inner room; Regigigas appears when the back wall is read with Regirock, Regice
@ and Registeel in the party. They are legendaries of the mirages' model (data/scripts/nabla/mirages.inc).

Nabla_SealedChamber_EventScript_Current::
	goto_if_set FLAG_SYS_GAME_CLEAR, Nabla_SealedChamber_EventScript_NoCurrent
	lockall
	msgbox Nabla_Text_SealedChamberCurrent, MSGBOX_DEFAULT
	closemessage
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_WalkDown
	waitmovement 0
	releaseall
Nabla_SealedChamber_EventScript_NoCurrent:
	end

Nabla_SealedChamber_OnTransition::
	setflag FLAG_TEMP_11  @ Regieleki
	setflag FLAG_TEMP_12  @ Regidrago
	setflag FLAG_TEMP_13  @ Regigigas
	call_if_unset FLAG_NABLA_REGIELEKI_CAUGHT, Nabla_SealedChamber_EventScript_ShowRegieleki
	call_if_unset FLAG_NABLA_REGIDRAGO_CAUGHT, Nabla_SealedChamber_EventScript_ShowRegidrago
	end

Nabla_SealedChamber_EventScript_ShowRegieleki:
	clearflag FLAG_TEMP_11
	return

Nabla_SealedChamber_EventScript_ShowRegidrago:
	clearflag FLAG_TEMP_12
	return

Nabla_SealedChamber_EventScript_Regieleki::
	setvar VAR_0x8004, SPECIES_REGIELEKI
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_REGIELEKI_CAUGHT
	release
	end

Nabla_SealedChamber_EventScript_Regidrago::
	setvar VAR_0x8004, SPECIES_REGIDRAGO
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_REGIDRAGO_CAUGHT
	release
	end

Nabla_SealedChamber_EventScript_Regigigas::
	setvar VAR_0x8004, SPECIES_REGIGIGAS
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_REGIGIGAS_CAUGHT
	release
	end

@ Called by the back wall of the inner room, after its braille: Regigigas appears (cry, white flash) if it is neither
@ caught nor there and Regirock, Regice and Registeel are in the party; otherwise the wall goes on as in Emerald.
Nabla_SealedChamber_EventScript_BackWall::
	goto_if_set FLAG_NABLA_REGIGIGAS_CAUGHT, Nabla_SealedChamber_EventScript_BackWallEnd
	goto_if_unset FLAG_TEMP_13, Nabla_SealedChamber_EventScript_BackWallEnd
	setvar VAR_0x8004, SPECIES_REGIROCK
	specialvar VAR_RESULT, NablaMirage_PartyHasSpecies
	goto_if_eq VAR_RESULT, FALSE, Nabla_SealedChamber_EventScript_BackWallEnd
	setvar VAR_0x8004, SPECIES_REGICE
	specialvar VAR_RESULT, NablaMirage_PartyHasSpecies
	goto_if_eq VAR_RESULT, FALSE, Nabla_SealedChamber_EventScript_BackWallEnd
	setvar VAR_0x8004, SPECIES_REGISTEEL
	specialvar VAR_RESULT, NablaMirage_PartyHasSpecies
	goto_if_eq VAR_RESULT, FALSE, Nabla_SealedChamber_EventScript_BackWallEnd
	msgbox Nabla_Text_SealedChamberRegisReact, MSGBOX_DEFAULT
	closemessage
	playmoncry SPECIES_REGIGIGAS, CRY_MODE_ENCOUNTER
	fadescreenswapbuffers FADE_TO_WHITE
	clearflag FLAG_TEMP_13
	addobject LOCALID_SEALED_CHAMBER_NABLA_REGIGIGAS
	fadescreenswapbuffers FADE_FROM_WHITE
	waitmoncry
	releaseall
	end
Nabla_SealedChamber_EventScript_BackWallEnd:
	return
