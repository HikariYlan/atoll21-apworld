from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules
from . import options as atoll21_options

class Atoll21World(World):
    """
    Atoll 21 takes place in a casino on an atoll, where your goal is to gamble the last few bucks you have in blackjack.
    Earn tickets and enough money to access the casino's boss' room, and defeat him in a final showdown.
    """

    game = "Atoll 21"

    options_dataclass = atoll21_options.Atoll21Options
    options: atoll21_options.Atoll21Options

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    location_name_groups = locations.LOCATION_NAME_GROUPS
    item_name_to_id = items.ITEM_NAME_TO_ID
    item_name_groups = items.ITEM_NAME_GROUPS

    origin_region_name = "Dealer's table"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.Atoll21Item:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> dict[str, Any]:
        return self.options.as_dict("death_link", "starting_bankroll", "boss_buy_in_multiplier", "death_link_cooldown")