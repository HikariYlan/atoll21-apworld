from __future__ import annotations

from BaseClasses import Item, ItemClassification

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import Atoll21World

ITEM_NAME_TO_ID = {
    "Double": 101,
    "Split": 102,
    "Insurance": 103,
    "Surrender": 104,
    "Dealer level up": 105,
    "Bet limit": 106,
    "Bet limit boost": 107,
    "Smaller chip": 108,
    "Bigger chip": 109,
    "Random chip color": 110,
    "Random table felt color": 111,
    "A nice drink on the side": 112,
    "Calm down for a bit": 113,
    "Fair and square": 114,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Double": ItemClassification.progression,
    "Split": ItemClassification.progression,
    "Insurance": ItemClassification.progression,
    "Surrender": ItemClassification.progression,
    "Dealer level up": ItemClassification.progression,
    "Bet limit": ItemClassification.progression,
    "Bet limit boost": ItemClassification.useful,
    "Smaller chip": ItemClassification.filler,
    "Bigger chip": ItemClassification.filler,
    "Random chip color": ItemClassification.filler,
    "Random table felt color": ItemClassification.filler,
    "A nice drink on the side": ItemClassification.trap,
    "Calm down for a bit": ItemClassification.trap,
    "Fair and square": ItemClassification.trap
}

class Atoll21Item(Item):
    game = "Atoll 21"

def get_random_filler_item_name(world: Atoll21World) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        trapChoice = world.random.randint(0, 2)
        match trapChoice:
            case 0:
                return "A nice drink on the side"
            case 1:
                return "Calm down for a bit"
            case 2:
                return "Fair and square"
    else:
        fillerChoice = world.random.randint(0, 3)
        match fillerChoice:
            case 0:
                return "Smaller chip"
            case 1:
                return "Bigger chip"
            case 2:
                return "Random chip color"
            case 3:
                return "Random table felt color"

def create_item_with_correct_classification(world: Atoll21World, name: str) -> Atoll21Item:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return Atoll21Item(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: Atoll21World) -> None:

    ITEM_COUNTS = {
        "Double": 1,
        "Split": 1,
        "Insurance": 1,
        "Surrender": 1,
        "Dealer level up": 3,
        "Bet limit": 1,
        "Bet limit boost": 2,
    }

    itempool: list[Item] = []
    for name, count in ITEM_COUNTS.items():
        itempool += [world.create_item(name) for _ in range(count)]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool