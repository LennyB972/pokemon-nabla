@ After the first Hall of Fame, MOM tells the player that the LEAGUE's gift is in their PC,
@ and that Steven waits for them at his house (data/scripts/nabla/eon_flute.inc)
Nabla_PlayersHouse_EventScript_LeagueGift::
	addpcitem ITEM_EXP_CANDY_XL, 150
	addpcitem ITEM_RARE_CANDY, 50
	msgbox Nabla_Text_MomLeagueGift, MSGBOX_DEFAULT
	clearflag FLAG_HIDE_MOSSDEEP_CITY_STEVENS_HOUSE_STEVEN
	msgbox Nabla_Text_MomStevenCameBy, MSGBOX_DEFAULT
	return
