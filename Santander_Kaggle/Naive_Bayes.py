import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.metrics import classification_report
data = pd.read_csv("/*/sampled.csv")
data2 = pd.read_csv("/*/sampled2.csv")
X = data.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
Y = data["target"]
X_test = data2.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
Y_test = data2["target"]
gnb = GaussianNB()
gnb = gnb.fit(X, Y)
y_pred = gnb.predict(X)
print(classification_report(Y_test,y_pred))
print(y_pred)
