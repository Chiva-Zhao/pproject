start = '2012-05-28'  # 回测开始时间
end = '2016-08-08'  # 回测结束时间
secID = '601318.XSHG'  # 中国平安

benchmark = secID  # 策略对标标的
universe = [secID]  # 证券池，支持股票和基金                # 证券池，支持股票和基金
capital_base = 100000  # 起始资金
freq = 'd'  # 策略类型，'d'表示日间策略使用日线回测，'m'表示日内策略使用分钟线回测
refresh_rate = 1  # 调仓频率，表示执行handle_data的时间间隔，若freq = 'd'时间间隔的单位为交易日，若freq = 'm'时间间隔为分钟
period1 = 5
period2 = 60
commission = Commission(buycost=0.0003, sellcost=0.0013, unit='perValue')
max_history_window = 100  # 设定调取历史价格区间最大为100个交易日


def initialize(account):  # 初始化虚拟账户状态
    pass


def handle_data(account):  # 每个交易日的买入卖出指令
    hist1 = account.get_attribute_history('closePrice', period1)  # 获取过去5个交易日的收盘价
    hist2 = account.get_attribute_history('closePrice', period2)  # 获取过去60个交易日的收盘价
    for s in account.universe:
        MA5 = hist1[s].mean()  # 计算过去5个交易日及过去60个交易日的均价
        MA60 = hist2[s].mean()

        if MA5 > MA60 and s not in account.security_position:  # “金叉”时买入
            amount = int(account.cash / account.referencePrice[s] / 100) * 100
            order(s, amount)
        elif MA5 < MA60 and s in account.security_position:  # “死叉”时卖出
            order_to(s, 0)
