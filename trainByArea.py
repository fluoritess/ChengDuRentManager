import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import re
from sklearn.linear_model import LinearRegression
from lxml import etree
import time
mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
Date = pd.read_csv('cdlianjia2.csv')
# 获取面积
house_area_ = list(Date.groupby('面积').size().index)
#当前面积平均价钱
housearea_mean_price=[]
house_area_1=[]
for house_area in house_area_:
    housearea_num = re.sub("\D", "", house_area)
    if housearea_num != '':
        housearea_num = int(housearea_num)
        if housearea_num < 1000 and housearea_num>10:  # 剔除异常数据
            house_area_1.append(housearea_num)
            # 获取当前面积数据
            house_area_Data = Date.loc[Date['面积'] == house_area]
            # 取出当前面积所有数据
            price_ = house_area_Data['价钱']
            # 存取当前面积房租的集合
            price_num_total = []
            # 存取当前面积房租总价
            price_num_all = 0
            for price in price_:
                price_num = re.sub("\D", "", price)
                price_num = int(price_num)
                if price_num < 100000:  # 剔除反常数据
                    price_num_total.append(price_num)
            for i in range(len(price_num_total)):
                price_num_all = price_num_all + price_num_total[i]
            # 当前面积房租平均价钱
            price_mean = price_num_all / len(price_num_total)
            housearea_mean_price.append(price_mean)
print(len(house_area_1))
print(len(housearea_mean_price))
#下面是训练代码
linearReg = LinearRegression()
X = np.array([house_area_1])
y = np.array([housearea_mean_price])
X = X[y <= 30000] #只考虑租房价格30000元以内的房子
y = y[y <= 30000] #只考虑租房价格30000元以内的房子
X = X.reshape(-1,1) #转成二维数组，固定1列（一个特征），行为自动
plt.scatter(X,y,color="b")  #根据矩阵X和向量y，把训练及的点画在图形上
linearReg.fit(X,y)  #根据矩阵X和向量y，进行训练
k = linearReg.coef_[0]  #系数
b = linearReg.intercept_ #截距
plt.plot(X,k * X + b,color="r")  # 根据训练所得的系数k和截距b，画出所得模型，其实就是直线方程 y = kX + b
plt.xlabel("房子面积")
plt.ylabel("租房价格")

#下面是预测代码
predict_x = [[50],[100],[150],[200]] #分别预测面积未50和120的租房价格
predict_y = linearReg.predict(predict_x)
print(predict_y)
plt.scatter(predict_x,predict_y,color="g") #预测的两个点画到图形上

plt.legend()
plt.show() #显示图形