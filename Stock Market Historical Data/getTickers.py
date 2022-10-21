import bs4 as bs
import pandas as pd
import pickle
import requests
from tqdm import tqdm

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table',{'class':'wikitable sortable'})
    tickers = []

    for row in table.findAll('tr')[1:]:
        #time.sleep(1)
        #ticker = row.find("td").text.strip()
        ticker = row.findAll('td')[0].text.replace('.','-').strip()
        tickers.append(ticker)

    resp = requests.get('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table',{'class':'wikitable sortable'})

    for row in table.findAll('tr')[1:]:
        #time.sleep(1)
        #ticker = row.find("td").text.strip()
        ticker = row.findAll('td')[2].text.replace('.','-').strip('NYSE:\xa0').strip()
        tickers.append(ticker)

    resp = requests.get('https://en.wikipedia.org/wiki/NASDAQ-100')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table',{'id':'constituents'})

    for row in table.findAll('tr')[1:]:
        #ticker = row.find("td").text.strip()
        ticker = row.findAll('td')[1].text.replace('.','-').strip('NYSE:\xa0').strip()
        tickers.append(ticker)

    dfamex = pd.read_excel('AMEX.xlsx')
    dfnasdaq = pd.read_csv('NASDAQ.csv')
    dfnyse = pd.read_excel('NYSE.xlsx')

    symbols = dfnasdaq.iloc[:,0]
    for symb in symbols:
        #time.sleep(1)
        temp = symb.replace('^','-')
        temp = temp.replace('.','-')
        tickers.append(temp.strip())

    symbols = dfamex.iloc[:, 0]
    for symb in symbols:
        #time.sleep(1)
        temp = symb.replace('^', '-')
        temp = temp.replace('.', '-')
        tickers.append(temp.strip())

    symbols = dfnyse.iloc[:, 0]
    for symb in symbols:
        #time.sleep(1)
        temp = symb.replace('^', '-')
        temp = temp.replace('.', '-')
        tickers.append(temp.strip())
        #print(temp)

    with open("alltickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    #print(tickers)
    return tickers

save_sp500_tickers()