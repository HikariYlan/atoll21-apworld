from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

from dataclasses import dataclass

class TrapChance(Range):
    """
    Percentage chance that any given chip is replaced by a trap.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 20

class DeathLink(Toggle):
    """
    Enables Death link, and death link related checks. When losing the last-chance chip, a death link is send. 
    When someone sends a death link, your actual hand is thrown out. When 2+ hands with Split, the hand thrown out is random.
    """

    display_name = "Death link"

@dataclass
class Atoll21Options(PerGameCommonOptions):
    trap_chance: TrapChance
    death_link: DeathLink