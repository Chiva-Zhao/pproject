import tushare as ts
import numpy as np
import pandas as pd
import time


def pankou(code):
    # rang =pd.date_range('20150101', periods=5)
    # a = ts.get_tick_data(code, rang)
    a = ts.get_tick_data(code, date='2017-03-09')
    buy_sum = 0
    sell_sum = 0
    other_sum = 0
    for item in range(0, len(a)):
        row = a[item:item + 1]
        type = row['type']
        if type[item] == '卖盘':
            sell_sum += row['amount'][item]
        elif type[item] == '买盘':
            buy_sum += row['amount'][item]
        else:
            other_sum += row['amount'][item]
    pan_sum = sum([sell_sum, buy_sum, other_sum])
    print('股票', code, (sell_sum, buy_sum, other_sum) / pan_sum)

    # pankou('600848')


if __name__ == '__main__':
    df = ts.get_today_all()
    b = df[df.changepercent > 5]
    stocks = b['code']
    for stock in stocks:
        pankou(stock)


