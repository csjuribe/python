import pandas as pd
import math

import pathlib
#input_dir = pathlib.Path('stock_dfs/')
#csv_path = inpputdir/"tsla.csv"


df = pd.read_csv('E:\Python_Projects\PycharmProjects\PythonFinanceOptions\stock_dfs\googl.csv', parse_dates=True, index_col=0)

df['HL_PCT'] = (df['High'] - df['Adj Close'])/df['Adj Close'] * 100.0
df['PCT_change'] = (df['Adj Close'] - df['Open'])/df['Open'] * 100.0

forecast_col = 'Adj Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.00001*len(df)))

df['Forecast'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.tail())
print(df.head())


