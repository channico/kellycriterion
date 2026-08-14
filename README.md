# Kelly Criterion Simulator

An interactive Python simulation for exploring **Kelly Criterion position sizing** and its effect on capital growth over a sequence of bets or trades.

The simulator lets you vary the assumed **win rate**, **payoff on winning trades**, **loss on losing trades**, and **initial capital**, then visualizes how your capital evolves when position sizes are determined using the Kelly Criterion.

## What is the Kelly Criterion?

The **Kelly Criterion** is a mathematical approach to position sizing that seeks to maximize the long-term geometric growth rate of capital.

In its simplest form, the Kelly fraction can be expressed as:

$$
f^* = \frac{bp-q}{b}
$$

where:

- $f^*$ = optimal fraction of capital to risk
- $p$ = probability of winning
- $q = 1-p$ = probability of losing
- $b$ = net payoff received for each unit risked

Rather than asking only:

> *"Is this trade profitable?"*

the Kelly Criterion asks:

> *"Given my probability of winning and my reward-to-risk characteristics, how much of my capital should I risk?"*

This simulator provides a visual way to explore that question.

## Features

- Interactive Jupyter Notebook controls
- Adjustable win probability
- Adjustable winning payoff
- Adjustable losing payoff
- Adjustable initial capital
- Kelly-based position sizing
- Monte Carlo simulation of winning and losing outcomes
- Capital growth visualization
- Tracking of the longest winning streak
- Tracking of the longest losing streak

## Example

Suppose a trading strategy has:

- **Win rate:** 60%
- **Winning payoff:** 1R
- **Losing payoff:** 1R
- **Starting capital:** $1,000

The simulator calculates a Kelly-based fraction and then generates a random sequence of wins and losses according to the specified win probability.

After each trade, the position size is recalculated as a fraction of the **current capital**.

As a result, the simulation demonstrates the compounding nature of Kelly position sizing:

```text
Capital
  ^
  |                         /\
  |                  /\    /  \
  |          /\     /  \__/    \
  |    _____/  \___/
  |___/
  +--------------------------------> Trades
```

Because the sequence of wins and losses is randomly generated, each simulation can produce a different capital path even when the underlying assumptions remain unchanged.

## Installation

Clone the repository:

```bash
git clone https://github.com/channico/kellycriterion.git
cd kellycriterion
```

Create a virtual environment if desired:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

or Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

The project requires:

- NumPy
- Matplotlib
- ipywidgets

## Running the Simulator

The easiest way to explore the simulator is through the included Jupyter Notebook:

```bash
jupyter notebook notebook.ipynb
```

Run the cells and use the interactive sliders to change the simulation parameters.

The simulator currently provides controls for:

| Parameter | Range | Default |
|---|---:|---:|
| Win Rate | 10% – 90% | 50% |
| Win Payoff | 0.1 – 10.0 | 2.0 |
| Lose Payoff | 0.1 – 10.0 | 1.0 |
| Initial Capital | 100 – 5,000 | 1,000 |

Each simulation runs **100 bets/trades**.

## How the Simulation Works

For each simulation:

1. The Kelly fraction is calculated from the selected parameters.
2. A sequence of random outcomes is generated using the selected win rate.
3. The amount at risk is determined from the current capital and Kelly fraction.
4. Capital increases according to the winning payoff when the simulated trade wins.
5. Capital decreases according to the losing payoff when the simulated trade loses.
6. The process is repeated for 100 trades.
7. The resulting capital curve is plotted.
8. The longest winning and losing streaks are reported.

Because the position size is based on current capital, gains and losses affect the size of subsequent positions.

## Why Simulate Kelly?

The Kelly Criterion is often presented simply as a formula. Simulation makes some of its consequences much easier to understand.

In particular, it demonstrates that:

- **Having an edge does not mean every sequence of trades will be profitable.**
- **Position sizing matters enormously to long-term outcomes.**
- **Compounding amplifies both good and bad sequences.**
- **Losing streaks can occur even with a profitable strategy.**
- **A high win rate alone does not determine profitability — payoff matters too.**

It also illustrates why traders often use **Fractional Kelly** rather than the full Kelly allocation in practice.

For example:

\[
f_{\text{Half Kelly}} = 0.5 f^*
\]

and:

\[
f_{\text{Quarter Kelly}} = 0.25 f^*
\]

Fractional Kelly sacrifices some theoretical growth in exchange for lower position sizes, lower volatility, and potentially smaller drawdowns.

## Project Structure

```text
kellycriterion/
│
├── kelly_criterion_simulator.py
├── notebook.ipynb
├── requirements.txt
└── .gitignore
```

### `kelly_criterion_simulator.py`

Contains the core Kelly calculation, simulation logic, visualization, and interactive controls.

### `notebook.ipynb`

Jupyter Notebook version for interactively experimenting with the simulator.

### `requirements.txt`

Python dependencies required to run the project.

## Possible Future Improvements

Some useful extensions to the simulator could include:

- Fractional Kelly (Half Kelly, Quarter Kelly, etc.)
- Fixed-percentage position sizing for comparison
- Fixed-dollar risk sizing
- Multiple Monte Carlo runs
- Distribution of terminal capital
- Maximum drawdown statistics
- Probability of ruin
- Expected geometric growth rate
- Comparison between Kelly and over-betting
- Comparison between Kelly and under-betting
- Variable win rates and payoff ratios
- Trading costs and commissions
- Configurable number of trades
- Export of simulation results

These additions would make it possible to explore not just optimal theoretical growth, but also the practical trade-off between **growth, volatility, and drawdown**.

## Disclaimer

This project is intended for **educational and experimental purposes only**.

The Kelly Criterion depends heavily on the accuracy of the estimated probability of winning and the expected payoff. Real-world trading outcomes are not necessarily independent, probabilities are rarely known with certainty, and transaction costs, slippage, liquidity, changing market conditions, and estimation errors can materially affect results.

The simulator should therefore not be interpreted as financial or investment advice.

## Author

**Nicodemus Chan**

GitHub: `@channico`

### License

This project is licensed under the **MIT License**.

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of this software, subject to the terms of the MIT License.

See the [`LICENSE`](LICENSE) file for details.

Copyright © 2026 Nicodemus Chan.