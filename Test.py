#STESDFSD
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

#enc = OneHotEncoder(handle_unknown="ignore")
data = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/LendingClub/random.csv")
print(data.info())
data2=pd.get_dummies(data)
print(data.shape)
print(data2.shape)
Y = data[""]
test = SelectKBest(score_func= chi2, k=4)
fit = test.fit()
"""
cat_features_data = data.select_dtypes(include = ["object"]).copy()
cat_features=cat_features_data.columns
enc = LabelEncoder()
enc.fit(cat_features_data)
new_cat_features =enc.transform(cat_features)
new_cat_features = new_cat_features.reshape(-1,1)
ohe = OneHotEncoder(sparse=False) #Easier to read
print(ohe.fit_transform(new_cat_features))
"""