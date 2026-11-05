NablaDragonspiral_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaDragonspiral_OnTransition
	.byte 0

NablaDragonspiral_OnTransition:
	call Nabla_Dragonspiral_EventScript_SetUp
	end
