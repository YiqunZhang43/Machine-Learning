from sklearn import tree
import pandas as pd
from sklearn.metrics import classification_report
import os
os.chdir("/*/")
data = pd.read_csv("/*/sampled.csv")
data2 = pd.read_csv("/*/sampled2.csv")
X = data.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
Y = data["target"]
X_test = data2.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
Y_test = data2["target"]
clf = tree.DecisionTreeClassifier(criterion= "entropy", splitter="random")
clf = clf.fit(X, Y)
Y_pred = clf.predict(X_test)
print(X_test.head())
print(Y_pred)
print(classification_report(Y_test,Y_pred))
print(clf.feature_importances_)
feature = pd.DataFrame(clf.feature_importances_)
feature.to_csv("Feature.csv")