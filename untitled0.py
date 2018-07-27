#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:13:20 2018

@author: dmitriy
"""

import pandas as pd

citys = ['chernigov','dnepr','donetsk','herson','Kharkov','kiev','lugansk','lvov','nikolaev','odessa','poltava','sympheropol','vinitsa','zaporozje']

for i,word in enumerate(citys):
    print(citys[i])
    word = citys[i]
    print(word)
    df = pd.read_csv(word + ".csv")
    df = df.assign(city = citys[i])
    df123 = df.iloc[:,-14:]
    print(df123)
    df123.to_csv(word + ".csv")

df0 = pd.read_csv('chernigov.csv')
df0.to_csv('all.csv')

for i,word in enumerate(citys):
    word = citys[i]
    df = pd.read_csv(word + ".csv")
    df1 = pd.read_csv("all.csv")
    df2 = pd.concat([df1, df], ignore_index = True)
    df123 = df.iloc[:,-14:]
    print(df123)
    df2.to_csv("all.csv", index = False)

df2 = pd.read_csv("all.csv")
print(df2.columns[-14:])
df3 = df2.iloc[:,-14:]
print(df3)
df4 = df3[df3.columns[::-1]]
print(df4)
#df3.columns = df0.columns[-14:]
print(df3)
df3.to_csv("allcity.csv")
print(df0.columns[-14:])
print(df3.columns)