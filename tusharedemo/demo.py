# coding:utf-8
import tushare as ts
from matplotlib.pyplot import plot, xlabel, ylabel, show, rcParams
import matplotlib
rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
print(ts.__author__, ts.__version__)
# df = ts.get_k_data('002743')
df_5 = ts.get_k_data('600000',ktype='D',start='2016-01-01')
# print(df_5['date'],df_5['open'])
dates = df_5['date']
matplotlib.pyplot.plot_date(dates, df_5['open'])
# plot(dates,df_5['open'])
xlabel('日期')
ylabel('开盘价')
show()

