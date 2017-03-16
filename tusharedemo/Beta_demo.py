import tushare as ts
import math
import numpy as np
import csv

datacsv = open("bt.csv", "w+", newline="\n", encoding="utf-8")
csvwriter = csv.writer(datacsv, dialect=("excel"))


def yieldOf(close):
    c1 = close[0:-1]
    c2 = close[1:]
    rst = []
    for i in range(len(c1)):
        rst.append(math.log(c2[i] / c1[i]))
    return rst


def computeYield(code, market, date):
    ds = ts.get_k_data(code, date)
    hs300 = ts.get_hist_data(market, date)
    close = ds['close'].values[:len(ds)]
    hs300_close = hs300['close'].values[:len(ds)]
    ri = yieldOf(close)
    rm = yieldOf(hs300_close)
    # print("股票" + code + "收益率", ri)
    # print("市场收益率", rm)
    covi = np.cov(ri, rm)
    print(covi)
    varm = np.var(rm)
    # print("协方差", covi)
    csvwriter.writerow([code, covi[0][1] / varm])


# computeYield("601169", "hs300", '2017-02-01')
stocks = ts.get_today_all()['code']
for stock in stocks:
    computeYield(stock, "hs300", '2017-02-01')
