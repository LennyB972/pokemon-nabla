@ Lilycove Department Store 3F clerk selling the items that replace trade evolutions.
Nabla_EventScript_EvolutionItemsClerk::
	lock
	faceplayer
	message Nabla_Text_EvolutionItemsClerk
	waitmessage
	pokemart Nabla_Pokemart_EvolutionItems
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

	.align 2
Nabla_Pokemart_EvolutionItems:
	.2byte ITEM_LINKING_CORD
	.2byte ITEM_KINGS_ROCK
	.2byte ITEM_METAL_COAT
	.2byte ITEM_DRAGON_SCALE
	.2byte ITEM_UPGRADE
	.2byte ITEM_DUBIOUS_DISC
	.2byte ITEM_PROTECTOR
	.2byte ITEM_ELECTIRIZER
	.2byte ITEM_MAGMARIZER
	.2byte ITEM_REAPER_CLOTH
	.2byte ITEM_DEEP_SEA_TOOTH
	.2byte ITEM_DEEP_SEA_SCALE
	.2byte ITEM_PRISM_SCALE
	.2byte ITEM_SACHET
	.2byte ITEM_WHIPPED_DREAM
	pokemartlistend
