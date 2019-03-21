import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.metrics import classification_report
from  sklearn import  svm

import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import scale


data = pd.read_csv("/*/sampled.csv")
data2 = pd.read_csv("/*/sampled2.csv")
X = data.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
Y = data["target"]
X_test = data2.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
Y_test = data2["target"]

X =scale(X)
LogReg = LogisticRegression()
LogReg.fit(X,Y)
y_pred_Log = LogReg.predict(X)

gnb = GaussianNB()
gnb = gnb.fit(X, Y)
y_pred_gnb = gnb.predict(X)
clf = tree.DecisionTreeClassifier(criterion= "entropy", splitter="random")
clf = clf.fit(X, Y)
Y_pred_clf = clf.predict(X)
clf = svm.SVC()
clf = clf.fit(X,Y)
Y_pred_svm = clf.predict(X_test)
print(classification_report(Y_test, Y_pred_svm))

print(len(y_pred_Log))
print(len(y_pred_gnb))
print(len(Y_pred_clf))

d = {"log" : y_pred_Log, "gnb" :y_pred_gnb, "clf":Y_pred_clf, "svm" :Y_pred_svm}
RESULT = pd.DataFrame(d)
print(RESULT)
Final_result = RESULT.mode(axis=1)
Final_pred = Final_result.ix[:,0].astype(int)
print(type(y_pred_Log[1]))
print(type(Final_result.ix[:,0][1]))
print(classification_report(Y_test, y_pred_gnb))
print(classification_report(Y_test, y_pred_Log))
print(classification_report(Y_test, Y_pred_clf))
print(classification_report(Y_test, Y_pred_svm))
print(classification_report(Y_test, Final_pred                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ))
