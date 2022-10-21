import os
import glob
import pickle

owd = os.getcwd()
os.chdir("stock_dfs")
tickers =[]

for names in glob.glob("*.csv"):
    tickers.append(names.strip('.csv'))

os.chdir(owd)
with open("updatedTickers8_1_2020.pickle", "wb") as f:
    pickle.dump(tickers, f)

print(tickers)