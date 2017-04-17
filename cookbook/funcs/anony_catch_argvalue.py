# 匿名函数捕获变量值
# 你用 lambda 定义了一个匿名函数，并想在定义时捕获到某些变量的值
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10), b(10))  # 30 30 not 20 30
# 这其中的奥妙在于 lambda 表达式中的 x 是一个自由变量，在运行时绑定值，而不
# 是定义时就绑定，这跟函数的默认值参数定义是不同的。因此，在调用这个 lambda 表
# 达式的时候， x 的值是执行时的值
x = 15
print(a(10))
x = 3
print(a(10))
# 如果你想让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10), b(10))
# 在这里列出来的问题是新手很容易犯的错误，有些新手可能会不恰当的使用
# lambda 表达式。比如，通过在一个循环或列表推导中创建一个 lambda 表达式列
# 表，并期望函数能在定义时就记住每次的迭代值
funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))
# 但是实际效果是运行时n 的值为迭代的最后一个值。现在我们用另一种方式修改一下
funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print(f(0))
# 通过使用函数默认值参数形式， lambda 函数在定义时就能绑定到值