import requests
from bs4 import BeautifulSoup
import csv

# # csvFile = open('items.csv','w+', newline='',encodinh='utf-8')
# with open("test.csv", "w+", newline="\n",encoding="utf-8") as datacsv:
#     csvwriter = csv.writer(datacsv, dialect=("excel"))
#     for i in range(2):
#         url = 'http://www.chuangyepu.com/institutions?page=' + str(i)
#         html = requests.get(url)
#         html.encoding = 'utf-8'
#         soup = BeautifulSoup(html.text, "html.parser")
#         table = soup.findAll('div', {"class": 'info'})
#         # for i in range(len(table)):
#         # w = table[0]+table[1]+
#         for name in table:
#             print("已写入" + name.get_text())
#             # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
#             csvwriter.writerow([name.get_text()])

url = 'http://www.chuangyepu.com/institutions/2819.html'
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
for name in soup.find_all("ul", class_="tag tag_industry"):
#for name in soup.select('.tag tag_industry'):
    str = ''
    for nam in name.select('li'):
        str +=nam.get_text()+','
    print(str)
