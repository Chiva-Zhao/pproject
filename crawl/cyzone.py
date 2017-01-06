import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib.request

with open("sj15.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
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
            for mz in soup.find_all('li', class_='name'):
                a = mz.get_text()
            for mz in soup.find_all('li', class_='time'):
                b = mz.get_text()
            for jj in soup.find_all('div', class_='info-box'):
                z = jj.get_text().strip()
            for mzs in soup.find_all('div', class_='info-tag clearfix'):
                for xy in mzs.find_all('ul'):
                    try:
                        c = xy.find_all('li')[0].get_text()
                        d = xy.find_all('li')[1].get_text()
                        e = xy.find_all('li')[2].get_text()
                        f = xy.find_all('li')[3]
                        y = ''
                        for nm in f.find_all('span'):
                            y += nm.get_text() + ','
                    except:
                        c = ''
                        d = ''
                        e = ''
                        f = ''
                    if c == '' or f == '' or d == '':
                        continue
                print('写入' + str(i) + a, b, c, d, e, y, z)
                csvwriter.writerow([a, b, c, d, e, y, z])
