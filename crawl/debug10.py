import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib.request

url = 'http://www.cyzone.cn/r/20161224/47311.html'
html = requests.get(url)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, "html.parser")
for mz in soup.find_all('li', class_='name'):
    a = mz.get_text()
for mz in soup.find_all('li', class_='time'):
    b = mz.get_text()
for jj in soup.find_all('div', class_='info-box'):
    z = jj.get_text().strip()
for mzs in soup.find_all('div', class_='info-tag clearfix'):
    for xy in mzs.find_all('ul'):
        c = xy.find_all('li')[0].get_text()
        d = xy.find_all('li')[1].get_text()
        e = xy.find_all('li')[2].get_text()
        f = xy.find_all('li')[3]
        w = ''
        for nm in f.find_all('span'):
            w += nm.get_text() + ','
    print(a, b, c, d, e, w, z)
