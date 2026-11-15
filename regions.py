from __future__ import annotations

from BaseClasses import Entrance, Region

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import Atoll21World

def create_and_connect_regions(world: Atoll21World) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: Atoll21World) -> None:
    dealer_table = Region("Dealer's table", world.player, world.multiworld)
    boss_room = Region("Casino's Boss' room", world.player, world.multiworld)

    regions = [dealer_table, boss_room]

    world.multiworld.regions += regions

def connect_regions(world: Atoll21World) -> None:
    dealer_table = world.get_region("Dealer's table")
    boss_room = world.get_region("Casino's Boss' room")

    dealer_table.connect(boss_room, "Dealer's table to casino's Boss' room")