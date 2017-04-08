# 打印输出至文件中
# 在 print() 函数中指定 file 关键字参数
with open('somefile.txt', 'wt') as f:
    print('Hello World!', file=f)

# 使用其他分隔符或行终止符打印
# 可以使用在 print() 函数中使用 sep 和 end 关键字参数
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')
# 使用 end 参数也可以在输出中禁止换行
for i in range(5):
    print(i)
for i in range(5):
    print(i, end=' ')
print(','.join(('ACME', '50', '91.5')))
# str.join() 的问题在于它仅仅适用于字符串。这意味着你通常需要执行另外一些
# 转换才能让它正常工作
row = ('ACME', 50, 91.5)
print(','.join(str(r) for r in row))
# 你当然可以不用那么麻烦，仅仅只需要像下面这样写
print(row, sep=',')
print(*row, sep=',')
