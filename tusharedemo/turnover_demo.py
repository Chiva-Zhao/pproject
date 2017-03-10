import tushare as ts
import pandas as pd


def yieldOf(close):
    c1 = close[0:-1]
    c2 = close[1:]
    rst = []
    for i in range(len(c1)):
        rst.append((c2 - c1) / c2)
    return rst


def computeYield(code):
    dates = pd.date_range('20150101', periods=5)
    ds = ts.get_hist_data(code)
    if ds is not None:
        close = ds['turnover']
        print(close)


def computeturnover(code):
    dates = pd.date_range('20160101', periods=30)
    for date in dates:
        ds = ts.get_hist_data(code, start=str(date)[0:10], end=str(date)[0:10])
        if ds.size > 0:
            print(code, ds['turnover'])


# computeYield("603311")
if __name__ == '__main__':
    a = ts.get_today_all()
    b = a[a.changepercent > 5]
    stocks = b['code']
    for stock in stocks:
        if stock[0] != '6':
            computeturnover(stock)
