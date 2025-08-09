# 📈 Moving Average Crossover Strategy

A Python program implementing a moving average crossover trading strategy for stock market analysis.  
This project calculates short-term and long-term moving averages to identify buy and sell signals, helping investors make data-driven trading decisions.

---

## 📖 Overview
The moving average crossover strategy is a popular technical analysis tool used to detect trend changes.  
This project computes two moving averages (short and long windows) on historical stock price data and signals potential trades based on their crossover points.

---

## 📌 Features

| Feature                      | Description                                               |
|------------------------------|-----------------------------------------------------------|
| 📊 Short & Long Moving Averages | Calculates customizable short-term and long-term averages. |
| 🔄 Crossover Signal Detection | Generates buy/sell signals based on moving average crossovers. |
| 📅 Date Range Selection       | Analyze historical stock data over user-defined periods. |
| 📈 Visualizations             | Plots stock prices with moving averages and signal markers. |
| 🛠 Easy Configuration         | Adjustable parameters for moving average window sizes.   |

---

## 🛠 Tech Stack
- **Language:** Python 3.10  
- **Libraries:** Pandas, NumPy, Matplotlib  
- **Tools:** Jupyter Notebook / VS Code

---

## ⚙️ Setup & Installation
```bash
# 1. Clone the repository
git clone https://github.com/ternce-bennett/moving-average-crossover-strategy.git
cd moving-average-crossover-strategy

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the strategy script or notebook
python strategy.py
# or
jupyter notebook strategy.ipynb
