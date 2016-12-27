import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib.request

url = 'http://www.chuangyepu.com/startups/9280.html'
html = requests.get(url)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, "html.parser")
for xx in soup.find_all('ul', class_='base_info'):
    a = xx.find_all('li')[0].get_text()
    b = xx.find_all('li')[1].get_text()
    c = xx.find_all('li')[2].get_text()
    d = xx.find_all('li')[3].get_text()
for yy in soup.find_all('ul', class_='invest-history-list'):
    for qq in yy.find_all('li'):
        e = qq.find_all('div')[0].get_text()
        f = qq.find_all('div')[1]
        for nm in f.find_all('span', class_='round'):
            y = nm.get_text()
        for nn in f.find_all('span', class_='number'):
            s = nn.get_text()
        w = ''
        for mm in f.find('p').find_all(['a','span']):
            w += mm.get_text() + ','
        print(a, b, c, d, e, y, s, w)
