#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 20:18:48 2018

@author: dmitriy
"""
#import all the necessary libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
#Create a list which contains names of the citys
citys = ['chernigov','dnepr','donetsk','herson','Kharkov', \
         'kiev','lugansk','lvov','nikolaev','odessa', \
         'poltava','sympheropol','vinitsa','zaporozje']
#Another list with city`s names in Russian
toocitys = ['чернигов', 'днепр-303007131', 'донецк', 'херсон', 'харьков', \
            'киев', 'луганск', 'львов', 'николаев', 'одесса', \
            'полтава', 'симферополь', 'винница', 'запорожье']
#Choose what city you want to scrape
i = 4
city = toocitys[i]
#Choose year
y = 2018
#Set month and days variables to 1
m = 1
d = 1
#Create list with number of days in each month
months = [31,28,31,30,31,30,31,31,30,31,30,31]
#Found the sum of list above
year = sum(months)
#Check sum: correct or not?
print(year)
#Create function that create adresses
def prepareadres(city,y,m,d):
    #Define iterator
    d = d + 1
    #Set days iterator to 0
    d0 = 0
    #Set month iterator to 0
    m0 = 0
    r = 0
    #Using for loop to get the correct adresses
    for month in months:
        k = months[r]
        if d > k:
             d = d - k
             m += 1
             r += 1
    if d == sum(months):    
        print("year complete")
        print(df.iloc[0, :-2])
    if (m < 10) and (d < 10):
        adres = "https://sinoptik.ua/погода-" + city + "/" + str(y) + "-" + str(m0) + str(m) + "-" + str(d0) + str(d)
    elif (m < 10) and (d >= 10):
        adres = "https://sinoptik.ua/погода-" + city + "/" + str(y) + "-"+ str(m0) + str(m) + "-" + str(d)
    elif (m >= 10) and (d < 10):
        adres = "https://sinoptik.ua/погода-" + city + "/" + str(y) + "-" + str(m) + "-" + str(d0) + str(d)   
    else:
        adres = "https://sinoptik.ua/погода-" + city + "/" + str(y) + "-" + str(m) + "-" + str(d)
    print(adres)
    return adres
#Got all the adresses
adres2 = [prepareadres(city,y,m,i) for i in range(year)]
#Check output
print(adres2)
print(len(adres2))
#Create function that scraping full one page from site
def onepage(adres):
    
    headers = {'User-Agent': 'Mozilla/5.0'}
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
    #Cheack output
    print(check)
    #Return df
    return df1

#Create an empty DataFrame  
df = pd.DataFrame()
#Adding each new page in one DataFrame
for url in adres2:
    df = pd.concat([df, onepage(url)], ignore_index = True)
#Check df    
print(df)
print(df.iloc[:, 0:-2])
#Save to csv
df.to_csv(citys[i] + ".csv")
df = pd.read_csv(citys[i] + ".csv")
