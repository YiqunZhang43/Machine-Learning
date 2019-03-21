import pandas as pd

#looking for outlines in the file:
import pandas as pd
#data = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/sampled.csv")
#understand the data type
data = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/sampled.csv")
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
std = values.std
print(mean)
