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

# url = 'http://www.chuangyepu.com/institutions/2819.html'
# html = requests.get(url)
# soup = BeautifulSoup(html.text,'html.parser')
# for name in soup.find_all("ul", class_="tag tag_industry"):
# #for name in soup.select('.tag tag_industry'):
#     str = ''
#     for nam in name.select('li'):
#         str +=nam.get_text()+','
#     print(str)

# with open("testjr.csv", "w+", newline="\n",encoding="utf-8") as datacsv:
#     csvwriter = csv.writer(datacsv, dialect=("excel"))
#     for i in range(2):
#         url = 'http://www.chuangyepu.com/investments?page=2'
#         html = requests.get(url)
#         html.encoding = 'utf-8'
#         soup = BeautifulSoup(html.text, "html.parser")
#         #for tzsjs in soup.find_all('td',class_='startup-item'):
#         for tzsjs in soup.find_all('tr'):
#             for tzsj in tzsjs.find_all('td'):
#                 a = tzsjs.find_all('td')[0].get_text()
#                 b = tzsjs.find_all('td')[1].get_text()
#                 csvwriter.writerow([(a),(b)])

with open("testjj116.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    for i in range(2):
        url = 'http://www.cyzone.cn/company/list-0-' + str(i) + '-0/'
        html = requests.get(url)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, "html.parser")
        for name in soup.select('.table-plate2'):
            a = name.select('a')[0]['href']
            url1 = a
            htm2 = requests.get(url1)
            htm2.encoding = 'utf-8'
            soup = BeautifulSoup(htm2.text, "html.parser")
            for name in soup.find_all('div', class_='ti-left pull-left'):
                for nam in name.find_all('ul'):
                    for na in nam.find_all('li'):
                        try:
                            b = nam.find_all('li')[0].get_text()
                            c = nam.find_all('li')[1].get_text()
                        except:
                            b = ''
                            c = ''
                        print('写入b' + b)
                        print('写入c' + c)
                        csvwriter.writerow([b, c])
