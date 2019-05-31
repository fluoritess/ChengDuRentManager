import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import re
from lxml import etree
import time
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
Date = pd.read_csv('csv/completed.csv')
X=Date.loc[:,['面积','所属区']]
y=Date.loc[:,['价钱']]
X=X[1:200]
y=y[1:200]
linreg=LinearRegression()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.8,random_state=0)
model=linreg.fit(X_train,y_train)
y_pred=linreg.predict(X_test)
plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label="price_predict")
plt.plot(range(len(y_pred)),y_test,'r',label="price_test")
plt.legend(loc="upper right")
plt.show()