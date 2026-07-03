# Monte Carlo Method

import pandas as pd # Data Manipulation library
import numpy as np # Number computing (arrays)
import yfinance as finance # Historical Market Data using Yahoo Finance.

# Returns rawData financial data.
def getData(stocks, start, end):
    # rawData OHLCV data for all stocks between start and end dates.
    rawData = finance.download(stocks, start=start, end=end, progress=False)

    # Checks if there are multiple tickers.
    if isinstance(rawData.columns, pd.MultiIndex):
        # Preferred adjusted close data (adjusts for dividends, stock splits, etc.)
        if 'Adj Close' in rawData.columns.get_level_values(0):
            prices = rawData['Adj Close']
            #print('Using Adjusted Close Data.')
        else:
            prices = rawData['Close']
            #print('Using Regular Close Data.')
    else:
        prices = rawData

    if prices.empty or prices.isna().all().all():
        raise RuntimeError("No price data scraped.")
    
    return prices.pct_change().dropna().values


def sampleWeights(nAssets, maxWeight):
    while True: 
        weights = np.random.random(nAssets)
        weights = weights / np.sum(weights)

        if np.all(weights <= maxWeight): 
            return weights


# Monte Carlo Method
def runSimulation(stockWeights, returns, sims, simulationDays, initialCapital):
    # Log returns for stability
    logReturns = np.log1p(returns)

    # X axis is time, y axis is paths.
    results = np.zeros((simulationDays, sims))

    for i in range(sims):
        randomDays = np.random.choice(len(logReturns), simulationDays)
        simReturns = logReturns[randomDays]

        portfolioLog = np.dot(simReturns, stockWeights)
        # Cumulative sum of portfolio, then convert it back to a %.
        results[:, i] = initialCapital * np.exp(np.cumsum(portfolioLog))

    return results

def calculateSharpe(returns, stockWeights):

    portfolioReturns = np.dot(returns, stockWeights)

    meanDailyReturn = np.mean(portfolioReturns)
    dailyVolatility = np.std(portfolioReturns)

    sharpe = (meanDailyReturn / dailyVolatility) * np.sqrt(252)

    return sharpe

def calculateSortino(finalValues, initialCapital):

    returns = finalValues / initialCapital - 1

    mean = np.mean(returns)

    # Only negative returns
    downside = returns[returns < 0]

    # If no downside risk exists
    if len(downside) == 0:
        return float("inf")

    downsideDeviation = np.std(downside)

    sortino = mean / (downsideDeviation + 1e-8)

    return sortino

def calculateRisk(paths, initialCapital, stockWeights):
    finalValues = paths[-1]

    # Convert to total return.
    returns = (finalValues / initialCapital) - 1

    # Numbers with stat value.
    mean = np.mean(returns)
    median = np.median(returns)
    std = np.std(returns)

    sortino = calculateSortino(finalValues, initialCapital)

    # 95% value at risk
    var95 = np.percentile(returns, 5)
    cvar95 = np.mean(returns[returns <= var95])

    drawdowns = []

    for path in paths.T:
        # Find the highest value over time
        peak = np.maximum.accumulate(path)

        # Drawdown = (current - peak) / peak
        drawdowns.append(np.min((path-peak) / peak))

    drawdowns = np.array(drawdowns)

    return {
        "Mean Return": mean,
        "Median Return": median,
        "Standard Deviation of Return": std,
        "Sharpe Ratio": -999,
        "Sortino Ratio": sortino,
        "Value at Risk 95%": var95,
        "Conditional Value at Risk 95%": cvar95,
        "Average Drawdown": np.mean(drawdowns),
        "Worst Drawdown": np.percentile(drawdowns, 5),
    }