import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://rong.36kr.com/organization/list/")
bsobj = BeautifulSoup(html, "html5lib")
print (bsobj.prettify())
table = bsobj.findAll("div", {"class": "table-body"})
rows = table.findAll("div", {"class": "table-row ng-scope"})

csv = open("../files/editors.csv", 'wt', newline='', enconding='utf-8')
writer = csv.writer(csv)
try:
    for row in rows:
        csv = []
        for cell in row.findAll(['div']):
            row.append(cell.get_text())
        writer.writerow(row)
finally:
    csv.close()
