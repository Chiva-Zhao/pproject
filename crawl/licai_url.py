import requests
from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver

with open("gssmzquanbu3.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    fb = open(r'C:\Users\Administrator\Desktop\888.txt')
    alldata = fb.read().split("\n")
    for i in range(len(alldata)):
        data = alldata[i].split("\t")
        a1 = data[0]
        a2 = data[1]
        b1 = data[2]
        print(a1)
