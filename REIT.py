# Install yfinance if needed: pip install yfinance
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# List of real estate stocks and REITs
tickers = ['VNQ', 'O', 'SPG', 'AMT', 'PLD']

# Step 1: Download data from Yahoo Finance
data = yf.download(tickers, start="2023-01-01", end="2023-12-31")['Adj Close']

# Drop any rows with missing data
data = data.dropna()

# Step 2: Calculate daily returns and 30-day rolling volatility
returns = data.pct_change().dropna()
rolling_volatility = returns.rolling(window=30).std()

# Step 3: Exploratory Data Analysis

# Plot stock price trends
plt.figure(figsize=(12, 6))
for ticker in tickers:
    plt.plot(data[ticker], label=ticker)
plt.title("Real Estate Stocks and REITs Price Trends (2023)")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.legend()
plt.show()

# Plot the distribution of daily returns
plt.figure(figsize=(10, 5))
sns.histplot(returns, kde=True)
plt.title("Distribution of Daily Returns for Real Estate Stocks")
plt.xlabel("Daily Returns")
plt.show()

# Step 4: Portfolio Analysis
# Equal-weighted portfolio returns
portfolio_returns = returns.mean(axis=1)
cumulative_returns = (1 + portfolio_returns).cumprod() - 1

# Plot cumulative returns of the portfolio
plt.figure(figsize=(10, 5))
cumulative_returns.plot()
plt.title("Cumulative Returns of Equal-Weighted Real Estate Portfolio")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.show()

# Step 5: Heatmap of Correlations
# Correlation heatmap of returns
plt.figure(figsize=(8, 6))
sns.heatmap(returns.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Real Estate Stocks/REITs Returns")
plt.show()
