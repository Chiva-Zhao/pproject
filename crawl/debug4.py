import requests
from bs4 import BeautifulSoup
import csv
import time

with open("cybsj16.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    for i in range(415, 843):
        url = 'http://www.cyzone.cn/event/list-764-0-' + str(i) + '-0-0-0-0/'
        time.sleep(5)
        html = requests.get(url)
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
                time.sleep(5)
                htm2 = requests.get(url1)
            except ConnectionError:
                print("连接异常：反爬虫")
                continue;
            htm2.encoding = 'utf-8'
            soup = BeautifulSoup(htm2.text, "html.parser")
            for name in soup.find_all('div', class_='ti-left pull-left'):
                for nam in name.find_all('ul'):
                    for na in nam.find_all('li'):
                        try:
                            b = name.find_all('li')[0].get_text()
                        except:
                            b = ''
                        if b == '':
                            continue
            for name in soup.find_all('div', class_='info-tag clearfix'):
                for nam in name.find_all('ul'):
                    for na in nam.find_all('li'):
                        try:
                            c = name.find_all('li')[0].get_text()
                        except:
                            c = ''
                    print('写入' + str(i) + b, c)
                    csvwriter.writerow([b, c])
