## Monte Carlo Portfolio Risk Simulator - v1.0
## Author: Ethan Kelliher

## Overview
This is a Python project that simulates how stock portfolios perform using the Monte Carlo Method.
Uses Historical Data from Yahoo Finance, runs a large amount of random simulations and portfolios to estimate risk-adjusted returns.

## Features
- Pulls data from yFinance.
- Control the simulation fully through inputs.
- Simulates thousands of possible price paths for as many portfolios as wanted.
- Uses past returns to model future behavior
- Calculates risk based stats:
  - Average return
  - Median return
  - Standard deviation
  - Sharpe & Sortino Ratios
  - Value at Risk (VaR)
  - Conditional Value at Risk (CVaR)
  - Risk of loss %.
- Displays a chart of possible outcomes, best, worst, & median.

---

## Requirements
pip install -r requirements.txt
Makes use of numpy, pandas, matplotlib, & yfinance

## Running the program
py main.py