import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib.request
from selenium import webdriver
# url = 'http://www.licai.com/pe/renwu-3989.html'
# time.sleep(1)
# html = requests.get(url)
# html.encoding = 'gbk'
# soup = BeautifulSoup(html.text, "html.parser")
# for wz in soup.find_all('div', class_='manager l'):
#     for xx in wz.find_all('h1', class_="jlname"):
#         a = xx.get_text()
#         for xy in wz.find_all('p'):
#           for yy in xy.find_all('a'):
#              b = yy.get_text()
#         print(a,b)

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'D:\\phantomjs211\\bin\\phantomjs.exe')
driver.get('http://www.licai.com/pe/jingli.html')
time.sleep(3)
data = driver.page_source
soup = BeautifulSoup(data, "html.parser")
for wz in soup.find_all('div',class_= 'pelist'):
    for wzs in wz.find_all('tbody'):
        for wzz in wzs.find_all('tr'):
            if len(wzz.find_all('td')) == 0:
                continue
            f = wzz.find_all('td')[1]
            b = f.find('a').attrs['href']
            print(f.get_text(),b)
