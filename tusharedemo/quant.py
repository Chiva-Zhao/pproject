import talib
import numpy as np
import math
import pandas
import time
import datetime
from functools import reduce


# init方法是您的初始化逻辑。context对象可以在任何方法之间传递。
def init(context):
    context.stock = "000001.SZ"
    context.buy = True
    context.backdays = 100
    logger.info("init universe for %s" % context.stock)
    # 加入池
    set_universe([context.stock])


# 日或分钟或实时数据更新，将会调用这个方法
def handle_data(context, data_dict):
    high_prices = get_history(context.backdays, '1d', 'high')[context.stock].values
    low_prices = get_history(context.backdays, '1d', 'low')[context.stock].values
    open_prices = get_history(context.backdays, '1d', 'open')[context.stock].values
    close_prices = get_history(context.backdays, '1d', 'close')[context.stock].values  # 获取100天的收盘价格
    volume_prices = get_history(context.backdays, '1d', 'volume')[context.stock].values

    kValue, dValue, jValue = get_KDJ(high_prices, low_prices, close_prices, 9, 3, 3)  # 获取kdj三条线的数值
    print(kValue, dValue, jValue)

    if context.buy:
        order_target_percent(context.stock, 1)
        context.buy = False


# 技术指标SMA函数
def get_SMA(close, timeperiod):
    close = np.nan_to_num(close)
    return reduce(lambda x, y: ((timeperiod - 1) * x + y) / timeperiod, close)


# 技术指标的KDJ函数
def get_KDJ(high, low, close, fastk_period, slowk_period, fastd_period):
    kValue, dValue = talib.STOCHF(high, low, close, fastk_period, fastd_period=1, fastd_matype=0)
    kValue = np.array(list(map(lambda x: get_SMA(kValue[:x], slowk_period), range(1, len(kValue) + 1))))
    dValue = np.array(list(map(lambda x: get_SMA(kValue[:x], fastd_period), range(1, len(kValue) + 1))))
    jValue = 3 * kValue - 2 * dValue
    func = lambda arr: np.array([0 if x < 0 else (100 if x > 100 else x) for x in arr])
    kValue = func(kValue)
    dValue = func(dValue)
    jValue = func(jValue)
    return kValue, dValue, jValue

    # talib定义的KDJ计算函数
    # 设定k、d平滑因子a、b，一般约定俗成固定为1/3,high,low,close 一般为60天
    # K1为前一日k值,D1为前一日D值,K2为当日k值,D2为当日D值,J为当日J值
    # 案例K1,D1,K2,D2,J2 = KDJ(1.0/3, 1.0/