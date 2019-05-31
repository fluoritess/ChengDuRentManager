from scipy.stats import pearsonr
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import re
mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
Date = pd.read_csv('cdlianjia2.csv')
name_Date=Date['房源名称']
layout_Date=Date['户型']
direction_Date=Date['面向']
houserarea_Date=Date['面积']
area_Date=Date['所属区']
address_Date=Date['地址']
price_Date=Date['价钱']

print(pearsonr(houserarea_Date,price_Date))
# x = [0.5, 0.4, 0.6, 0.3, 0.6, 0.2, 0.7, 0.5]
# y = [0.6, 0.4, 0.4, 0.3, 0.7, 0.2, 0.5, 0.6]
# print(pearsonr(x, y))

