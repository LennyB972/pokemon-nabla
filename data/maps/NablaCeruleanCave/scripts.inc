NablaCeruleanCave_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaCeruleanCave_OnTransition
	.byte 0

NablaCeruleanCave_OnTransition:
	call Nabla_CeruleanCave_EventScript_SetUp
	end
