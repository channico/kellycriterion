# %% md
# Kelly Criterion Simulation with UI Sliders
# This simulation will allow you to visualize the change in capital using the Kelly Criterion.

# %%
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider


# Function to calculate the optimal bet fraction using Kelly Criterion
def kelly_criterion(win_rate, win_payoff, lose_payoff):
    return max(0,
               (win_rate * win_payoff - (1 - win_rate) * lose_payoff) / (win_payoff * abs(lose_payoff))
               )


# Function to simulate the outcomes of bets and track capital
def simulate_kelly(win_rate, win_payoff, lose_payoff, initial_capital, num_bets=100):
    bet_fraction = kelly_criterion(win_rate, win_payoff, lose_payoff)
    capital = initial_capital
    capital_history = [capital]

    streak = {'win': 0, 'lose': 0}
    current_streak = {'win': 0, 'lose': 0}

    outcomes = (np.random.rand(num_bets) < win_rate)

    for outcome in outcomes:
        if outcome:  # Win
            capital += capital * bet_fraction * win_payoff
            current_streak['win'] += 1
            current_streak['lose'] = 0
        else:  # Loss
            capital -= capital * bet_fraction * abs(lose_payoff)
            current_streak['lose'] += 1
            current_streak['win'] = 0

        capital_history.append(capital)
        streak['win'] = max(streak['win'], current_streak['win'])
        streak['lose'] = max(streak['lose'], current_streak['lose'])

    return capital_history, streak['win'], streak['lose']


# Interactive UI for the simulation
def kelly_simulation_ui(win_rate, win_payoff, lose_payoff, initial_capital):
    capital_history, max_win_streak, max_lose_streak = simulate_kelly(win_rate, win_payoff, lose_payoff,
                                                                      initial_capital)

    plt.figure(figsize=(12, 6))
    plt.plot(capital_history, label="Capital Over Time")
    plt.title("Kelly Criterion Simulation")
    plt.xlabel("Number of Rounds")
    plt.ylabel("Capital")
    plt.axhline(y=initial_capital, color='orange', linestyle='--', label="Initial Capital")
    plt.legend()
    plt.grid()
    plt.show()

    print(f"Longest Winning Streak: {max_win_streak}")
    print(f"Longest Losing Streak: {max_lose_streak}")


# Set up interactive sliders
interact(
    kelly_simulation_ui,
    win_rate=FloatSlider(min=0.1, max=0.9, step=0.05, value=0.5, description='Win Rate'),
    win_payoff=FloatSlider(min=0.1, max=10, step=0.1, value=2, description='Win Payoff'),
    lose_payoff=FloatSlider(min=0.1, max=10, step=0.1, value=1, description='Lose Payoff'),
    initial_capital=IntSlider(min=100, max=5000, step=100, value=1000, description='Initial Capital')
)