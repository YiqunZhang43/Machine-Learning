from  sklearn import  svm
import pandas as pd
from sklearn.metrics import classification_report

data = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/sampled.csv")
data2 = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/sampled2.csv")
X = data.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
Y = data["target"]
X_test = data2.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
Y_test = data2["target"]

clf = svm.SVC()
clf = clf.fit(X,Y)
Y_pred = clf.predict(X_test)
print(classification_report(Y_test, Y_pred))