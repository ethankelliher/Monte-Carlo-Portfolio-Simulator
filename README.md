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
- Displays a chart of possible outcomes, top 95%, bottom 5%, & median (50%).
- Benchmarks against the S&P 500
- Outputs the best portfolio based on risk-adjusted return.

## Requirements
pip install -r requirements.txt
Dependencies:
numpy
pandas
matplotlib
yfinance

## Running the program
py main.py
