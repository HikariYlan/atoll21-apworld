from .bases import Atoll21TestBase


class TestSlotData(Atoll21TestBase):
    options = {
        "death_link": True,
        "starting_bankroll": 250,
        "boss_buy_in_multiplier": 12,
        "death_link_cooldown": 7,
    }

    run_default_tests = False

    def test_slot_data_contains_every_option_the_client_needs(self) -> None:
        slot_data = self.world.fill_slot_data()

        for key, value in [
            ("death_link", 1),
            ("starting_bankroll", 250),
            ("boss_buy_in_multiplier", 12),
            ("death_link_cooldown", 7),
        ]:
            with self.subTest(f"Test that {key} is in the slot data"):
                self.assertEqual(slot_data[key], value)
