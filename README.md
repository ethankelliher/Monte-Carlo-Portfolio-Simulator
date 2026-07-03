## Monte Carlo Portfolio Risk Simulator - v1.0
## Author: Ethan Kelliher

## Overview
This is a Python project that simulates how stock portfolios perform using the Monte Carlo Method.
Uses Historical Data from Yahoo Finance, runs a large amount of random simulations and portfolios to estimate risk-adjusted returns.

## Features
- Pulls data from yFinance.
- Control the simulation fully through inputs.
- Generates portfolio weights using random sampling with a max weight constraint. 
  - The "optimized" portfolio is chosen by the highest sharpe ratio.
- Runs a Monte Carlo simulation for possible price paths for the optimized portfolio.
- Approximates forward return distributions using bootstrapping.
- Calculates risk based stats:
  - Mean & Median return
  - Standard deviation (volatility)
  - Sharpe (annualized) & Sortino Ratios
  - Value at Risk (VaR 95%)
  - Conditional Value at Risk (CVaR)
  - Average & Worst drawdown.
- 
- Displays a chart of possible outcomes, top 95%, bottom 5%, & median (50%).
- Benchmarks against the S&P 500
- Outputs the best portfolio based on risk-adjusted return.

## Example Output
Best Portfolio (By Sharpe Ratio)
AAPL: 22.91%
MSFT: 5.29%
GOOG: 23.65%
AMZN: 3.62%
NVDA: 14.17%
META: 24.63%
TSLA: 5.74%

--- Portfolio Risk Report ---
Metrics
Mean Return:                     29.74%
Median Return:                   24.72%
Standard Deviation:              38.61%
Sharpe Ratio:                    1.01
Sortino Ratio:                   2.74
Value at Risk (95%):             -22.90%
Conditional VaR (95%):           -31.17%
Average Drawdown:                -22.75%
Worst Drawdown:                  -38.40%

Benchmark Comparison
SPY Sharpe:                      0.80
Portfolio Sharpe:                1.01
Portfolio - SPY (Excess Sharpe): 0.21

## Requirements
pip install -r requirements.txt
Dependencies:
numpy
pandas
matplotlib
yfinance

## Running the program
py main.py