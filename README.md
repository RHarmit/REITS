# REITS

**Project Overview**
This project provides an in-depth analysis of the real estate market by focusing on major real estate stocks and REITs. Using Python and the yfinance API, this tool gathers, processes, and visualizes data to offer insights into sector trends, stock correlations, and portfolio performance.

**Key Features**
Data Collection: Fetches historical stock prices for real estate stocks and REITs (e.g., VNQ, O, SPG, AMT, PLD) using yfinance.
Exploratory Data Analysis (EDA): Analyzes price trends, return distributions, and calculates correlations between stocks, revealing high interdependence (e.g., 0.89 correlation between PLD and VNQ).
Portfolio Analysis: Constructs an equal-weighted portfolio of selected real estate stocks, achieving a 15% peak in cumulative returns with a Sharpe ratio of 1.3, highlighting favorable risk-adjusted performance.

**Project Structure**
data_collection.py: Script for downloading and cleaning data using yfinance.
analysis.py: Contains functions for calculating returns, volatility, and generating visualizations.
portfolio_analysis.py: Builds and evaluates the equal-weighted portfolio, calculating cumulative returns and Sharpe ratio.

**Visualizations**
Correlation Heatmap: Shows relationships between real estate stocks, with strong correlations indicating sector trends.
Price Trends: Line charts displaying historical stock price movements over the year.
Return Distribution: Histogram of daily returns for volatility and stability assessment.

**Results**
Identified high correlations within the sector, indicating a tightly linked market.
Portfolio demonstrated resilience with significant cumulative returns, even during periods of market volatility.
Requirements
Python packages: yfinance, pandas, matplotlib, seaborn
Installation: Run pip install -r requirements.txt to install dependencies.
