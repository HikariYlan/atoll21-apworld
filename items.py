from BaseClasses import Item, ItemClassification

ITEM_NAME_TO_ID = {
    "Double": 101,
    "Split": 102,
    "Insurance": 103,
    "Surrender": 104,
    "Dealer level up": 105,
    "Bet limit": 106,
    "Bet limit boost": 107,
    "Small chip": 108,
    "Big chip": 109,
    "A nice drink on the side": 110,
    "Calm down for a bit": 111,
    "Fair and square": 112
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
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = [
        world.create_item("Double"),
        world.create_item("Split"),
        world.create_item("Insurance"),
        world.create_item("Surrender"),
        world.create_item("Dealer level up"),
        world.create_item("Bet limit"),
        world.create_item("Bet limit boost"),
        world.create_item("Small chip"),
        world.create_item("Big chip"),
        world.create_item("A nice drink on the side"),
        world.create_item("Calm down for a bit"),
        world.create_item("Fair and square")
    ]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool