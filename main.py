# Monte Carlo Portfolio Risk Simulator
# Author: Ethan Kelliher
import datetime as dt # Time

import monte_carlo
import plot

stockList = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA'] # Mag 7 Stocks

def main():

    portfolioNumbers = int(input("How many portfolios do you want to simulate? Default is 5,000. ") or 5000)
    initialCapital = float(input("How much initial capital do you want?  Default is 10,000. ") or 10000) # Initial capital in USD.
    simulationDays = int(input("How many days do you want to simulate? Default is 252 (1 financial year). ") or 252) # Number of days (252 simulationDays = 1 year)
    simulations = int(input("How many simulations do you want to run? Default is 10,000. ") or 10000) # Number of simulations ran.
    lookBack = int(input("How many years of data would you like to sample? Default is 5. ") or 5)
    maxWeight = float(input("What would you like the max weight for any asset to be? (0-1) Default is .25. ") or .25)

    end = dt.datetime.now()
    start = end - dt.timedelta(days=365*lookBack) # dt works with actual days, not market days.
    returns = monte_carlo.getData(stockList, start, end)
    spyReturns = monte_carlo.getData(["SPY"], start, end)
    spySharpe = monte_carlo.calculateSharpe(spyReturns, 1.0)
    
    if portfolioNumbers == 1:

        stockWeights = monte_carlo.sampleWeights(len(stockList), maxWeight)
        sharpe = monte_carlo.calculateSharpe(returns, stockWeights)
        paths = monte_carlo.runSimulation(stockWeights, returns, simulations, simulationDays, initialCapital)
        metrics = monte_carlo.calculateRisk(paths, initialCapital, stockWeights)

        print("\n--- Portfolio Risk Report ---")
        print("Metrics:")
        plot.displayMetrics(metrics)

        plot.plot(paths, simulationDays)

    else:
        print("\nSampling portfolios. This may take a while.")
        bestSharpe = -999

        for i in range(portfolioNumbers):

            stockWeights = monte_carlo.sampleWeights(len(stockList), maxWeight)

            sharpe = monte_carlo.calculateSharpe(returns, stockWeights)

            if  sharpe > bestSharpe:
                bestSharpe = sharpe
                bestWeights = stockWeights

        print("Running Monte Carlo Simulation...")
        paths = monte_carlo.runSimulation(
            bestWeights,
            returns,
            simulations,
            simulationDays,
            initialCapital
        )

        metrics = monte_carlo.calculateRisk(paths, initialCapital, stockWeights)
        metrics["Sharpe Ratio"] = bestSharpe

        print("\nBest Portfolio (By Sharpe Ratio)")
        for ticker, weight in zip(stockList, bestWeights):
            print(f"{ticker}: {weight:.2%}")

        print("\n--- Portfolio Risk Report ---")
        print("Metrics")
        plot.displayMetrics(metrics)

        print("\nBenchmark Comparison")
        print(f"SPY Sharpe:                      {spySharpe:.2f}")
        print(f"Portfolio Sharpe:                {bestSharpe:.2f}")
        print(f"Portfolio - SPY (Excess Sharpe): {bestSharpe - spySharpe:.2f}")

    plot.plot(paths, simulationDays)

main()