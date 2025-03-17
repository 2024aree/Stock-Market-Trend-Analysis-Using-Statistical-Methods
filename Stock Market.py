import yfinance as yf
import pandas as pd


stock_symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-01-01'


stock_data = yf.download(stock_symbol, start=start_date, end=end_date)


print(stock_data.head())



print(stock_data.isnull().sum())


stock_data.fillna(method='ffill', inplace=True)


stock_data.index = pd.to_datetime(stock_data.index)


print(stock_data.head())


stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
stock_data['200_MA'] = stock_data['Close'].rolling(window=200).mean()


print(stock_data[['Close', '50_MA', '200_MA']].tail())


stock_data['Daily_Return'] = stock_data['Close'].pct_change()


print(stock_data[['Close', 'Daily_Return']].tail())


stock_data['Cumulative_Return'] = (1 + stock_data['Daily_Return']).cumprod()


print(stock_data[['Close', 'Cumulative_Return']].tail())

import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")


plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Close Price', color='blue')
plt.plot(stock_data['50_MA'], label='50-Day MA', color='orange')
plt.plot(stock_data['200_MA'], label='200-Day MA', color='green')
plt.title(f'{stock_symbol} Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()


plt.figure(figsize=(14, 7))
plt.plot(stock_data['Daily_Return'], label='Daily Return', color='purple')
plt.title(f'{stock_symbol} Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.show()


plt.figure(figsize=(14, 7))
plt.plot(stock_data['Cumulative_Return'], label='Cumulative Return', color='red')
plt.title(f'{stock_symbol} Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.show()


plt.figure(figsize=(14, 7))
sns.histplot(stock_data['Daily_Return'].dropna(), bins=50, color='blue', kde=True)
plt.title(f'{stock_symbol} Daily Returns Histogram')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(14, 7))
sns.boxplot(x=stock_data['Daily_Return'].dropna(), color='green')
plt.title(f'{stock_symbol} Daily Returns Box Plot')
plt.xlabel('Daily Return')
plt.show()