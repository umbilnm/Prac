
import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

ticker = str(input('Введите тикер:\n'))
per = int(input('Введите период(мес):\n'))
data = yf.Ticker(ticker).history(period = f'{per}mo')['Close']
if data.size == 0:
    print('Некорректный тикер')
else:
    data.plot()
    plt.ylabel('Price USD')
    plt.suptitle(f'График цены акций компании {ticker}AAPL')
    plt.show()

