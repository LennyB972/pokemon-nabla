NablaDiamondMine_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaDiamondMine_OnTransition
	.byte 0

NablaDiamondMine_OnTransition:
	call Nabla_DiamondMine_EventScript_SetUp
	end
