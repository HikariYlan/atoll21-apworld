from .bases import Atoll21TestBase

BOSS_ROOM = "Casino's Boss' room"

TICKETS = ["Double", "Split", "Insurance", "Surrender", "Dealer level up", "Bet limit"]

BOSS_LOCATIONS = [
    "You're broke, homie",
    "The final showdown",
    "Note to self: do NOT gamble your life",
    "Called the bluff",
]


class TestBossRoomLogic(Atoll21TestBase):
    options = {
        "death_link": False,
    }

    def test_boss_room_requires_every_ticket(self) -> None:
        for ticket in TICKETS:
            with self.subTest(f"Test that the boss room requires {ticket}"):
                self.assertAccessDependency(BOSS_LOCATIONS, [[ticket]], only_check_listed=True)

    def test_boss_room_requires_all_three_dealer_level_ups(self) -> None:
        dealer_level_ups = self.get_items_by_name("Dealer level up")
        self.assertEqual(len(dealer_level_ups), 3)

        self.collect_all_but("Dealer level up")
        boss_room_entrance = self.world.get_entrance("Dealer's table to casino's Boss' room")

        for count in range(3):
            with self.subTest(f"Test that {count} Dealer level up is not enough"):
                self.assertFalse(boss_room_entrance.can_reach(self.multiworld.state))
                self.collect(dealer_level_ups[count])

        with self.subTest("Test that 3 Dealer level up is enough"):
            self.assertTrue(boss_room_entrance.can_reach(self.multiworld.state))

    def test_boss_room_does_not_require_bet_limit_boost(self) -> None:
        self.collect_all_but("Bet limit boost")

        for location in BOSS_LOCATIONS:
            with self.subTest(f"Test that {location} is reachable without Bet limit boost"):
                self.assertTrue(self.world.get_location(location).can_reach(self.multiworld.state))

    def test_boss_room_is_not_reachable_with_nothing(self) -> None:
        for location in BOSS_LOCATIONS:
            with self.subTest(f"Test that {location} is not reachable with nothing"):
                self.assertFalse(self.world.get_location(location).can_reach(self.multiworld.state))
