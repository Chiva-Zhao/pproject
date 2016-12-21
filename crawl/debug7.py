import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib.request

with open("sj6.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    csvwriter.writerow(['a','b','c','d','e'])
    for i in range(257, 258):
        url = 'http://www.cyzone.cn/event/list-764-0-' + str(i) + '-0-0-0-0/'
        time.sleep(1)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        html = requests.get(url=url, headers=headers)
        # htm2 = urllib.request.urlopen(html)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, "html.parser")
        for row in soup.find_all('span', class_="tp2_tit"):
            try:
                a = row.find_all('a')[0]['href']
            except:
                a = ''
            if a == '':
                continue
            url1 = a
            try:
                time.sleep(1)
                htm2 = requests.get(url1)
            except ConnectionError:
                print("连接异常：反爬虫")
                # continue
            htm2.encoding = 'utf-8'
            soup = BeautifulSoup(htm2.text, "html.parser")
            for name in soup.find_all('div', class_='ti-left pull-left'):
                for nam in name.find_all('ul'):
                    for na in nam.find_all('li'):
                        try:
                            b = nam.find_all('li')[0].get_text()
                        except:
                            b = ''
                        if b == '':
                            continue
            try:
                row = soup.find_all('tr', class_='live-title')[0]
                for tr in row.parent.find_all("tr", recursive=False):
                    if (tr.get('class') is not None and (
                                    tr.get('class')[0] == 'live-title' or tr.get('class')[0] == 'active')):
                        continue;
                    td = tr.find_all('td', recursive=False)
                    if (len(td) == 4):
                        c = td[0].getText()
                        try:
                            d = td[1].find_all("div", class_="money")[0].getText()
                        except:
                            d = td[1].getText()
                        e = td[2].getText()
                        f = td[3].getText()
                        print('写入' + str(i) + b, c, d, e, f)
                        csvwriter.writerow([b, c, d, e, f])
            except:
                row = ''
