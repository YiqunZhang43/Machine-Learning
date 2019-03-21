import pandas as pd
import os
from scipy import  stats
from collections import Counter

os.chdir("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/")

#select only two hundreds rows
list = []

train = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/nonoutlier.csv")
#we randome choose the cleaned data, then we test if the mean and variance is different, if different, we record, and only
## choose the variables which has the high frequency in the test.
for i in range(1,50):
    #print(train.info())
    #print(train.columns)
    print(train["target"].count())
    ones = train[train["target"] == 1]
    zeros = train[train["target"] == 0]
    ones = ones.sample(200)
    zeros = zeros.sample(200)
    sampled = pd.concat([ones, zeros])
    sampled.to_csv("sampled.csv")
    sampled_2 = train.sample(400)
    sampled_2.to_csv("sampled2.csv")

    # Y = train["target"]
    # X = train.drop(["target", "ID_code"], axis= 1)
    data = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/sampled.csv")
    print(data.info)
    data_1 = data[data["target"] == 1]
    data_0 = data[data["target"] == 0]
    # conduct a T-test between samples, seen which variable is truly different.
    print(data_1.describe())
    print(data_0.describe())
    for column in data.columns[3:]:
        p1, p2 = stats.levene(data_1[column], data_0[column])
        if p2 < 0.1:
            list.append(column)
    for column in data.columns[3:]:
        p1, p2 = stats.ttest_ind(data_1[column], data_0[column])
        if p2 < 0.1:
            list.append(column)

counted = Counter(list)
print(type(counted))
print(counted.most_common(40))
print(type(counted[1]))
counter = pd.DataFrame(counted)

counter.to_csv("counter.csv")