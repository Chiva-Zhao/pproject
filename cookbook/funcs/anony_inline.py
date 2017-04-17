# 定义匿名或内联函数
# 当一些函数很简单，仅仅只是计算一个表达式的值的时候，就可以使用 lambda 表达式来代替了
add = lambda x, y: x + y
print(add(2, 3))
print(add('hello', 'world'))
# lambda 表达式典型的使用场景是排序或数据 reduce 等
names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))
# 尽管 lambda 表达式允许你定义简单函数，但是它的使用是有限制的。你只能指定
# 单个表达式，它的值就是最后的返回值。也就是说不能包含其他的语言特性了，包括
# 多个语句、条件表达式、迭代以及异常处理等等。
# 你可以不使用 lambda 表达式就能编写大部分 python 代码。但是，当有人编写大
# 量计算表达式值的短小函数或者需要用户提供回调函数的程序的时候，你就会看到
# lambda 表达式的身影了
