# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import time
import re
import string

csv_file = open("cdlianjia2.csv", "w", newline='')
csv_writer = csv.writer(csv_file, delimiter=',')

list=["jinjiang","qingyang","wuhou","gaoxin7","chenghua","jinniu","tianfuxinqu","gaoxinxi1","shuangliu","longquanyi","xindou"]

# 去掉所有的html标签
reg1 = re.compile("<[^>]*>")
reg2 = re.compile('</?w+[^>]*>')
def getdata():
    for q in range(len(list)):
        url = 'https://cd.lianjia.com/zufang/'
        url += list[q] + "/pg"
        for y in range(100):
            len_str=len(url)
            if y>0:
                url=url[0:len_str-1]
            yeshu = str(y+1)
            url+=yeshu
            headers={
            #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400"
             }
            # url = 'https://cd.lianjia.com/zufang/jinjiang/pg1'
            response=requests.get(url,headers=headers)#,headers=headers#
            response.encoding=response.apparent_encoding
            p=[]
            soup=BeautifulSoup(response.text,'html.parser')# BeautifulSoup解析
            # text = soup.find("span",attrs={"class","content__list--item-price"})
            # print(text)
            totaldivlist=soup.find_all("div", attrs={"class","content__list--item"})#
            lenth=len(totaldivlist)
            for i in range(lenth):
                price_span=totaldivlist[i].find("span",attrs={"class","content__list--item-price"})
                #价钱
                price=price_span.text
                #房源名称和面向和户型
                tital_p = totaldivlist[i].find("p", attrs={"class", "content__list--item--title twoline"})
                a = tital_p.find("a")
                tital=a.text.split()
                #名称
                house_name=tital[0]
                #户型
                house_layout=tital[1]
                #面向
                if len(tital)>2:
                    house_direction=tital[2]
                else:
                    house_direction=''
                #地点
                address_p=totaldivlist[i].find("p", attrs={"class", "content__list--item--des"})
                address_a=address_p.find_all("a")
                #区
                if q==0:
                    area='锦江区'
                elif q==1:
                    area='青阳区'
                elif q==2:
                    area='武侯区'
                elif q==3:
                    area='高新区'
                elif q==4:
                    area='成华区'
                elif q==5:
                    area='金牛区'
                elif q==6:
                    area='天府新区'
                elif q==7:
                    area='高新西区'
                elif q==8:
                    area='双流区'
                elif q==9:
                    area='龙泉驿区'
                elif q==10:
                    area='新都区'
                #具体地点
                address=""
                for i in range(len(address_a)):
                     address+=address_a[i].text
                #房屋面积
                house_area_=address_p.text.split()
                house_area=house_area_[2]
                csv_writer.writerow([house_name, house_layout,house_direction, house_area,area, address,price])
            baibai_x=(y+1)*(101*(q+1))
            baifen_y=101*(101*(len(list)))
            print("爬取进度"+str(baibai_x/baifen_y))
if __name__ == '__main__':
    csv_writer.writerow(["房源名称", "户型", "面向", "面积","所属区","地址","价钱"])
    getdata()
