"""Kelly Criterion calculations and single-path bankroll simulation."""

import secrets

import numpy as np


def kelly_criterion(win_rate, win_payoff, lose_payoff):
    """Calculate the full-Kelly fraction for a binary outcome.

    The calculation uses the generalized Kelly formula::

        f* = (p * b - (1 - p) * a) / (a * b)

    where ``p`` is the win probability, ``b`` is the profit multiple on a
    win, and ``a`` is the loss multiple on a loss. A result below zero is
    returned as zero, indicating that the bet has no positive edge.

    Args:
        win_rate: Probability of winning, expressed as a value from 0 to 1.
        win_payoff: Profit per unit allocated when a bet wins. Must be
            greater than zero.
        lose_payoff: Loss per unit allocated when a bet loses. Must be
            greater than zero.

    Returns:
        The fraction of current capital prescribed by full Kelly, with a
        minimum value of zero.
    """
    return max(0,
               (win_rate * win_payoff - (1 - win_rate) * lose_payoff) / (win_payoff * abs(lose_payoff))
               )


def simulate_kelly(win_rate, win_payoff, lose_payoff, initial_capital, num_bets, kelly_fraction, seed=None):
    """Simulate a sequence of bets using fractional Kelly position sizing.

    Position size is recalculated from the current capital before every bet.
    Winning outcomes increase capital by the position size multiplied by
    ``win_payoff``; losing outcomes decrease it by the position size
    multiplied by ``lose_payoff``.

    Args:
        win_rate: Probability of winning each bet, expressed as a value from
            0 to 1.
        win_payoff: Profit multiple applied to the allocated capital after a
            win. Must be greater than zero.
        lose_payoff: Loss multiple applied to the allocated capital after a
            loss. Must be greater than zero.
        initial_capital: Capital available before the first bet.
        num_bets: Number of independent bets to simulate.
        kelly_fraction: Proportion of the full-Kelly allocation to use. For
            example, ``1.0`` is full Kelly and ``0.5`` is half Kelly.
        seed: Optional integer random seed. Supplying the same seed and
            inputs reproduces the same outcome sequence. When omitted, a
            random 64-bit seed is generated.

    Returns:
        A tuple containing:

        - capital history, including the initial capital;
        - longest winning streak;
        - longest losing streak;
        - Kelly-adjusted fraction allocated per bet; and
        - the random seed used for the simulation.
    """
    bet_fraction = kelly_criterion(win_rate, win_payoff, lose_payoff) * kelly_fraction
    capital = initial_capital
    capital_history = [capital]
    streak = {'win': 0, 'lose': 0}
    current_streak = {'win': 0, 'lose': 0}

    used_seed = secrets.randbits(64) if seed is None else seed
    rng = np.random.default_rng(used_seed)
    outcomes = (rng.random(num_bets) < win_rate)

    for outcome in outcomes:
        if outcome:
            capital += capital * bet_fraction * win_payoff
            current_streak['win'] += 1
            current_streak['lose'] = 0
        else:
            capital -= capital * bet_fraction * abs(lose_payoff)
            current_streak['lose'] += 1
            current_streak['win'] = 0

        capital_history.append(capital)
        streak['win'] = max(streak['win'], current_streak['win'])
        streak['lose'] = max(streak['lose'], current_streak['lose'])

    return (
        capital_history,
        streak['win'],
        streak['lose'],
        bet_fraction,
        used_seed
    )
