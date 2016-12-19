import requests
from bs4 import BeautifulSoup
import csv
import time

url = 'http://www.cyzone.cn/company/case-9-0-0-1/'
time.sleep(1)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
html = requests.get(url=url, headers=headers)
# htm2 = urllib.request.urlopen(html)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, "html.parser")
for row in soup.find_all('tr', class_='table-plate3'):
    a = row.find('span',class_='tp2_com').get_text()
    b = row.find('div', class_='money').get_text()
    print(a,b)