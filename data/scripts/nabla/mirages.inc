

@ Flower Paradise: Shaymin in the field of flowers, Zarude in the jungle
Nabla_FlowerParadise_EventScript_SetUp::
	setflag FLAG_TEMP_HIDE_FOLLOWER
	setflag FLAG_TEMP_11  @ Shaymin
	setflag FLAG_TEMP_12  @ Zarude
	call_if_unset FLAG_NABLA_SHAYMIN_CAUGHT, Nabla_FlowerParadise_EventScript_ShowShaymin
	call_if_unset FLAG_NABLA_ZARUDE_CAUGHT, Nabla_FlowerParadise_EventScript_ShowZarude
	return

Nabla_FlowerParadise_EventScript_ShowShaymin:
	clearflag FLAG_TEMP_11
	return

Nabla_FlowerParadise_EventScript_ShowZarude:
	clearflag FLAG_TEMP_12
	return

Nabla_FlowerParadise_EventScript_Shaymin::
	setvar VAR_0x8004, SPECIES_SHAYMIN
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_SHAYMIN_CAUGHT
	release
	end

Nabla_FlowerParadise_EventScript_Zarude::
	setvar VAR_0x8004, SPECIES_ZARUDE
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_ZARUDE_CAUGHT
	release
	end
