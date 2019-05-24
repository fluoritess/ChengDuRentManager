#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin
url = 'http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000'


page = 1

reg1 = re.compile('<[^>]+>')
'''
response = requests.get(url.format(page=page))
html = BeautifulSoup(response.text)
print(html)
house_info = html.select('.list')
print(house_info)
reg1 = re.compile("<[^>]*>")
#content = reg1.sub('',soup.prettify())
#strb = re.compile('<b>'|'</b>')


for house in house_info:
    house_money = str(house.select('h2')[0])
    house_money = reg1.sub('',house_money)
    print(house_money)\
'''


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
        house.select('h2')[0].string.encode('utf-8').split()
        print(house_title)
        #reg2.sub('',house_title)
        house_url = urljoin(url,house.select('a')[0]['href'])
        house_info_list = str(house.select('h2')[0]).split()
        '''
        print(house.select('h2')[0])
        print(urljoin(url,house.select('a')[0]['href']))
        print(house_info_list)
        '''

      
        
        # 如果第二列是公寓名则取第一列作为地址
        #print(house_info)
        '''
        if '公寓' in house_info or '青年社区' in house_info:
            house_location = str(house_info_list[0])
        else:
            house_location = str(house_info_list[1])
        '''
        house_location =  house_info_list[2]
        print(str(house_location))
        house_money = str(house.select('.money')[0].select('b')[0])
        house_money = reg1.sub('',house_money)
    