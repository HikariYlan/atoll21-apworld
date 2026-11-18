from .bases import Atoll21TestBase


class TestLocationGroups(Atoll21TestBase):
    options = {
        "death_link": True,
    }

    run_default_tests = False

    def test_groups_only_contain_real_locations(self) -> None:
        for group, names in self.world.location_name_groups.items():
            for name in names:
                with self.subTest(f"Test that {name} in {group} is a real location"):
                    self.assertIn(name, self.world.location_name_to_id)

    def test_every_location_is_in_exactly_one_group(self) -> None:
        for name in self.world.location_name_to_id:
            with self.subTest(f"Test that {name} is in exactly one group"):
                groups = [group for group, names in self.world.location_name_groups.items() if group != "Everywhere" and name in names]
                self.assertEqual(len(groups), 1)
