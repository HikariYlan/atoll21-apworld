from .bases import Atoll21TestBase


class TestAbilityLogic(Atoll21TestBase):
    options = {
        "death_link": False,
    }

    def test_free_locations_are_reachable_with_nothing(self) -> None:
        for name in ["Royal court", "Beginner's luck", "Happy feet", "Bankroll milestone 1", "Hands won: 10", "Tickets, please"]:
            with self.subTest(f"Test that {name} is reachable with nothing"):
                self.assertTrue(self.world.get_location(name).can_reach(self.multiworld.state))

    def test_surrender_locations(self) -> None:
        self.assertAccessDependency(["Coward", "Regret"], [["Surrender"]], only_check_listed=True)

    def test_insurance_locations(self) -> None:
        self.assertAccessDependency(
            ["Do you have 5 minutes?", "Never back down, never what", "Claim approved"],
            [["Insurance"]],
            only_check_listed=True,
        )

    def test_split_locations(self) -> None:
        self.assertAccessDependency(
            ["Prepare for trouble...", "...and that's it.", "...and make it double!"],
            [["Split"]],
            only_check_listed=True,
        )

    def test_double_locations(self) -> None:
        self.assertAccessDependency(
            ["The greed mentioned in the Bible", "Jackpot!", "Pride goes before a fall"],
            [["Double"]],
            only_check_listed=True,
        )
