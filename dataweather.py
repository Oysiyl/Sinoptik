#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:46:13 2018

@author: dmitriy
"""
from datetime import timedelta
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv("Kharkov.csv")
df = df.iloc[:,1:]
print(df)
print(df.columns)

#df["wow"] = df["sunDown"] - df["sunUp"]
print(df.info())

year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)

df.sunUp = pd.to_datetime(df.sunUp, format='%H:%M')
df.sunDown = pd.to_datetime(df.sunDown, format='%H:%M')
#print(df.sunUp)
#print(df.sunDown)

wiwi = list(df.sunDown - df.sunUp)

c = (df['sunDown'] - df['sunUp'])\
              .dt.components[['days', 'hours', 'minutes']]
df['diff'] = (c.days * 24 + c.hours).astype(str) + 'h ' + c.minutes.astype(str) + 'm'
#print(df['diff'])
print(df.plot.bar)

df2  = df.iloc[:, 1:-3]
print(df2)

#df2[['tempMax','tempMin', 'maxTemp', 'minTemp', 'maxYear', 'minYear']] = df2[['tempMax','tempMin', 'maxTemp', 'minTemp', 'maxYear', 'minYear']].apply(pd.to_numeric, errors = 'ignore')
#
#df2 = df2.infer_objects()

print(df2.dtypes)

print(df2['tempMax'].max())
print(df2['tempMin'].min())
print(df2['maxTemp'].max())
print(df2['minTemp'].min())
print(df2['maxYear'].max())
print(df2['minYear'].min())

import datetime

now = datetime.datetime.now()

print("Current date and time using str method of datetime object:")
print(str(now))
print("Current date and time using strftime:")
print(now.strftime("%Y-%m-%d"))
a = now.year
b = now.month
c = now.day
print(a)
print(b)
print(c)
df3 = pd.DataFrame()

years = list(range(1891,2011))

df3["year"] = years
print(df3["year"])
df3["year"].dtype
df2["maxYear0"] = df2["maxYear"].str.split(",")
print(df2["maxYear0"])
wow = list(df2["maxYear0"])
print((df2["minYear"] == 1971).sum())
print(wow)
wow3 = df2["maxYear"].tolist()
print(wow3)

wow4 = []

for i in list(range(len(wow3))):
    wow4.append(wow3[i].replace(" ", "").split(",")[-1])
print(wow4)
print(len(wow4))

hihi = Counter(wow4)

df6 = pd.DataFrame.from_dict(hihi, orient='index').reset_index()
df6 = df6.rename(columns={'index':'year', 0:'count'})
result = df6.sort_values(['year'], ascending=True)
print(result)
plt.hist(result)
#plt.xticks(result["count"])
plt.title("Hot temperature per year")
plt.xlabel("year")
plt.ylabel("counts")
plt.show()

df3["year"] = years
print(df3["year"])
df3["year"].dtype
df2["maxYear0"] = df2["maxYear"].str.split(",")
print(df2["maxYear0"])
wow = list(df2["maxYear0"])
print((df2["minYear"] == 1971).sum())
print(wow)
wow3 = df2["minYear"].tolist()
print(wow3)

wow4 = []

for i in list(range(len(wow3))):
    wow4.append(wow3[i].replace(" ", "").split(",")[-1])
print(wow4)
print(len(wow4))

hihi = Counter(wow4)

df6 = pd.DataFrame.from_dict(hihi, orient='index').reset_index()
df6 = df6.rename(columns={'index':'year', 0:'count'})
result = df6.sort_values(['year'], ascending=True)
print(result)
plt.hist(result)
#plt.xticks(range(1890,2010))
plt.title("Cold temperature per year")
plt.xlabel("year")
plt.ylabel("counts")
plt.show()
#df.groupby(['country','place'], as_index=False)['value'].max()
#df.wiw = ""
#for i in range(len(wiwi)):
#    i = wiwi[i]
#    df.append(i)

#print(df.wiw)
#wiwi = df.sunUp.strftime("%h/%m")
