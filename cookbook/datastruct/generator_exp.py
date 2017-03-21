# 转换并同时计算数据
# 一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数
nums = [1, 2, 4, 9]
# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]


def default():
    print(sum(x * x for x in nums))


def more():
    import os
    files = os.listdir('.')
    if any(name.endswith('.py') for name in files):
        print('There be python!')
    else:
        print('Sorry, no python.')
    # Output a tuple as CSV
    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))
    min_shares = min(s['shares'] for s in portfolio)
    print(min_shares)


more()
# 使用一个生成器表达式作为参数会比先创建一个临时列表更加高效和优雅
# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)
