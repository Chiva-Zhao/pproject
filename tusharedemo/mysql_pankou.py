import tushare as ts
from math import isnan
import pymysql.cursors
import pymysql
import csv
# datacsv = open("pk2.csv", "w+", newline="\n", encoding="utf-8")
# csvwriter = csv.writer(datacsv, dialect=("excel"))
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='zzh',
                             password='zzh',
                             db='pydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def pankou(name):
    # rang =pd.date_range('20150101', periods=5)
    # a = ts.get_tick_data(code, rang)
    a = ts.get_tick_data(name, date='2017-03-09')
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
    except Exception as e:
        print('***** Logging failed with this error:', str(e))
    # finally:
    #     connection.close()


if __name__ == '__main__':
    #df = ts.get_today_all()
    #df1 = df['code']
    list1 = ['000001','000002','000003']
    for a in list1:
        pankou(a)