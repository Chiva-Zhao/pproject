# 访问闭包中定义的变量
# 通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。但是，你可以通过编写访
# 问函数并将其作为函数属性绑定到闭包上来实现这个目的。
def sample():
    n = 0

    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


# 下面是使用的例子:
f = sample()
f()
f.set_n(10)
f()
print(f.get_n())
# 为了说明清楚它如何工作的，有两点需要解释一下。首先， nonlocal 声明可以让
# 我们编写函数来修改内部变量的值。其次，函数属性允许我们用一种很简单的方式将
# 访问方法绑定到闭包函数上，这个跟实例方法很像 (尽管并没有定义任何类)。
# 还可以进一步的扩展，让闭包模拟类的实例。你要做的仅仅是复制上面的内部函数
# 到一个字典实例中并返回它即可
import sys


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()


# Example use
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


# 下面是一个交互式会话来演示它是如何工作的：
s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('Hello')
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())


# 有趣的是，这个代码运行起来会比一个普通的类定义要快很多。你可能会像下面这
# 样测试它跟一个类的性能对比
class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


# 如果这样做，你会得到类似如下的结果：
from timeit import timeit

# Test involving closures
s = Stack()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
# Test involving a class
s = Stack2()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
# 结果显示，闭包的方案运行起来要快大概 8%，大部分原因是因为对实例变量的简
# 化访问，闭包更快是因为不会涉及到额外的 self 变量。
# 总体上讲，在配置的时候给闭包添加方法会有更多的实用功能，比如你需要重置内
# 部状态、刷新缓冲区、清除缓存或其他的反馈机制的时候。
