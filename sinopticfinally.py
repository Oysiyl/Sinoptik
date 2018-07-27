#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 20:18:48 2018

@author: dmitriy
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

citys = ['chernigov','dnepr','donetsk','herson','Kharkov','kiev','lugansk','lvov','nikolaev','odessa','poltava','sympheropol','vinitsa','zaporozje']

toocitys = ['чернигов', 'днепр-303007131', 'донецк', 'херсон', 'харьков', 'киев', 'луганск', 'львов', 'николаев', 'одесса', 'полтава', 'симферополь', 'винница', 'запорожье']

i = 13

city = toocitys[i]

y = 2017
m = 1
d = 1

months = [31,28,31,30,31,30,31,31,30,31,30,31]

#month2 = [sum(month[:i+1]) for i in range(len(month))]

def prepareadres(city,y,m,d):
    
    #months2 = [028, 31]
    d = d + 1
    d0 = 0
    m0 = 0
    for month in months:
        if d > 31:
             d = d - month
             m += 1
    if d == sum(months):    
        print("year complete")
        #print(df.iloc[0, :-2])
    if (m < 10) and (d < 10):
        adres = "https://sinoptik.ua/погода-" + city + "/" + str(y) + "-" + str(m0) + str(m) + "-" + str(d0) + str(d)
    elif (m < 10) and (d >= 10):
        adres = "https://sinoptik.ua/погода-" + city + "/" + str(y) + "-"+ str(m0) + str(m) + "-" + str(d)
    elif (m >= 10) and (d < 10):
        adres = "https://sinoptik.ua/погода-" + city + "/" + str(y) + "-" + str(m) + "-" + str(d0) + str(d)   
    else:
        adres = "https://sinoptik.ua/погода-" + city + "/" + str(y) + "-" + str(m) + "-" + str(d)
    #print(adres)
    return adres

year = sum(months)

adres2 = [prepareadres(city,y,m,i) for i in range(year)]

print(adres2)
print(len(adres2))

def weather(adres):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    page = requests.get(adres, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    up = soup.find("p", class_ = "infoHistoryval")
    up = list(up)
    infoDayweek = soup.find("p", class_ = "infoDayweek")
    infoDayweek = list(infoDayweek)[0]

    infoDate = soup.find("p", class_ = "infoDate")
    infoDate = list(infoDate)[0]
    infoMonth = soup.find("p", class_ = "infoMonth")
    infoMonth = list(infoMonth)[0]
    infoDaylight = soup.find(class_ = "infoDaylight")
    infoDaylight = list(infoDaylight)

    sunUp = infoDaylight[1].get_text()
    sunDown = infoDaylight[3].get_text()

    maxTemp = up[3].get_text()
    maxYear = up[4]
    maxYear = maxYear.replace("(", "")
    maxYear = maxYear.replace(")", "")

    minTemp = up[9].get_text()
    minYear = up[10]
    minYear = minYear.replace("(", "")
    minYear = minYear.replace(")", "")

    h2 = soup.find_all("div", class_ = "description")
    dayInfo = list(h2)[0].get_text()
    dayHistory = list(h2)[1].get_text()

    tempMax = soup.find("div", class_ = "max")
    tempMax = list(tempMax)[1].get_text()
    tempMin = soup.find("div", class_ = "min")
    tempMin = list(tempMin)[1].get_text()  

# find a problem!
    
    df1 = pd.DataFrame({
    "infoDayweek": infoDayweek,
    "infoDate": infoDate,
    "infoMonth": infoMonth,
    "sunUp": sunUp,
    "sunDown": sunDown,
    "tempMax": tempMax,
    "tempMin": tempMin,
    "maxTemp": maxTemp, 
    "maxYear": maxYear, 
    "minTemp": minTemp, 
    "minYear": minYear,
    "dayInfo": dayInfo,
    "dayHistory": dayHistory
    }, index=[0])
    check = df1.iloc[0, 0:-2]
    print(check)

    return df1
    


df = pd.DataFrame()

for url in adres2:
    df = pd.concat([df, weather(url)], ignore_index = True)
    
print(df)
print(df.iloc[:, 0:-2])
df.to_csv(citys[i] + ".csv")
df = pd.read_csv(citys[i] + ".csv")
#df2 = df.iloc[:,1:-2]
#print(df)
#df2.to_csv("results.csv")
