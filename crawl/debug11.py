import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib.request

with open("sj12.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    for i in range(1):
        url = 'http://www.cyzone.cn/event/list-764-0-' + str(i) + '-0-0-0-0/'
        time.sleep(1)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
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
            for row in soup.find_all('div', class_="desc-block"):
                h = row.find_all('a')[1]['href']
                url2 = h
                try:
                    time.sleep(1)
                    htm2 = requests.get(url2)
                except ConnectionError:
                    print("连接异常：反爬虫")
                # continue
                htm2.encoding = 'utf-8'
                soup = BeautifulSoup(htm2.text, "html.parser")
                for xyzz in soup.find_all('div', class_='list-nav-tag clearfix'):
                    for xyz in xyzz.find_all('td', class_='t2-2'):
                        b = xyz.find_all('p')[0].get_text()
                        c = xyz.find_all('p')[1].get_text()
                    for xx in xyzz.find_all('tr', class_='t2'):
                        d = xx.find_all('td')[2].get_text().strip()
                        e = xx.find_all('td')[3].get_text().strip()
                        # z = xx.find_all('td',class_='t2-3').get_text().strip()
                        f = xx.find_all('td')[4]
                        y = f['title']
                    print('写入' + str(i) + b, c, d, e, y)
                    csvwriter.writerow([b, c, d, e, y])
