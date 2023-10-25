# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:32:44 2023

@author: USER
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

data = requests.get(url,headers=header)  
data.encoding = 'utf-8'
data = data.text

soup = BeautifulSoup(data,'html.parser')  

rates = soup.find(id='exchangeRate')

tbody = rates.find('tbody')

trs = tbody.find_all('tr')  #[2:] #切片 取第二個開始到最後一個

for row in trs:
    tds = row.find_all('td',recursive=False) 
    #recursive=False 關閉遞迴只抓一層(下一層)的子節點  
    if len(tds) == 4:
        
        print(tds[0].text.strip().split()[0])
        print(tds[1].text.strip())
        print(tds[2].text.strip())
        print(tds[3].text.strip())
        print()
        print()

    

   