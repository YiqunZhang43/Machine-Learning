import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import pylab
import os
import random
from numpy.polynomial.polynomial import polyfit

BankData = pd.read_excel("/Users/yiqunzhang/Desktop/Virtusa/Group_Dep_Emp.xlsx")
print(BankData.columns)
Done_list = []

"""
Hline ="dep_per_emp16-17"
Vline = " numemp 17-16"
fig, ax = plt.subplots()
ax.scatter(BankData[Hline], BankData[Vline])
for i, txt in enumerate(BankData["name"]):
    ax.annotate(txt, (BankData[Hline][i], BankData[Vline][i]), fontsize=7)
plt.axhline(y=BankData[Vline].mean(), color='r', linestyle='-')
plt.axvline(x=BankData[Hline].mean(), color='r', linestyle='-')
plt.xlabel(Hline)
plt.ylabel(Vline)
plt.xlim((-1,1))
plt.ylim((-1,1))
plt.title("Deposit per Employee VS Number of Employee 16-17", fontsize=12)
filename = Hline[:-5] + Vline
filename = filename.replace("/", "_")
fig.savefig("/Users/yiqunzhang/Desktop/Virtusa/Graphs/" + filename + ".png")
plt.show()
"""
for i in range(0,200):
    Item = np.random.choice(BankData.columns[1:8], 2, replace=False)
    Item = sorted(Item.tolist())
    Hline = Item[0]
    Vline = Item[1]
   # Hline = float(Hline)
   # Vline = float(Vline)
    print(type((Hline[1])))

    #results = sm.OLS(np.array(Vline), sm.add_constant(np.array(Hline)).fit())
    #b,m = polyfit(np.array(Hline), np.array(Vline),deg=1)#np.array(Hline) * results.params[0] + results.params[1])
    Inner = list([Hline, Vline])
    if (Hline[-4:] == Vline[-4:]) & (Hline[:5] != Vline[:5]) & (Inner not in Done_list):
        fig, ax = plt.subplots()

        ax.scatter(BankData[Hline], BankData[Vline])#, c= BankData["Signal"])
        #ax.plot(BankData[Hline],0.017 + 1.3 * BankData[Hline],"-", c = "green")
        #   plt.plot((BankData[Hline].mean(), 0.017 + 1.3 * BankData[Hline].mean()), '-')
        for i, txt in enumerate(BankData["name"]):
            ax.annotate(txt, (BankData[Hline][i], BankData[Vline][i]), fontsize=7)
        plt.axhline(y=BankData[Vline].mean(), color='r', linestyle='-')
        plt.axvline(x=BankData[Hline].mean(), color='r', linestyle='-')
        plt.xlabel("Deposit per Employee Growth Rate(%)")
        plt.ylabel("Number of Employee Growth Rate (%)")
        #plt.legend(handles =BankData["Signal"] )
        #plt.xlim((0.35, 0.8))
        #plt.ylim((0.5, 11))
        #my_x_ticks = np.arange(0.4, 0.8, 0.1)
        #my_y_ticks = np.arange(1, 11, 1)
        #plt.xticks(my_x_ticks)
        #plt.yticks(my_y_ticks)
        plt.title(Hline + " VS "+Vline, fontsize=12)
        #plt.plot((BankData[Hline], 0.017 + 1.3 * BankData[Hline]), '-')
        filename = Hline[:-5] + Vline
        filename =  filename.replace("/", "_")
        fig.savefig("/Users/yiqunzhang/Desktop/Virtusa/Graphs/" + filename + ".png")
        #plt.show()
        Done_list.append(Inner)
    else:
        print("bad luck!")



#Hline='opt cost 18-17'
#Vline = 'total deposit18-17'

"""
"""