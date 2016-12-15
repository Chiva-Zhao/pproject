import requests
from bs4 import BeautifulSoup
import time

url = 'http://www.cyzone.cn/r/20160926/44237.html'
time.sleep(0.1)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
html = requests.get(url=url, headers=headers)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, "html.parser")
row = soup.find_all('tr', class_='live-title')[0]
for tr in row.parent.find_all("tr", recursive=False):
    if (tr.get('class') is not None and (tr.get('class')[0] == 'live-title' or tr.get('class')[0] == 'active')):
        continue;
    td = tr.find_all('td', recursive=False)
    if (len(td) == 4):
        print(td[0].getText())
        try:
            print(td[1].find_all("div", class_="money")[0].getText())
        except:
            print(td[1].getText())
        print(td[2].getText())
        print(td[3].getText())
