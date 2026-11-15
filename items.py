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
    "Small chip": 108,
    #"Big chip": 109,
    "A nice drink on the side": 110,
    #"Calm down for a bit": 111,
    #"Fair and square": 112
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Double": ItemClassification.progression,
    "Split": ItemClassification.progression,
    "Insurance": ItemClassification.progression,
    "Surrender": ItemClassification.progression,
    "Dealer level up": ItemClassification.progression,
    "Bet limit": ItemClassification.progression,
    "Bet limit boost": ItemClassification.useful,
    "Small chip": ItemClassification.filler,
    # "Big chip": ItemClassification.filler, for now I will do with only one filler
    "A nice drink on the side": ItemClassification.trap,
    # "Calm down for a bit": ItemClassification.trap, for now I will do with only one trap
    # "Fair and square": ItemClassification.trap
}

class Atoll21Item(Item):
    game = "Atoll 21"

def get_random_filler_item_name(world: Atoll21World) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        return "A nice drink on the side"
    return "Small chip"

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