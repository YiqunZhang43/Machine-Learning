import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report

train = pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/train.csv")

ones = train[train["target"] == 1]
zeros = train[train["target"] == 0]
ones = ones.sample(200)
zeros = zeros.sample(200)
sampled = pd.concat([ones, zeros])
sampled.to_csv("sampled.csv")

sampled_2 = train.sample(400)
sampled_2.to_csv("sampled2.csv")
data = train.sample(400)
#ata= pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/sampled.csv")
#choose those data we find useful in the first place:
print(data.columns)
X = data.drop(['ID_code', 'target'],axis= 1)
#X =data.drop(['ID_code', 'target'])
#X = data[["var_81","var_12","var_139","var_22","var_26","var_110","var_133","var_44","var_99","var_80","var_179","var_0","var_53","var_166"
   # , "var_76","var_6","var_26","var_198","var_170","var_174","var_146","var_1","var_2","var_21"]]

Y = data["target"]
data2= pd.read_csv("/Users/yiqunzhang/Desktop/MyOwnProject/Santander/sampled2.csv")
X_test = data2.drop(['Unnamed: 0', 'Unnamed: 0.1', 'ID_code', 'target'],axis= 1)
# X_test = data2[["var_81","var_12","var_139","var_22","var_26","var_110","var_133","var_44","var_99","var_80","var_179","var_0","var_53","var_166"
 #   , "var_76","var_6","var_26","var_198","var_170","var_174","var_146","var_1","var_2","var_21"]]
Y_test = data2["target"]
#check the correlation metrics and plot it

print(X.corr())
#the result shows that they almost don't have a correlation.
#plt.show()
X = scale(X)
LogReg = LogisticRegression()
LogReg.fit(X,Y)
y_pred = LogReg.predict(X)
y_pred_test = LogReg.predict(X_test)
print(classification_report(Y, y_pred))
print(classification_report(Y_test,y_pred_test))
print(y_pred_test)
print(X_test.head())
print(LogReg.coef_)