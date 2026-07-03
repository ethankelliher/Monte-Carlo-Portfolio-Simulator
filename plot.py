# Data plot for the simulation

import matplotlib.pyplot as plt # Plotting library
import numpy as np # Number computing (arrays)

# Visualization
def plot(paths, simulationDays):
    # Bottom 5%
    p5 = np.percentile(paths, 5, axis = 1)

    # Median
    p50 = np.percentile(paths, 50, axis = 1)

    # 95th %
    p95 = np.percentile(paths, 95, axis = 1)

    plt.fill_between(range(simulationDays), p5, p95, alpha=0.3)
    plt.plot(p50)
    plt.title("Monte Carlo Portfolio Simulation (Optimized Portfolio)")
    plt.show()


def displayMetrics(metrics):
    print(f"Mean Return:                     {metrics['Mean Return']:.2%}")
    print(f"Median Return:                   {metrics['Median Return']:.2%}")
    print(f"Standard Deviation:              {metrics['Standard Deviation of Return']:.2%}")

    print(f"Sharpe Ratio:                    {metrics['Sharpe Ratio']:.2f}")
    print(f"Sortino Ratio:                   {metrics['Sortino Ratio']:.2f}")

    print(f"Value at Risk (95%):             {metrics['Value at Risk 95%']:.2%}")
    print(f"Conditional VaR (95%):           {metrics['Conditional Value at Risk 95%']:.2%}")

    print(f"Average Drawdown:                {metrics['Average Drawdown']:.2%}")
    print(f"Worst Drawdown:                  {metrics['Worst Drawdown']:.2%}")