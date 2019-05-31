#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import time
import re
url = 'http://cd.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000'

#已完成的 页数序号，初始为0
page = 0

csv_file = open("rent.csv","w",newline='') 
csv_writer = csv.writer(csv_file,delimiter=',')

#去掉所有的html标签
reg1 = re.compile("<[^>]*>")
reg2 = re.compile('</?w+[^>]*>')
while True:
    page += 1
    print('fetch:',url.format(page=page))
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text,"lxml")
    html.prettify()
    #print(html)
    house_list = html.select('.list > li')
    #print(house_list)
    # 循环在读不到新的房源时结束
    if not house_list:
        break

    for house in house_list:
        house_title = str(house.select('h2')[0])
        house_title = house_title.replace('<h2>','')
        house_title = house_title.replace('</h2>','')
        print(house_title)
        #reg2.sub('',house_title)
        print(house_title)
        house_url = urljoin(url,house.select('a')[0]['href'])
        house_info_list = house_title.split()
        '''
        print(house.select('h2')[0])
        print(urljoin(url,house.select('a')[0]['href']))
        print(house_info_list)
        '''

      
        
        # 如果第二列是公寓名则取第一列作为地址
        house_info = str(house_info_list[1])
        print(house_info)
        if '公寓' in house_info or '青年社区' in house_info:
            house_location = str(house_info_list[0])
        else:
            house_location = str(house_info_list[1])
        print(house_location)
        house_money = str(house.select('.money')[0].select('b')[0])
        house_money = reg1.sub('',house_money)
        #print(type(house_title),type(house_location),type(house_money),type(house_url))
        csv_writer.writerow([house_title,house_location,house_money,house_url])
        if page % 60 == 0:
            time.sleep(3)
csv_file.close()