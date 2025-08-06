# Moving Average Crossover Trading Strategy

A simple Python program that implements a **moving average crossover trading strategy** using historical stock data. This project is designed for beginners to learn about algorithmic trading, data analysis, and Python programming.

---

## 🚀 Project Overview

The strategy uses two moving averages—**50-day** and **200-day**—to generate buy and sell signals:

- **Buy signal:** When the 50-day moving average crosses above the 200-day moving average (golden cross).
- **Sell signal:** When the 50-day moving average crosses below the 200-day moving average (death cross).

The program backtests this strategy on historical stock price data, calculates performance metrics, and compares the results to a simple buy-and-hold approach.

---

## 📌 Features

- Download historical stock data from Yahoo Finance using the `yfinance` package  
- Apply the moving average crossover strategy  
- Calculate key performance metrics including:  
  - Total return  
  - Sharpe ratio  
  - Maximum drawdown  
- Visualize buy/sell signals on price charts  
- Plot portfolio value over time to compare strategy performance against buy-and-hold  

---

## 🧰 Tech Stack

- Python  
- yfinance  
- Matplotlib  
- Pandas  

---

## 💻 Installation

Make sure Python 3.8+ is installed, then install the required packages:

```bash

pip install yfinance matplotlib pandas
pip install yfinance matplotlib pandas

