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
import seaborn as sns

citys = ['chernigov','dnepr','donetsk','herson','Kharkov','kiev','lugansk','lvov','nikolaev','odessa','poltava','sympheropol','vinitsa','zaporozje']

i = 4

city = citys[i]

df = pd.read_csv(str(city) + ".csv")
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

years = list(range(1880,2010))

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

ignore = ["188","189","190","191","192","193","194","195","196","197","198","199","200","201","2"]
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

df6["year"] = df6["year"].astype(int)

df3 = df3.set_index("year")
df6 = df6.set_index("year")

df7 = df3.join(df6["count"], how = "outer", lsuffix='_left', rsuffix='_right')
df7 = df7.fillna(0)
df7["count"] = df7["count"].astype(int)
df7["year"] = years
print(df7)
#df7["count_right"] = df7["count_right"].astype(int)
#df7.reset_index()
#df7["count_left"] = years
df7.rename(columns={"count_left": "year", "count_right": "count"}, inplace=True, index = None)
print(df7)
print(df7.dtypes)
result = df7[["year","count"]]
#result.columns = result.columns.droplevel(level=0)
#print(result.index.nlevels)
#result = result.rename_axis(None)
#result.to_csv("resultitet.csv", index=False)
#result = pd.read_csv("resultitet.csv")
#del result["index"]
print(result)

#print(result)
plt.hist(result, 13, density=True, facecolor='g', alpha=0.75)
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

# Monthly plot of rainy days
#plt.figure(figsize=(12,8))
#sns.set_style("whitegrid")
#sns.set_context("notebook", font_scale=2)
#sns.barplot(x=result["year"], y=result["count"], data=result.sort_values(['year', 'count']))
#plt.xlabel("Years")
#plt.ylabel("Number of Records")
#plt.xticks(rotation=45)
#plt.title("Hot or Cold Records in Kharkiv")
#plt.show()

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
    wow4.append(wow3[i].replace(" ", "").split(",")[0])
#print(wow4)
#print(len(wow4))

hihi = Counter(wow4)

ignore = ["188","189","190","191","192","193","194","195","196","197","198","199","200","201","2"]
ignore2 = [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 2]
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

yay = [1880,0,0,0,0,0,0,0,0,0,1890,0,0,0,0,0,0,0,0,0,1900,0,0,0,0,0,0,0,0,0,1910,0,0,0,0,0,0,0,0,0,1920,0,0,0,0,0,0,0,0,0,1930,0,0,0,0,0,0,0,0,0,1940,0,0,0,0,0,0,0,0,0,1950,0,0,0,0,0,0,0,0,0,1960,0,0,0,0,0,0,0,0,0,1970,0,0,0,0,0,0,0,0,0,1980,0,0,0,0,0,0,0,0,0,1990,0,0,0,0,0,0,0,0,0,2000,0,0,0,0,0,0,0,0,2009]

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
print(df13)
print(len(years))
print(len(df13["count_left"]))
df13["count_left"] = years
df13.rename(columns={"count_left": "year", "count_right": "count"}, inplace=True, index = None)
print(df13)
print(df13.dtypes)
result2 = df13[["year","count"]]
#result2.reset_index(drop=False,inplace=True)
#result2.rename(columns={"":"index"}, inplace=True)
#result.columns = result.columns.droplevel(level=0)
#print(result2.index.nlevels)
#result2 = result2.rename_axis(None)
#result2.to_csv("resultite.csv", index=False)
#result2 = pd.read_csv("resultite.csv")
#del result2["index"]
print(result2)

#plt.xticks(range(1890,2010))
#plt.title("Hot temperature per year")
#plt.xlabel("year")
#plt.ylabel("counts")
#plt.show()
plt.bar(result["year"],result["count"])
plt.show()
plt.scatter(result["year"],result["count"])
plt.show()
plt.plot(result["year"],result["count"])
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize=(13,8))
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=2)
sns.barplot(x=result["year"], y=result["count"], data=result.sort_values(['year', 'count']))
plt.xlabel("Years from 1880 to 2010")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.title("Hot Records in " + str(city))
plt.xticks([])
plt.show()


plt.bar(result2["year"],result2["count"])
plt.show()
plt.scatter(result2["year"],result2["count"])
plt.show()
plt.plot(result2["year"],result2["count"])
plt.xticks(rotation=90)
plt.show()


#print(len(yay))
#print(result2)
# Monthly plot of rainy days
plt.figure(figsize=(13,8))
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=2)
sns.barplot(x=result2["year"], y=result2["count"], data=result2.sort_values(['year', 'count']))
plt.xlabel("Years from 1880 to 2010")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.title("Cold Records in " + str(city))
plt.xticks([])
plt.show()


result2["wow"] = yay
result["wow"] = yay
second = result2["count"].tolist()
first = result["count"].tolist()
ten = ["1880-1890", "1890-1900", "1900-1910", "1910-1920", "1920-1930", "1930-1940", "1940-1950", "1950-1960", "1960-1970", "1970-1980", "1980-1990", "1990-2000", "2000-2010"]
ten2 = ["1887-1897", "1897-1907", "1907-1917", "1917-1927", "1927-1937", "1937-1947", "1947-1957", "1957-1967", "1967-1977", "1977-1987", "1987-1997", "1997-2007", "2007-2017"]
tencountsfirst = []
tencountssecond = []

print(first)
print(second)

for i in range(len(second)):
    k = second[i]
    if (i == 9):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 19):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 29):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 39):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 49):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 59):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 69):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 79):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 89):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 99):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 109):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 119):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
    if (i == 129):
        k = second[i-9] + second[i-8] + second[i-7] + second[i-6] + second[i-5] + second[i-4] + second[i-3] + second[i-2] + second[i-1] + second[i]
        tencountssecond.append(k)
        
        
print(tencountssecond)

for i in range(len(first)):
    k = first[i]
    if (i == 9):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 19):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 29):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 39):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 49):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 59):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 69):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 79):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 89):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 99):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 109):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 119):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
    if (i == 129):
        k = first[i-9] + first[i-8] + first[i-7] + first[i-6] + first[i-5] + first[i-4] + first[i-3] + first[i-2] + first[i-1] + first[i]
        tencountsfirst.append(k)
        
        
print(tencountsfirst)

df21 = pd.DataFrame({"year":ten, "count": tencountsfirst})
df22 = pd.DataFrame({"year":ten, "count": tencountssecond})
print(df21)
print(df22)

plt.bar(df21["year"],df21["count"])
plt.xticks(rotation=90)
plt.show()
plt.scatter(df21["year"],df21["count"])
plt.xticks(rotation=90)
plt.show()
plt.plot(df21["year"],df21["count"])
plt.xticks(rotation=90)
plt.show()


#print(len(yay))
#print(result2)
# Monthly plot of rainy days
plt.figure(figsize=(13,8))
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=2)
sns.barplot(x=df21["year"], y=df21["count"], data=df21.sort_values(['year', 'count']))
plt.xlabel("Years from 1880 to 2010")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.title("Hot Records in " + str(city))
#plt.xticks([])
plt.show()

plt.bar(df22["year"],df22["count"])
plt.xticks(rotation=90)
plt.show()
plt.scatter(df22["year"],df22["count"])
plt.xticks(rotation=90)
plt.show()
plt.plot(df22["year"],df22["count"])
plt.xticks(rotation=90)
plt.show()

#print(len(yay))
#print(result2)
# Monthly plot of rainy days
plt.figure(figsize=(13,8))
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=2)
sns.barplot(x=df22["year"], y=df22["count"], data=df22.sort_values(['year', 'count']))
plt.xlabel("Years from 1880 to 2010")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.title("Cold Records in " + str(city))
#plt.xticks([])
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
#print(result)
#result.to_csv("third.csv")
#
#first = pd.read_csv("first.csv")
#del first["Unnamed: 0"]
#print(first)
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
