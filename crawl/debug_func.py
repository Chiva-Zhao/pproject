# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv


def myfunc() -> None:
    with open("cyb06.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
        csvwriter = csv.writer(datacsv, dialect=("excel"))
        for i in range(1):
            url = 'http://www.cyzone.cn/company/list-0-' + str(i) + '-4/'
            html = requests.get(url)
            html.encoding = 'utf-8'
            soup = BeautifulSoup(html.text, "html.parser")
            for xxyy in soup.find_all('td', class_='table-company2-tit'):

                dd = xxyy.find_all('a')[0]['href']
                url = dd
                html = requests.get(url)
                html.encoding = 'utf-8'
                soup = BeautifulSoup(html.text, "html.parser")
                for xxyy in soup.find_all('ul', class_='clearfix'):
                    for xy in xxyy.find_all('p', class_='name'):
                        cc = xy.find_all('a')[0]['href']
                        url1 = cc
                        html = requests.get(url1)
                        html.encoding = 'utf-8'
                        soup = BeautifulSoup(html.text, "html.parser")
                        for xxyys in soup.find_all('div', class_='top-info clearfix top-info-vpeople'):
                            for xxyy in xxyys.find_all('div', class_='ti-left pull-left'):
                                for xm in xxyy.find_all('ul'):
                                    a = xm.find_all('li')[0].get_text()
                                    b = xm.find_all('li')[1].get_text()
                                    c = xm.find_all('li')[2].get_text()
                        for tzfw in soup.find_all('div', class_='invest'):
                            try:
                                d = tzfw.find_all('div')[0].get_text().split("\n")
                                e = tzfw.find_all('div')[1].get_text().split("\n")
                                f = tzfw.find_all('div')[2].get_text().split("\n")
                                h = tzfw.find_all('div')[3].get_text().split("\n")
                            except:
                                d = ''
                                e = ''
                                f = ''
                                h = ''
                            if d == '' or e == '' or f == '' or h == '':
                                continue
                        for rwjj in soup.find_all('div', class_='people-info-box'):
                            try:
                                z = rwjj.get_text()
                            except:
                                z = ''
                            if z == '':
                                continue
                        for sjjl in soup.find_all('div', class_='rbr-all'):
                            for sjj in sjjl.find_all('div', class_='info'):
                                try:
                                    x = sjj.find_all('span')[0].get_text()
                                    y = sjj.find_all('span')[1].get_text()
                                except:
                                    x = ''
                                    y = ''
                                if x == '' or y == '':
                                    continue
                        for sl in sjjl.find_all('div', class_='time'):
                            try:
                                s = sl.get_text().strip()
                            except:
                                s = ''
                            if s == '':
                                continue
                        print('写入' + str(i) + a, b, c, d, e, y, z)
                        csvwriter.writerow([a, b, c, d, e, y, z])


if (__name__ == '__main__'):
    myfunc()
