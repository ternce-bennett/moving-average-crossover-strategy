import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

def fetch_data(ticker: str, start: str, end: str):
    df = yf.download(ticker, start=start, end=end)
    return df

def apply_strategy(df, short_window=50, long_window=200):
    df['SMA_Short'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_Long'] = df['Close'].rolling(window=long_window).mean()
    df['Signal'] = 0
    df.loc[short_window:, 'Signal'] = (
        df['SMA_Short'][short_window:] > df['SMA_Long'][short_window:]
    ).astype(int)
    df['Position'] = df['Signal'].diff()
    return df

def backtest(df, initial_capital=10000, commission=0.001):
    df['Returns'] = df['Close'].pct_change()
    df['Strategy_Returns'] = df['Returns'] * df['Position'].shift(1)
    # Subtract commissions for every position change
    trade_costs = abs(df['Position'].diff()) * commission
    df['Portfolio_Value'] = initial_capital * (1 + df['Strategy_Returns'] - trade_costs).cumprod()
    return df

def calculate_metrics(df):
    total_return = df['Portfolio_Value'].iloc[-1] / df['Portfolio_Value'].iloc[0] - 1
    returns = df['Strategy_Returns'].dropna()
    sharpe_ratio = np.sqrt(252) * (returns.mean() / returns.std())
    max_drawdown = (df['Portfolio_Value'].cummax() - df['Portfolio_Value']).max()

    print(f"Total Return: {total_return * 100:.2f}%")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Max Drawdown: {max_drawdown:.2f}")

def plot_strategy(df):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Price')
    plt.plot(df['SMA_Short'], label='Short MA (50)', alpha=0.7)
    plt.plot(df['SMA_Long'], label='Long MA (200)', alpha=0.7)
    plt.scatter(df[df['Position'] == 1].index, df['Close'][df['Position'] == 1], label='Buy', marker='^', color='green')
    plt.scatter(df[df['Position'] == -1].index, df['Close'][df['Position'] == -1], label='Sell', marker='v', color='red')
    plt.legend()
    plt.title("Moving Average Crossover Strategy")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def compare_to_benchmark(df):
    df['BuyAndHold'] = 10000 * (1 + df['Returns']).cumprod()
    plt.figure(figsize=(14, 7))
    plt.plot(df['Portfolio_Value'], label='Strategy')
    plt.plot(df['BuyAndHold'], label='Buy & Hold', linestyle='--')
    plt.title("Strategy vs. Buy & Hold")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value (€)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = fetch_data("AAPL", "2019-01-01", "2023-01-01")
    df = apply_strategy(df)
    df = backtest(df)
    plot_strategy(df)
    calculate_metrics(df)
    compare_to_benchmark(df)
