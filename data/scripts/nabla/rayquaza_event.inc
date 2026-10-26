@ After the eighth Gym, Steven sends the player to the top of Sky Pillar, where a weakened Rayquaza
@ appears. It eats the player's METEORITE, learns Dragon Ascent and battles until it is caught, then
@ joins the party at its head (with a full party, the player has to send a Pokémon to the PC); then
@ Deoxys appears (it comes back after the League while it is not caught). Victory Road waits until
@ the end of the event, and Sky Pillar's floors stay whole until then. Since Rayquaza ate the
@ METEORITE, the white rock of Mossdeep City changes the form of Deoxys (src/nabla_rayquaza_event.c).

@ Sootopolis City

@ Called from SootopolisCity_OnTransition
Nabla_SootopolisCity_EventScript_SetUpStevenCall::
	setflag FLAG_NABLA_HIDE_SOOTOPOLIS_STEVEN
	goto_if_unset FLAG_BADGE08_GET, Common_EventScript_NopReturn
	goto_if_set FLAG_NABLA_SKY_PILLAR_CALL, Common_EventScript_NopReturn
	clearflag FLAG_NABLA_HIDE_SOOTOPOLIS_STEVEN
	setvar VAR_TEMP_1, 1
	return

@ Coming out of the Gym, Steven walks up to the player. Arriving another way, the player talks to him.
Nabla_SootopolisCity_EventScript_StevenComesUp::
	setvar VAR_TEMP_1, 0
	getplayerxy VAR_0x8004, VAR_0x8005
	goto_if_ne VAR_0x8004, 31, Nabla_SootopolisCity_EventScript_StevenWaits
	goto_if_ne VAR_0x8005, 33, Nabla_SootopolisCity_EventScript_StevenWaits
	lockall
	applymovement LOCALID_SOOTOPOLIS_NABLA_STEVEN, Common_Movement_ExclamationMark
	waitmovement 0
	applymovement LOCALID_SOOTOPOLIS_NABLA_STEVEN, Nabla_SootopolisCity_Movement_StevenComesUp
	waitmovement 0
	goto Nabla_SootopolisCity_EventScript_StevenCall

Nabla_SootopolisCity_EventScript_StevenWaits::
	end

Nabla_SootopolisCity_EventScript_Steven::
	lockall
	faceplayer
	goto Nabla_SootopolisCity_EventScript_StevenCall

Nabla_SootopolisCity_EventScript_StevenCall::
	msgbox Nabla_Text_StevenSootopolisCall, MSGBOX_DEFAULT
	closemessage
	fadescreenswapbuffers FADE_TO_BLACK
	removeobject LOCALID_SOOTOPOLIS_NABLA_STEVEN
	fadescreenswapbuffers FADE_FROM_BLACK
	setflag FLAG_NABLA_SKY_PILLAR_CALL
	releaseall
	end

Nabla_SootopolisCity_Movement_StevenComesUp:
	walk_up
	walk_up
	step_end

@ Ever Grande City

@ Called from EverGrandeCity_OnTransition
Nabla_EverGrandeCity_EventScript_SetUpVictoryRoadBlock::
	goto_if_set FLAG_NABLA_SKY_PILLAR_DONE, Common_EventScript_NopReturn
	setvar VAR_TEMP_2, 1
	return

Nabla_EverGrandeCity_EventScript_VictoryRoadBlocked::
	lockall
	msgbox Nabla_Text_VictoryRoadBlocked, MSGBOX_DEFAULT
	closemessage
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_WalkDown
	waitmovement 0
	releaseall
	end

@ Sky Pillar

@ Called from SkyPillar_Top_OnTransition. Emerald's Rayquaza at the top is only met in this event.
Nabla_SkyPillar_Top_EventScript_SetUpEvent::
	setflag FLAG_HIDE_SKY_PILLAR_TOP_RAYQUAZA_STILL
	setflag FLAG_NABLA_HIDE_SKY_PILLAR_STEVEN
	setflag FLAG_NABLA_HIDE_SKY_PILLAR_RAYQUAZA
	setflag FLAG_NABLA_HIDE_SKY_PILLAR_DEOXYS
	goto_if_set FLAG_NABLA_SKY_PILLAR_DONE, Nabla_SkyPillar_Top_EventScript_TryShowDeoxys
	call SkyPillar_Top_EventScript_SetCleanLayout
	goto_if_unset FLAG_NABLA_SKY_PILLAR_CALL, Common_EventScript_NopReturn
	clearflag FLAG_NABLA_HIDE_SKY_PILLAR_STEVEN
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setvar VAR_TEMP_1, 1
	return

Nabla_SkyPillar_Top_EventScript_TryShowDeoxys::
	goto_if_unset FLAG_SYS_GAME_CLEAR, Common_EventScript_NopReturn
	goto_if_set FLAG_NABLA_DEOXYS_CAUGHT, Common_EventScript_NopReturn
	clearflag FLAG_NABLA_HIDE_SKY_PILLAR_DEOXYS
	return

@ Reaching the top of the stairs, the player walks up to Steven
Nabla_SkyPillar_Top_EventScript_StairsLeft::
	lockall
	applymovement OBJ_EVENT_ID_PLAYER, Nabla_SkyPillar_Top_Movement_PlayerFromStairsLeft
	waitmovement 0
	goto Nabla_SkyPillar_Top_EventScript_StevenScene

Nabla_SkyPillar_Top_EventScript_StairsRight::
	lockall
	applymovement OBJ_EVENT_ID_PLAYER, Nabla_SkyPillar_Top_Movement_PlayerFromStairsRight
	waitmovement 0
	goto Nabla_SkyPillar_Top_EventScript_StevenScene

Nabla_SkyPillar_Top_EventScript_Steven::
	lockall
	goto Nabla_SkyPillar_Top_EventScript_StevenScene

Nabla_SkyPillar_Top_EventScript_StevenScene::
	setvar VAR_TEMP_1, 0
	call Nabla_SkyPillar_Top_EventScript_FaceEachOther
	goto_if_set FLAG_NABLA_RAYQUAZA_CAUGHT, Nabla_SkyPillar_Top_EventScript_DeoxysAppears
	msgbox Nabla_Text_StevenYouMadeIt, MSGBOX_DEFAULT
	closemessage
	call Nabla_SkyPillar_Top_EventScript_FaceUp
	playmoncry SPECIES_RAYQUAZA, CRY_MODE_WEAK
	clearflag FLAG_NABLA_HIDE_SKY_PILLAR_RAYQUAZA
	addobject LOCALID_SKY_PILLAR_TOP_NABLA_RAYQUAZA
	applymovement LOCALID_SKY_PILLAR_TOP_NABLA_RAYQUAZA, Nabla_SkyPillar_Top_Movement_RayquazaComesDown
	waitmovement 0
	waitmoncry
	msgbox Nabla_Text_StevenRayquazaIsExhausted, MSGBOX_DEFAULT
	closemessage
	playse SE_M_COSMIC_POWER
	waitse
	msgbox Nabla_Text_MeteoriteIsGlowing, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_SKY_PILLAR_TOP_NABLA_RAYQUAZA, Nabla_SkyPillar_Top_Movement_RayquazaOpensMouth
	waitmovement 0
	removeitem ITEM_METEORITE
	msgbox Nabla_Text_RayquazaAteMeteorite, MSGBOX_DEFAULT
	closemessage
	playmoncry SPECIES_RAYQUAZA, CRY_MODE_ENCOUNTER
	setvar VAR_0x8004, 1  @ vertical pan
	setvar VAR_0x8005, 2  @ horizontal pan
	setvar VAR_0x8006, 8  @ num shakes
	setvar VAR_0x8007, 5  @ shake delay
	special ShakeCamera
	waitstate
	waitmoncry
	applymovement LOCALID_SKY_PILLAR_TOP_NABLA_RAYQUAZA, Nabla_SkyPillar_Top_Movement_RayquazaStandsUp
	waitmovement 0
	msgbox Nabla_Text_StevenRayquazaTestsYou, MSGBOX_DEFAULT
	closemessage
Nabla_SkyPillar_Top_EventScript_BattleRayquaza::
	setwildbattle SPECIES_RAYQUAZA, NABLA_SKY_PILLAR_LEGENDARIES_LEVEL
	createmon 1, 0, SPECIES_RAYQUAZA, NABLA_SKY_PILLAR_LEGENDARIES_LEVEL, move1=MOVE_DRAGON_ASCENT, move2=MOVE_EXTREME_SPEED, move3=MOVE_DRAGON_DANCE, move4=MOVE_DRAGON_PULSE
	special BattleSetup_StartLegendaryBattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, Nabla_SkyPillar_Top_EventScript_CaughtRayquaza
	msgbox Nabla_Text_RayquazaWantsToBattleAgain, MSGBOX_DEFAULT
	closemessage
	goto Nabla_SkyPillar_Top_EventScript_BattleRayquaza

Nabla_SkyPillar_Top_EventScript_CaughtRayquaza::
	setflag FLAG_NABLA_RAYQUAZA_CAUGHT
	fadescreenswapbuffers FADE_TO_BLACK
	removeobject LOCALID_SKY_PILLAR_TOP_NABLA_RAYQUAZA
	fadescreenswapbuffers FADE_FROM_BLACK
	specialvar VAR_RESULT, NablaRayquazaEvent_PutRayquazaFirst
	call_if_eq VAR_RESULT, FALSE, Nabla_SkyPillar_Top_EventScript_RayquazaJoinsFullParty
	call Nabla_SkyPillar_Top_EventScript_FaceEachOther
	msgbox Nabla_Text_StevenRayquazaChoseYou, MSGBOX_DEFAULT
Nabla_SkyPillar_Top_EventScript_DeoxysAppears::
	msgbox Nabla_Text_StevenSomethingIsComing, MSGBOX_DEFAULT
	closemessage
	call Nabla_SkyPillar_Top_EventScript_FaceUp
	playse SE_M_COSMIC_POWER
	fadescreenswapbuffers FADE_TO_WHITE
	clearflag FLAG_NABLA_HIDE_SKY_PILLAR_DEOXYS
	addobject LOCALID_SKY_PILLAR_TOP_NABLA_DEOXYS
	fadescreenswapbuffers FADE_FROM_WHITE
	waitse
	playmoncry SPECIES_DEOXYS, CRY_MODE_ENCOUNTER
	waitmoncry
	msgbox Nabla_Text_StevenDeoxysFollowedMeteorite, MSGBOX_DEFAULT
	closemessage
	call Nabla_SkyPillar_Top_EventScript_BattleDeoxys
	call Nabla_SkyPillar_Top_EventScript_FaceEachOther
	msgbox Nabla_Text_StevenVictoryRoadAwaits, MSGBOX_DEFAULT
	closemessage
	fadescreenswapbuffers FADE_TO_BLACK
	removeobject LOCALID_SKY_PILLAR_TOP_NABLA_STEVEN
	fadescreenswapbuffers FADE_FROM_BLACK
	setflag FLAG_NABLA_SKY_PILLAR_DONE
	releaseall
	end

@ After the League, while Deoxys is not caught
Nabla_SkyPillar_Top_EventScript_Deoxys::
	lockall
	waitse
	playmoncry SPECIES_DEOXYS, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	call Nabla_SkyPillar_Top_EventScript_BattleDeoxys
	releaseall
	end

Nabla_SkyPillar_Top_EventScript_BattleDeoxys::
	setwildbattle SPECIES_DEOXYS, NABLA_SKY_PILLAR_LEGENDARIES_LEVEL
	special BattleSetup_StartLegendaryBattle
	specialvar VAR_RESULT, GetBattleOutcome
	call_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, Nabla_SkyPillar_Top_EventScript_SetDeoxysCaught
	fadescreenswapbuffers FADE_TO_BLACK
	removeobject LOCALID_SKY_PILLAR_TOP_NABLA_DEOXYS
	fadescreenswapbuffers FADE_FROM_BLACK
	goto_if_set FLAG_NABLA_DEOXYS_CAUGHT, Common_EventScript_NopReturn
	bufferspeciesname STR_VAR_1, SPECIES_DEOXYS
	msgbox gText_LegendaryFlewAway, MSGBOX_DEFAULT
	closemessage
	return

@ Rayquaza went to the PC: the player sends a Pokémon there instead
Nabla_SkyPillar_Top_EventScript_RayquazaJoinsFullParty::
	msgbox Nabla_Text_RayquazaWantsToStayWithYou, MSGBOX_DEFAULT
	closemessage
	special ChoosePartyMon
	goto_if_ge VAR_0x8004, PARTY_SIZE, Nabla_SkyPillar_Top_EventScript_RayquazaJoinsFullParty
	bufferpartymonnick STR_VAR_1, VAR_0x8004
	special NablaRayquazaEvent_SwapRayquazaIntoParty
	msgbox Nabla_Text_MonWentToPC, MSGBOX_DEFAULT
	closemessage
	return

Nabla_SkyPillar_Top_EventScript_SetDeoxysCaught::
	setflag FLAG_NABLA_DEOXYS_CAUGHT
	return

Nabla_SkyPillar_Top_EventScript_FaceEachOther::
	applymovement LOCALID_SKY_PILLAR_TOP_NABLA_STEVEN, Common_Movement_FaceRight
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_FaceLeft
	waitmovement 0
	return

Nabla_SkyPillar_Top_EventScript_FaceUp::
	applymovement LOCALID_SKY_PILLAR_TOP_NABLA_STEVEN, Common_Movement_FaceUp
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_FaceUp
	waitmovement 0
	return

Nabla_SkyPillar_Top_Movement_PlayerFromStairsLeft:
	walk_right
Nabla_SkyPillar_Top_Movement_PlayerFromStairsRight:
	walk_right
	walk_right
	walk_up
	walk_up
	walk_up
	step_end

@ Rayquaza has unusual movement frames (see SkyPillar_Top_Movement_RayquazaFlyOff): facing up while
@ sliding down keeps it flying
Nabla_SkyPillar_Top_Movement_RayquazaComesDown:
	face_up
	lock_facing_direction
	slide_down
	slide_down
	slide_down
	slide_down
	slide_down
	slide_down
	unlock_facing_direction
	walk_in_place_down  @ Coiled, asleep
	step_end

Nabla_SkyPillar_Top_Movement_RayquazaOpensMouth:
	walk_in_place_left  @ Coiled, mouth open
	delay_16
	delay_16
	step_end

Nabla_SkyPillar_Top_Movement_RayquazaStandsUp:
	walk_in_place_right  @ Normal, awake
	step_end

@ Fallarbor Town: Prof. Cozmo lets the player keep the METEORITE and gives the TM anyway

@ Instead of the original exchange (FallarborTown_CozmosHouse_EventScript_PlayerHasMeteorite)
Nabla_FallarborTown_EventScript_CozmoKeepTheMeteorite::
	msgbox Nabla_Text_CozmoKeepTheMeteorite, MSGBOX_DEFAULT
	giveitem ITEM_TM_RETURN
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	setflag FLAG_RECEIVED_TM_RETURN
	release
	end

@ Mossdeep City: the white rock changes the form of Deoxys

Nabla_MossdeepCity_EventScript_WhiteRock::
	lockall
	specialvar VAR_RESULT, NablaWhiteRock_HasFormChangeMon
	goto_if_eq VAR_RESULT, FALSE, Nabla_MossdeepCity_EventScript_JustAWhiteRock
	msgbox Nabla_Text_WhiteRockReacts, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Nabla_MossdeepCity_EventScript_WhiteRockEnd
	special ChoosePartyMon
	goto_if_ge VAR_0x8004, PARTY_SIZE, Nabla_MossdeepCity_EventScript_WhiteRockEnd
	specialvar VAR_RESULT, NablaWhiteRock_TryFormChange
	goto_if_eq VAR_RESULT, FALSE, Nabla_MossdeepCity_EventScript_WhiteRockNothing
	bufferpartymonnick STR_VAR_1, VAR_0x8004
	playse SE_M_COSMIC_POWER
	waitse
	msgbox Nabla_Text_WhiteRockFormChanged, MSGBOX_DEFAULT
	releaseall
	end

Nabla_MossdeepCity_EventScript_JustAWhiteRock::
	msgbox MossdeepCity_Text_ItsAWhiteRock, MSGBOX_DEFAULT
	releaseall
	end

Nabla_MossdeepCity_EventScript_WhiteRockNothing::
	msgbox Nabla_Text_WhiteRockNothingHappened, MSGBOX_DEFAULT
Nabla_MossdeepCity_EventScript_WhiteRockEnd::
	releaseall
	end
