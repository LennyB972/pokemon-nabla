@ Pokémon League (1F): the Hyper Trainer raises the IVs of a Pokémon to the max with Bottle Caps
@ (one stat with a Bottle Cap, all of them with a Gold Bottle Cap), with the native canhypertrain / hypertrain.
@ Stats are given by their number in enum Stat: 0 HP, 1 Attack, 2 Defense, 3 Speed, 4 Sp. Atk, 5 Sp. Def.
Nabla_EventScript_HyperTrainer::
	lock
	faceplayer
	msgbox Nabla_Text_HyperTrainerIntro, MSGBOX_DEFAULT
	checkitem ITEM_BOTTLE_CAP
	copyvar VAR_0x8005, VAR_RESULT
	checkitem ITEM_GOLD_BOTTLE_CAP
	copyvar VAR_0x8006, VAR_RESULT
	goto_if_eq VAR_0x8005, TRUE, Nabla_EventScript_HyperTrainerChooseMon
	goto_if_eq VAR_0x8006, TRUE, Nabla_EventScript_HyperTrainerChooseMon
	msgbox Nabla_Text_HyperTrainerNoBottleCap, MSGBOX_DEFAULT
	release
	end

Nabla_EventScript_HyperTrainerChooseMon:
	msgbox Nabla_Text_HyperTrainerWhichMon, MSGBOX_DEFAULT
	special ChoosePartyMon
	goto_if_ge VAR_0x8004, PARTY_SIZE, Nabla_EventScript_HyperTrainerCancel
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
	goto_if_eq VAR_RESULT, SPECIES_EGG, Nabla_EventScript_HyperTrainerEgg
	bufferpartymonnick STR_VAR_1, VAR_0x8004
	goto_if_eq VAR_0x8005, FALSE, Nabla_EventScript_HyperTrainerGoldBottleCap
	goto_if_eq VAR_0x8006, FALSE, Nabla_EventScript_HyperTrainerBottleCap
	msgbox Nabla_Text_HyperTrainerWhichBottleCap, MSGBOX_DEFAULT
	dynmultichoice 0, 0, FALSE, 2, 0, DYN_MULTICHOICE_CB_NONE, Nabla_Text_BottleCap, Nabla_Text_GoldBottleCap
	switch VAR_RESULT
	case 0, Nabla_EventScript_HyperTrainerBottleCap
	case 1, Nabla_EventScript_HyperTrainerGoldBottleCap
	goto Nabla_EventScript_HyperTrainerCancel

@ Bottle Cap: one stat
Nabla_EventScript_HyperTrainerBottleCap:
	msgbox Nabla_Text_HyperTrainerWhichStat, MSGBOX_DEFAULT
	dynmultichoice 0, 0, FALSE, 6, 0, DYN_MULTICHOICE_CB_NONE, Nabla_Text_StatHP, Nabla_Text_StatAttack, Nabla_Text_StatDefense, Nabla_Text_StatSpAtk, Nabla_Text_StatSpDef, Nabla_Text_StatSpeed
	switch VAR_RESULT
	case 0, Nabla_EventScript_HyperTrainHP
	case 1, Nabla_EventScript_HyperTrainAttack
	case 2, Nabla_EventScript_HyperTrainDefense
	case 3, Nabla_EventScript_HyperTrainSpAtk
	case 4, Nabla_EventScript_HyperTrainSpDef
	case 5, Nabla_EventScript_HyperTrainSpeed
	goto Nabla_EventScript_HyperTrainerCancel

Nabla_EventScript_HyperTrainHP:
	canhypertrain 0, VAR_0x8004
	goto_if_eq VAR_RESULT, FALSE, Nabla_EventScript_HyperTrainerAlreadyBest
	hypertrain 0, VAR_0x8004
	goto Nabla_EventScript_HyperTrainerUsedBottleCap

Nabla_EventScript_HyperTrainAttack:
	canhypertrain 1, VAR_0x8004
	goto_if_eq VAR_RESULT, FALSE, Nabla_EventScript_HyperTrainerAlreadyBest
	hypertrain 1, VAR_0x8004
	goto Nabla_EventScript_HyperTrainerUsedBottleCap

Nabla_EventScript_HyperTrainDefense:
	canhypertrain 2, VAR_0x8004
	goto_if_eq VAR_RESULT, FALSE, Nabla_EventScript_HyperTrainerAlreadyBest
	hypertrain 2, VAR_0x8004
	goto Nabla_EventScript_HyperTrainerUsedBottleCap

Nabla_EventScript_HyperTrainSpAtk:
	canhypertrain 4, VAR_0x8004
	goto_if_eq VAR_RESULT, FALSE, Nabla_EventScript_HyperTrainerAlreadyBest
	hypertrain 4, VAR_0x8004
	goto Nabla_EventScript_HyperTrainerUsedBottleCap

Nabla_EventScript_HyperTrainSpDef:
	canhypertrain 5, VAR_0x8004
	goto_if_eq VAR_RESULT, FALSE, Nabla_EventScript_HyperTrainerAlreadyBest
	hypertrain 5, VAR_0x8004
	goto Nabla_EventScript_HyperTrainerUsedBottleCap

Nabla_EventScript_HyperTrainSpeed:
	canhypertrain 3, VAR_0x8004
	goto_if_eq VAR_RESULT, FALSE, Nabla_EventScript_HyperTrainerAlreadyBest
	hypertrain 3, VAR_0x8004
Nabla_EventScript_HyperTrainerUsedBottleCap:
	removeitem ITEM_BOTTLE_CAP
	goto Nabla_EventScript_HyperTrainerDone

@ Gold Bottle Cap: every stat that is not at its best yet
Nabla_EventScript_HyperTrainerGoldBottleCap:
	setvar VAR_0x8007, FALSE
	canhypertrain 0, VAR_0x8004
	call_if_eq VAR_RESULT, TRUE, Nabla_EventScript_HyperTrainAllHP
	canhypertrain 1, VAR_0x8004
	call_if_eq VAR_RESULT, TRUE, Nabla_EventScript_HyperTrainAllAttack
	canhypertrain 2, VAR_0x8004
	call_if_eq VAR_RESULT, TRUE, Nabla_EventScript_HyperTrainAllDefense
	canhypertrain 3, VAR_0x8004
	call_if_eq VAR_RESULT, TRUE, Nabla_EventScript_HyperTrainAllSpeed
	canhypertrain 4, VAR_0x8004
	call_if_eq VAR_RESULT, TRUE, Nabla_EventScript_HyperTrainAllSpAtk
	canhypertrain 5, VAR_0x8004
	call_if_eq VAR_RESULT, TRUE, Nabla_EventScript_HyperTrainAllSpDef
	goto_if_eq VAR_0x8007, FALSE, Nabla_EventScript_HyperTrainerAlreadyBest
	removeitem ITEM_GOLD_BOTTLE_CAP
	goto Nabla_EventScript_HyperTrainerDone

Nabla_EventScript_HyperTrainAllHP:
	hypertrain 0, VAR_0x8004
	setvar VAR_0x8007, TRUE
	return

Nabla_EventScript_HyperTrainAllAttack:
	hypertrain 1, VAR_0x8004
	setvar VAR_0x8007, TRUE
	return

Nabla_EventScript_HyperTrainAllDefense:
	hypertrain 2, VAR_0x8004
	setvar VAR_0x8007, TRUE
	return

Nabla_EventScript_HyperTrainAllSpeed:
	hypertrain 3, VAR_0x8004
	setvar VAR_0x8007, TRUE
	return

Nabla_EventScript_HyperTrainAllSpAtk:
	hypertrain 4, VAR_0x8004
	setvar VAR_0x8007, TRUE
	return

Nabla_EventScript_HyperTrainAllSpDef:
	hypertrain 5, VAR_0x8004
	setvar VAR_0x8007, TRUE
	return

Nabla_EventScript_HyperTrainerDone:
	playfanfare MUS_LEVEL_UP
	msgbox Nabla_Text_HyperTrainerDone, MSGBOX_DEFAULT
	waitfanfare
	release
	end

Nabla_EventScript_HyperTrainerAlreadyBest:
	msgbox Nabla_Text_HyperTrainerAlreadyBest, MSGBOX_DEFAULT
	release
	end

Nabla_EventScript_HyperTrainerEgg:
	msgbox Nabla_Text_HyperTrainerEgg, MSGBOX_DEFAULT
	release
	end

Nabla_EventScript_HyperTrainerCancel:
	msgbox Nabla_Text_HyperTrainerCancel, MSGBOX_DEFAULT
	release
	end
