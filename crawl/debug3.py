import requests
from bs4 import BeautifulSoup
import csv

with open("cyb2.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    for i in range(2):
        url = 'http://www.cyzone.cn/event/list-764-0-' + str(i) + '-0-0-0-0/'
        html = requests.get(url)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, "html.parser")
        for row in soup.find_all('tr', class_="table-plate3"):
            a = row.find_all('span', class_="tp2_com")[0].get_text()
            b = row.find_all('div', class_="money")[0].get_text()
            print('写入' + str(i) + a, b)
