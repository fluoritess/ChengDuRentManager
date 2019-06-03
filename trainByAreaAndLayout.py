import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn import  metrics
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier

mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
Date = pd.read_csv('csv/completed.csv')
X=Date.loc[:,['面积','所属区']]
y=Date.loc[:,['价钱']]
#多元线性回归
linreg=LinearRegression()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.9,random_state=0)
model=linreg.fit(X_train,y_train)
y_pred=linreg.predict(X_test)
plt.figure()
plt.plot(range(len(y_pred[120:250])),y_pred[120:250],'b',label="price_predict")
plt.plot(range(len(y_pred[120:250])),y_test[120:250],'r',label="price_test")
plt.legend(loc="upper right")
plt.show()

#随机森林
try:
    clf = joblib.load('random.h5')  # 加载API
except:
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    joblib.dump(clf, "random.h5")  # 保存
y_pred2 = clf.predict(X_test)
plt.figure()
plt.plot(range(len(y_pred2[120:250])),y_pred2[120:250],'b',label="price_predict")
plt.plot(range(len(y_pred2[120:250])),y_test[120:250],'r',label="price_test")
plt.legend(loc="upper right")
plt.show()
#朴素贝叶斯
try:
        mnb = joblib.load('mnb.pkl')
except:
        mnb = MultinomialNB()  # 使用默认配置初始化朴素贝叶斯
        mnb.fit(X_train,y_train)    # 利用训练数据对模型参数进行估计
y_pred3 = mnb.predict(X_test)     # 对参数进行预测
plt.figure()
plt.plot(range(len(y_pred3[120:250])),y_pred3[120:250],'b',label="price_predict")
plt.plot(range(len(y_pred3[120:250])),y_test[120:250],'r',label="price_test")
plt.legend(loc="upper right")
plt.show()

# #多层感知机
# #定义模型
# try:
#         MLP = joblib.load('MLP.pkl')
# except:
#         MLP =  MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(30,20), random_state=1)
#         MLP.fit(X_train,y_train)
# y_pred6=MLP.predict(X_test)
# plt.figure()
# plt.plot(range(len(y_pred6[120:250])),y_pred6[120:250],'b',label="price_predict")
# plt.plot(range(len(y_pred6[120:250])),y_test[120:250],'r',label="price_test")
# plt.legend(loc="upper right")
# plt.show()
# sum_mean=0
# for i in range(len(y_pred)):
#     sum_mean+=(y_pred[i]-y_test.values[i])**2
# sum_erro=np.sqrt(sum_mean/33000)
# print("RMSE:",sum_erro)
# df_corr = Date.corr()
# # 可视化
# import matplotlib.pyplot as mp, seaborn
# seaborn.heatmap(df_corr, center=0, annot=True)
# mp.show()
#Kmeans
#定义模型
# try:
#         kmeans = joblib.load('kmeans.pkl')
# except:
#         kmeans = KMeans(n_clusters=10).fit(X_train)
# y_pred5=kmeans.predict(X_test)
# plt.figure()
# plt.plot(range(len(y_pred5[120:250])),y_pred5[120:250],'b',label="price_predict")
# plt.plot(range(len(y_pred5[120:250])),y_test[120:250],'r',label="price_test")
# plt.legend(loc="upper right")
# plt.show()
#逻辑回归
# try:
#         clf = joblib.load('逻辑回归.pkl')#加载API
# except:
#         clf = LogisticRegression()#使用逻辑回归创建分类器对象
#         clf.fit(X_train, y_train) #用训练数据拟合分类器模型
# y_pred4 = clf.predict(X_test) #用训练好的分类器去预测
# plt.figure()
# plt.plot(range(len(y_pred4[120:250])),y_pred4[120:250],'b',label="price_predict")
# plt.plot(range(len(y_pred4[120:250])),y_test[120:250],'r',label="price_test")
# plt.legend(loc="upper right")
# plt.show()