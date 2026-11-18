from .bases import Atoll21TestBase

ITEM_COUNTS = {
    "Double": 1,
    "Split": 1,
    "Insurance": 1,
    "Surrender": 1,
    "Dealer level up": 3,
    "Bet limit": 1,
    "Bet limit boost": 2,
}

CHIPS = ["Smaller chip", "Bigger chip", "Random chip color", "Random table felt color"]
TRAPS = ["A nice drink on the side", "Calm down for a bit", "Fair and square"]


class TestItemPool(Atoll21TestBase):
    options = {
        "death_link": False,
    }

    def test_item_counts(self) -> None:
        for name, count in ITEM_COUNTS.items():
            with self.subTest(f"Test that there are {count} {name} in the pool"):
                self.assertEqual(len(self.get_items_by_name(name)), count)

    def test_progression_items(self) -> None:
        for name in ["Double", "Split", "Insurance", "Surrender", "Dealer level up", "Bet limit"]:
            with self.subTest(f"Test that {name} is progression"):
                self.assertTrue(all(item.advancement for item in self.get_items_by_name(name)))

    def test_bet_limit_boost_is_useful_but_not_progression(self) -> None:
        boosts = self.get_items_by_name("Bet limit boost")

        with self.subTest("Test that the Bet limit boost items are useful"):
            self.assertTrue(all(boost.useful for boost in boosts))

        with self.subTest("Test that the Bet limit boost items are not progression"):
            self.assertFalse(any(boost.advancement for boost in boosts))

    def test_item_groups_contain_real_items(self) -> None:
        for group, names in self.world.item_name_groups.items():
            for name in names:
                with self.subTest(f"Test that {name} in {group} is a real item"):
                    self.assertIn(name, self.world.item_name_to_id)


class TestNoTraps(Atoll21TestBase):
    options = {
        "death_link": False,
        "trap_chance": 0,
    }

    run_default_tests = False

    def test_no_traps_in_pool(self) -> None:
        for name in TRAPS:
            with self.subTest(f"Test that {name} is not in the pool"):
                self.assertEqual(len(self.get_items_by_name(name)), 0)


class TestOnlyTraps(Atoll21TestBase):
    options = {
        "death_link": False,
        "trap_chance": 100,
    }

    run_default_tests = False

    def test_no_chips_in_pool(self) -> None:
        for name in CHIPS:
            with self.subTest(f"Test that {name} is not in the pool"):
                self.assertEqual(len(self.get_items_by_name(name)), 0)
