# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:34:03 2016

@author: wangjing
"""

import requests
from bs4 import BeautifulSoup
import csv

with open("rw2.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))

    for i in range(2):
        url = 'http://www.cyzone.cn/vpeople/list-0-' + str(i) + '/'
        html = requests.get(url)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, "html.parser")
        for names in soup.find_all('td', class_='people-name'):

            try:
                a = names.find_all('a')[0]['href']
                if url == a:
                    continue
            except:
                a = ''
            if a == '':
                continue
            url = a
            html = requests.get(url)
            html.encoding = 'utf-8'
            soup = BeautifulSoup(html.text, "html.parser")
            for names in soup.find_all('li', class_='name'):

                try:

                    # for nam in name.soup.select('td'):
                    b = names.get_text()
                except:
                    b = ''
            for names in soup.find_all('div', class_='tl-img'):

                try:
                    c = names.find_all('img')[0]['src']
                except:
                    c = ''

                print('写入' + b, c)
                csvwriter.writerow([b, c])
