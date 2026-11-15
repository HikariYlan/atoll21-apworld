from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule


def set_all_rules(world: Atoll21World) -> None:
    set_all_entrances_rules(world)
    set_all_locations_rules(world)
    set_completion_condition(world)

def set_all_entrances_rules(world: Atoll21World) -> None:
    dealer_table_to_boss_room = world.get_entrance("Dealer's table to casino's Boss' room")

    has_all_dealer_level_up = Has("Dealer level up", count=3)
    has_all_abilities = HasAll("Double", "Split", "Insurance", "Surrender")
    has_bet_limit = Has("Bet limit")
    can_enter_boss_room = has_all_dealer_level_up & has_all_abilities & has_bet_limit

    world.set_rule(dealer_table_to_boss_room, can_enter_boss_room)

def set_all_locations_rules(world: Atoll21World) -> None:
    can_surrender = Has("Surrender")
    can_bet_insurance = Has("Insurance")
    can_split = Has("Split")
    can_double = Has("Double")

    coward = world.get_location("Coward")
    regret = world.get_location("Regret")
    world.set_rule(coward, can_surrender)
    world.set_rule(regret, can_surrender)

    do_you_have_5_minutes = world.get_location("Do you have 5 minutes?")
    never_back_down_never_what = world.get_location("Never back down, never what")
    claim_approved = world.get_location("Claim approved")
    world.set_rule(do_you_have_5_minutes, can_bet_insurance)
    world.set_rule(never_back_down_never_what, can_bet_insurance)
    world.set_rule(claim_approved, can_bet_insurance)

    prepare_for_trouble = world.get_location("Prepare for trouble...")
    and_thats_it = world.get_location("...and that's it.")
    and_make_it_double = world.get_location("...and make it double!")
    world.set_rule(prepare_for_trouble, can_split)
    world.set_rule(and_thats_it, can_split)
    world.set_rule(and_make_it_double, can_split)

    the_greed_mentioned_in_the_bible = world.get_location("The greed mentioned in the Bible")
    jackpot = world.get_location("Jackpot!")
    pride_goes_before_a_fall = world.get_location("Pride goes before a fall")
    world.set_rule(the_greed_mentioned_in_the_bible, can_double)
    world.set_rule(jackpot, can_double)
    world.set_rule(pride_goes_before_a_fall, can_double)

def set_completion_condition(world: Atoll21World) -> None:
    world.set_completion_rule(Has("Called the bluff"))