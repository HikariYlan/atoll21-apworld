from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink

from dataclasses import dataclass

class TrapChance(Range):
    """
    Percentage chance that any given chip is replaced by a trap.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 20

@dataclass
class Atoll21Options(PerGameCommonOptions):
    trap_chance: TrapChance
    death_link: DeathLink