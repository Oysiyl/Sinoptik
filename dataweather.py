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
import numpy as np

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
#print(df.plot.bar)

df2  = df.iloc[:, 1:-3]
#print(df2)

#df2[['tempMax','tempMin', 'maxTemp', 'minTemp', 'maxYear', 'minYear']] = df2[['tempMax','tempMin', 'maxTemp', 'minTemp', 'maxYear', 'minYear']].apply(pd.to_numeric, errors = 'ignore')
#
#df2 = df2.infer_objects()

#print(df2.dtypes)
#
#print(df2['tempMax'].max())
#print(df2['tempMin'].min())
#print(df2['maxTemp'].max())
#print(df2['minTemp'].min())
#print(df2['maxYear'].max())
#print(df2['minYear'].min())

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

years = list(range(1890,2010))

df3["year"] = years
print(df3["year"])
df3["year"].dtype
df2["maxYear0"] = df2["maxYear"].str.split(",")

#print(df2["maxYear0"])
wow = list(df2["maxYear0"])
#print((df2["minYear"] == 1971).sum())
#print(wow)
wow3 = df2["maxYear"].tolist()
#print(wow3)

wow4 = []

for i in list(range(len(wow3))):
    wow4.append(wow3[i].replace(" ", "").split(",")[-1])
#print(wow4)
#print(len(wow4))

hihi = Counter(wow4)

ignore = ["189","190","191","192","193","194","195","196","197","198","199","200","201"]
hyhy = Counter(wow4)
for word in list(hyhy):
    if word in ignore:
        del hyhy[word]
        
#print(hyhy)
#
#print(hihi)

hoho = Counter(years)

#print(hoho)

df6 = pd.DataFrame.from_dict(hyhy, orient='index').reset_index()
df6 = df6.rename(columns={'index':'year', 0:'count'})
result = df6.sort_values(['year'], ascending=True)
result = result[["year","count"]]
#print(result)
plt.hist(result, 12, density=True, facecolor='g', alpha=0.75)
#plt.xticks(range(1890,2010))
plt.title("Hot temperature per year")
plt.xlabel("year")
plt.ylabel("counts")
plt.show()
plt.bar(result["year"],result["count"])
plt.show()
plt.scatter(result["year"],result["count"])
plt.show()
plt.plot(result["year"],result["count"])
plt.xticks(rotation=90)
plt.show()




df3["year"] = years
#print(df3["year"])
df3["count"] = 0
#print(df3)



df3["year"].dtype
df2["minYear0"] = df2["minYear"].str.split(",")
#print(df2["minYear0"])
wow = list(df2["minYear0"])
#print((df2["minYear"] == 1971).sum())
#print(wow)
wow3 = df2["minYear"].tolist()
#print(wow3)

wow4 = []

for i in list(range(len(wow3))):
    wow4.append(wow3[i].replace(" ", "").split(",")[-1])
#print(wow4)
#print(len(wow4))

hihi = Counter(wow4)

ignore = ["189","190","191","192","193","194","195","196","197","198","199","200","201"]
hyhy = Counter(wow4)
for word in list(hyhy):
    if word in ignore:
        del hyhy[word]
       
#print(hyhy)
#
#print(hihi)

hoho = Counter(years)

#print(hoho)

df6 = pd.DataFrame.from_dict(hyhy, orient='index').reset_index()
df6 = df6.rename(columns={'index':'year', 0:'count'})
#result = df6.sort_values(['year'], ascending=True)
result = result[["year","count"]]
res = result["count"]
#for i in res:
    


##print(result)
#plt.hist(result, 12, density=True, facecolor='g', alpha=0.75)
##plt.xticks(range(1890,2010))
#plt.title("Cold temperature per year")
#plt.xlabel("year")
#plt.ylabel("counts")
#plt.show()
#plt.bar(result["year"],result["count"])
#plt.show()
#plt.scatter(result["year"],result["count"])
#plt.show()
#plt.plot(result["year"],result["count"])
#plt.xticks(rotation=90)
#plt.show()

#print(df3.dtypes)
#print(df6.dtypes)
way = pd.merge(df3,df6)
#print(way)

df11 = df3
df12 = df6

df12["year"] = df12["year"].astype(int)
#print(df11)
#print(df11.dtypes)
#print(df12)
#print(df12.dtypes)



#df = pd.DataFrame({
#    "year" : np.random.randint(1850, 2000, size=(100,)),
#    "qty" : np.random.randint(0, 10, size=(100,)),
#})
#
#df2 = pd.DataFrame({
#    "year" : np.random.randint(1850, 2000, size=(100,)),
#    "qty" : np.random.randint(0, 10, size=(100,)),
#})

df11 = df11.set_index("year")
df12 = df12.set_index("year")

df13 = df11.join(df12["count"], how = "outer", lsuffix='_left', rsuffix='_right')
df13 = df13.fillna(0)
df13["count_right"] = df13["count_right"].astype(int)
df13.reset_index()
df13["count_left"] = years
df13.rename(columns={"count_left": "year", "count_right": "count"}, inplace=True)
print(df13)
print(df13.dtypes)
result = df13
plt.hist(result, 12, density=True, facecolor='g', alpha=0.75)
#plt.xticks(range(1890,2010))
plt.title("Cold temperature per year")
plt.xlabel("year")
plt.ylabel("counts")
plt.show()
plt.bar(result["year"],result["count"])
plt.show()
plt.scatter(result["year"],result["count"])
plt.show()
plt.plot(result["year"],result["count"])
plt.xticks(rotation=90)
plt.show()


#def foo(x1, x2):
#    if x1 == x2:
#        return x2
#    else:
#        return x1
#
#df13["count"] = df13.apply(lambda row: foo(row["count_left"], row["count_left"]), axis=1)
#df13.drop(["count_left","count_right"], axis = 1, inplace = True)

#df1 = df1.drop('count', axis=1)
#df_new = df2.join(df1, on='year', how='left', lsuffix='_left', rsuffix='_right')
#df_new['count'] = df_new['count'].fillna(0)
#print(df_new)
#df3 = pd.concat([df1,df2], axis=0)
print(df13)
df13.to_csv("third.csv")

first = pd.read_csv("first.csv")
del first["Unnamed: 0"]
print(first)
#
#
#
#
#
#way2 = df6.join(df3, how="outer", on="count", lsuffix='_left', rsuffix='_right')
#print(way2)
#
#for index,row in way2.iterrows():  
#    print(row["year"],row["count_left"])
#    if row["year"] == row["year_right"]:
#       row["count_left"] = row["count_right"]
#    else:
#       row["count_left"] = 0
#print(df3)
#print(way2)
