import tushare as ts

print(ts.__author__, ts.__version__)
df = ts.get_k_data('002743')
df_5 = ts.get_k_data('600000', ktype='5')
print(df_5)
