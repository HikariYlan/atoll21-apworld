from __future__ import annotations

from BaseClasses import ItemClassification, Location, LocationProgressType

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import Atoll21World

from . import items

LOCATION_NAME_TO_ID = {
    # 1xx: Gated by a ticket (11)
    # Surrender
    "Coward": 101,
    "Regret": 102,
    # Insurance
    "Do you have 5 minutes?": 103,
    "Never back down, never what": 104,
    "Claim approved": 105,
    # Split
    "Prepare for trouble...": 106,
    "...and that's it.": 107,
    "...and make it double!": 108,
    # Double down
    "The greed mentioned in the Bible": 109,
    "Jackpot!": 110,
    "Pride goes before a fall": 111,

    # 2xx: Free events (11)
    "That's the name of the game!": 201,
    "Royal court": 202,
    "Déjà vu": 203,
    "Unlucky luck": 204,
    "Beginner's luck": 205,
    "Ha! You suck!": 206,
    "Well, that's awkward": 207,
    "I don't have a greeeen!!": 208,
    "I didn't sweat at all": 209,
    "Sir, you need to leave": 210,
    "It's rigged anyway": 211,
    "Wait, what?": 212,
    "Well, that's really awkward": 213,

    # 3xx: Streaks (4)
    "Happy feet": 301,
    "Wombo Combo": 302,
    "Get your a** whooped!": 303,
    "Skill issue": 304,

    # 4xx: Bankroll milestones (10)
    "Bankroll milestone 1": 401,
    "Bankroll milestone 2": 402,
    "Bankroll milestone 3": 403,
    "Bankroll milestone 4": 404,
    "Bankroll milestone 5": 405,
    "Bankroll milestone 6": 406,
    "Bankroll milestone 7": 407,
    "Bankroll milestone 8": 408,
    "Bankroll milestone 9": 409,
    "Bankroll milestone 10": 410,

    # 5xx: Hands won in total (4)
    "Hands won: 10": 501,
    "Hands won: 25": 502,
    "Hands won: 50": 503,
    "99% of gamblers lose because they stop playing": 504,

    # 6xx: Door and boss (4)
    "Tickets, please": 601,
    "You're broke, homie": 602,
    "The final showdown": 603,
    "Note to self: do NOT gamble your life": 604,

    # 7xx: DeathLink deaths (6, only generated with DeathLink on)
    "First blood": 701,
    "Collateral damage": 702,
    "Stop it. Get some help": 703,
    "This is the part where I tell you to Alt + F4": 704,
    "Dude. Please.": 705,
    "15 mistakes. Only 1 person.": 706,
}

DEALER_TABLE_LOCATIONS = [
    # Gated by a ticket
    "Coward",
    "Regret",
    "Do you have 5 minutes?",
    "Never back down, never what",
    "Claim approved",
    "Prepare for trouble...",
    "...and that's it.",
    "...and make it double!",
    "The greed mentioned in the Bible",
    "Jackpot!",
    "Pride goes before a fall",
    # Free events
    "That's the name of the game!",
    "Royal court",
    "Déjà vu",
    "Unlucky luck",
    "Beginner's luck",
    "Ha! You suck!",
    "Wait, what?",
    "Well, that's awkward",
    "Well, that's really awkward",
    "I don't have a greeeen!!",
    "I didn't sweat at all",
    "Sir, you need to leave",
    "It's rigged anyway",
    # Streaks
    "Happy feet",
    "Wombo Combo",
    "Get your a** whooped!",
    "Skill issue",
    # Bankroll milestones
    "Bankroll milestone 1",
    "Bankroll milestone 2",
    "Bankroll milestone 3",
    "Bankroll milestone 4",
    "Bankroll milestone 5",
    "Bankroll milestone 6",
    "Bankroll milestone 7",
    "Bankroll milestone 8",
    "Bankroll milestone 9",
    "Bankroll milestone 10",
    # Hands won in total
    "Hands won: 10",
    "Hands won: 25",
    "Hands won: 50",
    "99% of gamblers lose because they stop playing",
    # Door (turned away)
    "Tickets, please",
    "You're broke, homie",
]

BOSS_ROOM_LOCATIONS = [
    "The final showdown",
    "Note to self: do NOT gamble your life",
]

# Only when death link is on
DEATH_LINK_LOCATIONS = [
    "First blood",
    "Collateral damage",
    "Stop it. Get some help",
    "This is the part where I tell you to Alt + F4",
    "Dude. Please.",
    "15 mistakes. Only 1 person."
]


class Atoll21Location(Location):
    game = "Atoll 21"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: Atoll21World) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: Atoll21World) -> None:
    dealer_table = world.get_region("Dealer's table")
    boss_room = world.get_region("Casino's Boss' room")

    dealer_table_locations = get_location_names_with_ids(DEALER_TABLE_LOCATIONS)
    dealer_table.add_locations(dealer_table_locations, Atoll21Location)

    boss_room_locations = get_location_names_with_ids(BOSS_ROOM_LOCATIONS)
    boss_room.add_locations(boss_room_locations, Atoll21Location)

    if world.options.death_link:
        death_link_locations = get_location_names_with_ids(DEATH_LINK_LOCATIONS)
        dealer_table.add_locations(death_link_locations, Atoll21Location)
        
        for name in DEATH_LINK_LOCATIONS:
            world.get_location(name).progress_type = LocationProgressType.EXCLUDED

def create_events(world: Atoll21World) -> None:
    boss_room = world.get_region("Casino's Boss' room")

    bluff_called = Atoll21Location(world.player, "Called the bluff", None, boss_room)
    boss_room.locations.append(bluff_called)

    victory_item = items.Atoll21Item("Called the bluff", ItemClassification.progression, None, world.player)
    bluff_called.place_locked_item(victory_item)
