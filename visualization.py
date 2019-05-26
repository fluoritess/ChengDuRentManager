import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import re
mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
Date = pd.read_csv('cdlianjia.csv')
# 获取所属区
areas = list(Date.groupby('所属区').size().index)
#每个区房租平均价钱
area_mean_price=[]
#每个区房屋平均面积
area_mean_house_area=[]
#每个区平均每平米房租价钱
area_mean_perhouseareaprice=[]
for area in areas:
    #获取当前区数据
    area_Data=Date.loc[Date['所属区']==area]
    #取出当前区所有房租数据
    price_=area_Data['价钱']
    #存取当前区房租的集合
    price_num_total=[]
    #存取当前区房租总价
    price_num_all=0
    for price in price_:
        price_num=re.sub("\D", "", price)
        price_num=int(price_num)
        if price_num<100000:#剔除反常数据
            price_num_total.append(price_num)
    for i in range(len(price_num_total)):
        price_num_all=price_num_all+price_num_total[i]
    #当前区房租平均价钱
    price_mean=price_num_all/len(price_num_total)
    #存入房租平均价钱
    area_mean_price.append(price_mean)
    #取出当前区所有房屋面积数据
    house_area_=area_Data['面积']
    #存放当前区房屋面积的集合
    house_area_total=[]
    #存放当前区房屋总面积
    house_area_all=0
    for housearea in house_area_:
        housearea_num=re.sub("\D", "", housearea)
        if housearea_num!='':
            housearea_num=int(housearea_num)
            if housearea_num<1000:#剔除异常数据
                house_area_total.append(housearea_num)
    for i in range(len(house_area_total)):
        house_area_all=house_area_all+house_area_total[i]
    #计算房钱区房屋平均面积
    house_area_mean=house_area_all/len(house_area_total)
    #存入
    area_mean_house_area.append(house_area_mean)
print(area_mean_price)
#第一张图
x = np.arange(len(areas))
width = 0.3
fig,ax = plt.subplots()
# plt.figure(figsize=(20,20))
# ax.bar(x,area_mean_price,width,alpha = 0.8)
plt.xticks(rotation=45)
ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(areas)#将横坐标替换成
plt.xlabel('区')
plt.ylabel('每月平均房租')
x = range(len(area_mean_price))
rects1 = plt.bar(x=x, height=area_mean_price, width=0.3, alpha=0.8)
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(int(height)), ha="center", va="bottom")
plt.show()
#第二张图
print(area_mean_house_area)
x = np.arange(len(areas))
width = 0.2
fig,ax = plt.subplots()
# ax.bar(x,area_mean_house_area,width,alpha = 0.8)
plt.xticks(rotation=45)
ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(areas)#将横坐标替换成
plt.xlabel('区')
plt.ylabel('租房的平均面积')
x = range(len(area_mean_house_area))
rects1 = plt.bar(x=x, height=area_mean_house_area, width=0.3, alpha=0.8)
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(int(height)), ha="center", va="bottom")
plt.show()
for area in areas:
    #获取当前区数据
    area_Data=Date.loc[Date['所属区']==area]
    #取出当前区所有房租数据
    price_=area_Data['价钱']
    # 取出当前区所有房屋面积数据
    house_area_ = area_Data['面积']
    #存放当前区平均每平米房租价钱
    area_mean_perhouseareaprice_=[]
    #存放当前区每平米房租总价钱
    area_mean_perhouseareaprice_all=0
    for price,housearea in zip(price_,house_area_):
        price_num=re.sub("\D", "", price)
        housearea_num = re.sub("\D", "", housearea)
        if housearea_num != '':
            housearea_num = int(housearea_num)
            price_num=int(price_num)
            if price_num<100000 and housearea_num<1000:
                area_mean_perhouseareaprice_.append(price_num/housearea_num)
    for i in range(len(area_mean_perhouseareaprice_)):
        area_mean_perhouseareaprice_all=area_mean_perhouseareaprice_all+area_mean_perhouseareaprice_[i]

    #计算
    area_mean_perhouseareaprice_mean=area_mean_perhouseareaprice_all/len(area_mean_perhouseareaprice_)
    #存入
    area_mean_perhouseareaprice.append(area_mean_perhouseareaprice_mean)
print(area_mean_perhouseareaprice)
print(area_mean_perhouseareaprice)
x = np.arange(len(areas))
width = 0.2
fig,ax = plt.subplots()
# ax.bar(x,area_mean_perhouseareaprice,width,alpha = 0.8)
plt.xticks(rotation=45)
ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(areas)#将横坐标替换成
plt.xlabel('区')
plt.ylabel('每月租房每平米平均价钱')
x = range(len(area_mean_perhouseareaprice))
rects1 = plt.bar(x=x, height=area_mean_perhouseareaprice, width=0.3, alpha=0.8)
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(int(height)), ha="center", va="bottom")
plt.show()