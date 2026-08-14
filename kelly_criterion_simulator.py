# %% md
# Kelly Criterion Simulation with UI Sliders
# This simulation will allow you to visualize the change in capital using the Kelly Criterion.

# %%
import numpy as np
import secrets

# Function to calculate the optimal bet fraction using Kelly Criterion
def kelly_criterion(win_rate, win_payoff, lose_payoff):
    return max(0,
               (win_rate * win_payoff - (1 - win_rate) * lose_payoff) / (win_payoff * abs(lose_payoff))
               )


def simulate_kelly(win_rate, win_payoff, lose_payoff, initial_capital, num_bets, kelly_fraction, seed=None):
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
