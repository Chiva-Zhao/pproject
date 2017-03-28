from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

url = 'https://simu.howbuy.com/manager/92002249.html'
# time.sleep(1)
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
html = requests.get(url=url)
# htm2 = urllib.request.urlopen(html)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, "html.parser")
time.sleep(3)
xxyy = soup.find('div', class_='manager_info_right fl')
for xy in xxyy.find_all('li', class_="info_item"):
    if xy.find_all('a', class_="c"):
        a1 = xy.find_all('a', class_="c")[0].get_text()
        print(a1)

    # a1 = xxyy.find_all('a',class_="c")
