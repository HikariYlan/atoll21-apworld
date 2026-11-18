from .bases import Atoll21TestBase

DEATH_LINK_LOCATIONS = [
    "First blood",
    "Collateral damage",
    "Stop it. Get some help",
    "This is the part where I tell you to Alt + F4",
    "Dude. Please.",
    "15 mistakes. Only 1 person.",
]


class TestDeathLinkOff(Atoll21TestBase):
    options = {
        "death_link": False,
    }

    def test_death_link_locations_do_not_exist(self) -> None:
        for name in DEATH_LINK_LOCATIONS:
            with self.subTest(f"Test that {name} does not exist"):
                self.assertRaises(KeyError, self.world.get_location, name)

    def test_location_count(self) -> None:
        self.assertEqual(len(self.multiworld.get_unfilled_locations(self.player)), 46)


class TestDeathLinkOn(Atoll21TestBase):
    options = {
        "death_link": True,
    }

    def test_death_link_locations_exist_and_are_excluded(self) -> None:
        for name in DEATH_LINK_LOCATIONS:
            with self.subTest(f"Test that {name} exists and is excluded"):
                try:
                    location = self.world.get_location(name)
                except KeyError:
                    self.fail(f"{name} should exist, but it doesn't.")
                self.assertTrue(location.progress_type.name == "EXCLUDED")

    def test_death_link_locations_are_reachable_with_nothing(self) -> None:
        for name in DEATH_LINK_LOCATIONS:
            with self.subTest(f"Test that {name} is reachable with nothing"):
                self.assertTrue(self.world.get_location(name).can_reach(self.multiworld.state))

    def test_location_count(self) -> None:
        self.assertEqual(len(self.multiworld.get_unfilled_locations(self.player)), 52)
