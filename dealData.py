#处理数据
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import re
import csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from lxml import etree
import time
csv_file = open("completed.csv", "w", newline='')
csv_writer = csv.writer(csv_file, delimiter=',')
mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
Date = pd.read_csv('csv/cdlianjia.csv')
csv_writer.writerow(['价钱', '面积', '所属区'])
area_ditc={'锦江区':1,'青阳区':2,'武侯区':3,'高新区':4,'成华区':5,'金牛区':6,'天府新区':7,'高新西区':8,'双流区':9,'龙泉驿区':10,'新都区':11}
house_area_=Date['面积']
price_l_=Date['价钱']
price_list=[]
house_area_list=[]
area_list=[]
for house_area in house_area_:
    housearea_num = re.sub("\D", "", house_area)
    if housearea_num != '':
        housearea_num = int(housearea_num)
        if housearea_num > 1000 or housearea_num < 10:  # 剔除异常数据
            # print(len(Date))
            Date = Date[~Date['面积'].isin([house_area])]
    elif housearea_num == '':
        Date = Date[~Date['面积'].isin([house_area])]
for price in price_l_:
            price_num = re.sub("\D", "", price)
            price_num = int(price_num)
            if price_num > 30000 or price_num < 100:  # 剔除反常数据
                # print(len(Date))
                Date = Date[~Date['价钱'].isin([price])]

house_area_ = Date['面积']
price_l_ = Date['价钱']
area_=Date['所属区']
for price in price_l_:
    # string = "www.gziscas.com.cn"
    # print(string.split('.',2)[1])
    price=price.split('/',1)[0]
    price=price.split(' ',1)[0]
    price=int(price)
    price_list.append(price)
for house_area in house_area_:
    housearea_num = re.sub("\D", "", house_area)
    housearea_num = int(housearea_num)
    house_area_list.append(housearea_num)
for area in area_:
    area_num=area_ditc[area]
    area_list.append(area_num)

for i in range(len(price_list)):
    price=price_list[i]
    house_area=house_area_list[i]
    area=area_list[i]
    csv_writer.writerow([price, house_area,area])

