import tushare as ts
from webapp.DBUtils import UseDatabase
from math import isnan
# datacsv = open("pk2.csv", "w+", newline="\n", encoding="utf-8")
# csvwriter = csv.writer(datacsv, dialect=("excel"))
config = {'host': '127.0.0.1',
          'user': 'zzh',
          'password': 'zzh',
          'database': 'pydb', }


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
    with UseDatabase(config) as cursor:
        _SQL = """insert into pankou
        (name, mp, sp, zx)
        values
        (%s, %s, %s, %s)"""
        cursor.execute(_SQL, (name, mp, sp, zx))
        # csvwriter.writerow([str(name), mp, sp, zx])
        # pankou('600848')


if __name__ == '__main__':
    fb = open(r'gupiao.txt')
    alldata = fb.read().split("\n")
    for i in range(len(alldata)):
        pankou(alldata[i])
