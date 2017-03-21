import tushare as ts
from math import isnan
import pymysql.cursors
import pandas as pd

# datacsv = open("pk2.csv", "w+", newline="\n", encoding="utf-8")
# csvwriter = csv.writer(datacsv, dialect=("excel"))
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='zzh',
                             password='zzh',
                             db='pydb',
                             charset='utf8mb4')


def pankou(name, date):
    # rang =pd.date_range('20150101', periods=5)
    # a = ts.get_tick_data(code, rang)
    a = ts.get_tick_data(name, date)
    buy_sum = 0
    sell_sum = 0
    other_sum = 0
    if len(a) == 0:
        return
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
    mp = buy_sum / pan_sum
    sp = sell_sum / pan_sum
    zx = other_sum / pan_sum
    # print('股票',code,(sell_sum, buy_sum, other_sum)/pan_sum)
    print('股票', name, mp, sp, zx)
    if isnan(mp):
        return
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            _SQL = """insert into pankou
                (name, mp, sp, zx)
                values
                (%r, %.2f, %.2f, %.2f)"""
            cursor.execute(_SQL % (name, mp, sp, zx))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
    finally:
        connection.close();


if __name__ == '__main__':
    range = pd.date_range(start='20150101', end='20150103', freq='B')
    for date in range:
        pankou('000001', date)
