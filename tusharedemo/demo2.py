import tushare as ts
import numpy as np

a = ts.get_tick_data('600848', date='2014-01-09')
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
pan_sum = sum([sell_sum,buy_sum,other_sum])
print((sell_sum, buy_sum, other_sum)/pan_sum)
