#looking for outlines in the file:
import pandas as pd
import os
#data = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/sampled.csv")
#understand the data type
os.chdir("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/")
data = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/train.csv")
#print(data.select_dtypes(include = ["object", "int"]))
#looks like only unnamed, ID_code and Target is object or int
#now we are looking for the outlines
#select only the float type
values = data.select_dtypes(include = ["float64"])
##use iqr method i got 74/400 outilner, which is not appriate
"""
percentile = values.quantile([0.25, 0.75])
distance = 1.5*(percentile.iloc[1]-percentile.iloc[0])
upper = percentile.iloc[1]+distance
lower = percentile.iloc[0]-distance
"""
mean = values.mean()
std = values.std()
print(mean)
upper = mean + 3.0*std
lower = mean - 3.0*std

#print(data)
Outliner_list = []
for columns in upper.index:
    Outliner_list.append(list(data[data[columns] > upper[columns]].index.values))
    Outliner_list.append(list(data[data[columns] < lower[columns]].index.values))

Outliner_list_flat = []
for sub in Outliner_list:
    for item in sub:
        Outliner_list_flat.append(item)
Outliner_list_flat = list(set(Outliner_list_flat))
print(len(Outliner_list_flat))
nonoutlier = data.drop(Outliner_list_flat)
print(data.groupby(["target"])["target"].count())
print(nonoutlier.groupby(["target"]).count())
nonoutlier.to_csv("nonoutlier.csv")


