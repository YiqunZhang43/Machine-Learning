import pandas as pd
import os
from sklearn.decomposition import FactorAnalysis
data= pd.read_csv("/*/sampled.csv")
print(data.columns)
data = data.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
print(data.corr())
cor = data.corr()
os.chdir("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/")
cor.to_csv("cor.csv")