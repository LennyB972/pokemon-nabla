@ Route 111: ancient carvings on the rock of the Desert Ruins, on both sides of the entrance.
@ A Galarian Yamask that has lost at least 49 HP evolves into Runerigus when the player reads
@ them, as under the stone arch of Sword/Shield.
Nabla_EventScript_Route111AncientCarvings::
	lockall
	msgbox Nabla_Text_Route111AncientCarvings, MSGBOX_DEFAULT
	closemessage
	tryspecialevo EVO_TRIGGER_TABLET_CURSE, TRUE, TRUE
	releaseall
	end
