from Options import PerGameCommonOptions, Range, DeathLink

from dataclasses import dataclass

class TrapChance(Range):
    """
    Percentage chance that a filler item is a trap instead of a cosmetic chip.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 20

class StartingBankroll(Range):
    """
    The amount of money you start with, and the amount you return to after winning the last-chance chip.
    The bet limits (minimum 10%, maximum 50% of this amount at the start), the boss buy-in (the bankroll required to reach the boss' room) and the boss' stake are all calculated from this number.
    """

    display_name = "Starting bankroll"

    range_start = 10
    range_end = 999
    default = 100

class BossBuyInMultiplier(Range):
    """
    The boss buy-in, the bankroll required to reach the boss' room, is your starting bankroll multiplied by this number.
    For example, a $100 starting bankroll with a multiplier of 10 means you need $1000.
    The boss' stake is half of that amount ($500 in this example).
    """

    display_name = "Boss buy-in multiplier"

    range_start = 5
    range_end = 20
    default = 10

class DeathLinkCooldown(Range):
    """
    How much time to wait between two death links. Note that only 1 death link is queued, others are dropped. Dropped one don't count for death link checks.
    """

    display_name = "Death Link cooldown"
    range_start = 1
    range_end = 20
    default = 10

@dataclass
class Atoll21Options(PerGameCommonOptions):
    trap_chance: TrapChance
    death_link: DeathLink
    starting_bankroll: StartingBankroll
    boss_buy_in_multiplier: BossBuyInMultiplier
    death_link_cooldown: DeathLinkCooldown