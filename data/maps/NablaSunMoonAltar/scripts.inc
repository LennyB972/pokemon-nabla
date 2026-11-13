NablaSunMoonAltar_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaSunMoonAltar_OnTransition
	.byte 0

NablaSunMoonAltar_OnTransition:
	call Nabla_SunMoonAltar_EventScript_SetUp
	end
