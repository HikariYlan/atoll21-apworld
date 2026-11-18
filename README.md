# /// Atoll 21 \\\\\\
## Made by Hikari / Ylan

Atoll 21 is a blackjack game for [Archipelago](https://archipelago.gg), set in a run-down casino on a tropical atoll. You show up with $100 and not much else. The goal is to climb to the boss buy-in, collect every ticket, and beat the casino's boss at his own table.

This repository is the **APWorld** (the part that plugs into Archipelago's generator). The game client is a separate project, and it is not released yet.

> **Status:** work in progress. The APWorld generates and is tested, but there is nothing to play yet. Version 1.0.0 will be the first full release of both the APWorld and the client.

## How it works

You start with only **Hit** and **Stand**, a weak dealer and a low bet limit. Everything else is shuffled into the multiworld:

- **Four abilities:** Double, Split, Insurance and Surrender.
- **Three Dealer level ups:** the dealer gets stronger each time you receive one.
- **Bet limit:** raises your maximum bet, and **Bet limit boost** (two of them) raises it further. The boost is optional.
- **Filler:** cosmetic chips and table colors, and a few traps if you ask for them.

To enter the boss's room you need **all 8 tickets** (the four abilities, the three Dealer level ups and the first Bet limit) **and** enough money. The money required is your starting bankroll times a multiplier you choose.

At the boss table you stake half of the buy-in and play a streak match: the first side to win two hands in a row takes it. The boss has a few visible advantages, and he may well pull something on you once. Beat him and you are done.

If you lose your last chip, a single purple chip with a skull appears. Win that hand and you are back to your starting bankroll. Lose it and you are thrown out.

## Checks

There are **52 checks** (46 with DeathLink off). They come from tickets, free events, streaks, bankroll milestones, hands won, the door and the boss, and, if DeathLink is on, from being killed by your friends.

## DeathLink

DeathLink is supported, and it is meant to be gentle. When someone else dies, you lose the hand you are playing, but not your money. Deaths are queued between rounds, one at a time, with a cooldown. If you go bust, you send a death.

The six checks that depend on other players dying are excluded locations, so they can only hold filler or traps. Nothing important is ever locked behind your friends' misfortune.

## Options

| Option | Default | Description |
|---|---|---|
| Starting bankroll | 100 | Your starting money (10 to 999). Bet limits and the boss buy-in are calculated from it. |
| Boss buy-in multiplier | 10 | The money needed for the boss's room is the starting bankroll times this (5 to 20). |
| Trap chance | 20 | Percentage of fillers that are traps instead of cosmetic chips. |
| Death Link | off | Send and receive deaths. |
| Death Link cooldown | 10 | Seconds to wait between two deaths. Only one is queued, the others are dropped. |

## Installing

1. Get `atoll21.apworld` (there is no public release yet).
2. Install it with the Archipelago launcher, or copy it into the `worlds` folder of your Archipelago data directory.
3. Restart the launcher. Atoll 21 now appears in the options creator.

## Running the tests

The tests need an Archipelago source checkout, since the packaged launcher does not ship the test tools.

1. Put this folder in the `worlds` directory of an Archipelago source checkout (matching version 0.6.8 or later), named `atoll21`.
2. From the root of that checkout, run `pytest worlds/atoll21/test`.

## AI disclosure

The game design and most of the code are mine. I used Claude as a helper for **bug fixing** (reviewing the code and catching mistakes) and for **writing the test suite**. It also wrote the item and location groups and a first draft of this README. The decisions about the game are mine.

## License

MIT, see [LICENSE](LICENSE).
