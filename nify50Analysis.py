# -*- coding: utf-8 -*-
"""
Created on Sun May 13 13:21:21 2018

@author: bhavesh
"""
import bs4 as bs
import pickle
import requests

resp = requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
soup = bs.BeautifulSoup(resp.text, 'lxml')
tables = soup.find_all('table',  
                      {'id' : 'constituents'})
tickers = []
for t in tables:
    for row in t.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker)
    with open("nifty100tickers.pickle","wb") as f:
        pickle.dump(tickers, f)
    
#constituents