@ The assistant of Prof. Birch's lab after the League (docs/nabla/postgame.md, 7.5): shown a Pokémon of the party,
@ he gives the items that go with it and are not in the bag (src/nabla_lab_assistant.c), or helps Keldeo and
@ Meloetta remember their move. Hidden by a temporary flag until the League.

Nabla_LabAssistant_EventScript_SetUp::
	goto_if_set FLAG_SYS_GAME_CLEAR, Nabla_LabAssistant_EventScript_SetUpEnd
	setflag FLAG_TEMP_11
Nabla_LabAssistant_EventScript_SetUpEnd:
	return

Nabla_LabAssistant_EventScript_Assistant::
	lock
	faceplayer
	msgbox Nabla_Text_LabAssistantShowMe, MSGBOX_DEFAULT
	special ChoosePartyMon
	goto_if_ge VAR_0x8004, PARTY_SIZE, Nabla_LabAssistant_EventScript_Bye
	specialvar VAR_RESULT, NablaLabAssistant_Check
	switch VAR_RESULT
	case LAB_ASSISTANT_NOTHING, Nabla_LabAssistant_EventScript_Nothing
	case LAB_ASSISTANT_HAS_ALL, Nabla_LabAssistant_EventScript_HasAll
	case LAB_ASSISTANT_MANY_ITEMS, Nabla_LabAssistant_EventScript_GiveAll
	case LAB_ASSISTANT_SECRET_MOVE, Nabla_LabAssistant_EventScript_SecretMove
	msgbox Nabla_Text_LabAssistantHereYouGo, MSGBOX_DEFAULT
Nabla_LabAssistant_EventScript_GiveNext:
	specialvar VAR_RESULT, NablaLabAssistant_NextItem
	goto_if_eq VAR_RESULT, ITEM_NONE, Nabla_LabAssistant_EventScript_Done
	copyvar VAR_0x8005, VAR_RESULT
	giveitem VAR_0x8005
	goto_if_eq VAR_RESULT, FALSE, Nabla_LabAssistant_EventScript_Done
	goto Nabla_LabAssistant_EventScript_GiveNext

Nabla_LabAssistant_EventScript_GiveAll:
	msgbox Nabla_Text_LabAssistantHereYouGo, MSGBOX_DEFAULT
	specialvar VAR_RESULT, NablaLabAssistant_GiveAllItems
	goto_if_eq VAR_RESULT, 0, Nabla_LabAssistant_EventScript_BagFull
	playfanfare MUS_OBTAIN_ITEM
	message Nabla_Text_LabAssistantReceivedItems
	waitmessage
	waitfanfare
	msgbox Nabla_Text_LabAssistantPutAway, MSGBOX_DEFAULT
	goto Nabla_LabAssistant_EventScript_Done

Nabla_LabAssistant_EventScript_BagFull:
	msgbox gText_TooBadBagIsFull, MSGBOX_DEFAULT
	release
	end

Nabla_LabAssistant_EventScript_SecretMove:
	special Special_HasMoveToRelearn
	goto_if_eq VAR_RESULT, FALSE, Nabla_LabAssistant_EventScript_Nothing
	msgbox Nabla_Text_LabAssistantSecretMove, MSGBOX_DEFAULT
	setmoverelearnerstate MOVE_RELEARNER_LEVEL_UP_MOVES
	special TeachMoveRelearnerMove
	goto Nabla_LabAssistant_EventScript_Done

Nabla_LabAssistant_EventScript_Nothing:
	msgbox Nabla_Text_LabAssistantNothing, MSGBOX_DEFAULT
	release
	end

Nabla_LabAssistant_EventScript_HasAll:
	msgbox Nabla_Text_LabAssistantHasAll, MSGBOX_DEFAULT
	release
	end

Nabla_LabAssistant_EventScript_Done:
	msgbox Nabla_Text_LabAssistantComeBack, MSGBOX_DEFAULT
	release
	end

Nabla_LabAssistant_EventScript_Bye:
	msgbox Nabla_Text_LabAssistantBye, MSGBOX_DEFAULT
	release
	end
