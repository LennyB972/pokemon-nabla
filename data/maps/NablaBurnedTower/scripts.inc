NablaBurnedTower_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaBurnedTower_OnTransition
	.byte 0

NablaBurnedTower_OnTransition:
	call Nabla_BurnedTower_EventScript_SetUp
	end
