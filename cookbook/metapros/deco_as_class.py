# 将装饰器定义为类
# 你想使用一个装饰器去包装函数，但是希望返回一个可调用的实例。你需要让你的
# 装饰器可以同时工作在类定义的内部和外部。
# 为了将装饰器定义成一个实例，你需要确保它实现了 call () 和 get () 方法。
# 例如，下面的代码定义了一个类，它在其他函数上放置一个简单的记录层：
import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


# 你可以将它当做一个普通的装饰器来使用，在类里面或外面都可以：
@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


print(add(2, 3))
print(add(4, 5))
print(add.ncalls)
s = Spam()
s.bar(2)
s.bar(3)
s.bar(4)
print(s.bar.ncalls)


# 将装饰器定义成类通常是很简单的。但是这里还是有一些细节需要解释下，特别是
# 当你想将它作用在实例方法上的时候。
# 首先，使用 functools.wraps() 函数的作用跟之前还是一样，将被包装函数的元
# 信息复制到可调用实例中去。
# 其次，通常很容易会忽视上面的 get () 方法。如果你忽略它，保持其他代码不
# 变再次运行，你会发现当你去调用被装饰实例方法时出现很奇怪的问题。例如：
# >>> s = Spam()
# >>> s.bar(3)
# Traceback (most recent call last):
# ...
# TypeError: bar() missing 1 required positional argument: 'x'
# 出错原因是当方法函数在一个类中被查找时，它们的 get () 方法依据描述器协
# 议被调用。在这里， get () 的目的是创建一
# 个绑定方法对象 (最终会给这个方法传递 self 参数)。下面是一个例子来演示底层原理：
# >>> s = Spam()
# >>> def grok(self, x):
# ... pass
# ...
# >>> grok.__get__(s, Spam)
# <bound method Spam.grok of <__main__.Spam object at 0x100671e90>>
def grok(self, x):
    pass


print(grok.__get__(s, Spam))


# get () 方法是为了确保绑定方法对象能被正确的创建。 type.MethodType() 手
# 动创建一个绑定方法来使用。只有当实例被使用的时候绑定方法才会被创建。如果这
# 个方法是在类上面来访问，那么 get () 中的 instance 参数会被设置成 None 并直接
# 返回 Profiled 实例本身。这样的话我们就可以提取它的 ncalls 属性了。
# 如果你想避免一些混乱，也可以考虑另外一个使用闭包和 nonlocal 变量实现的装饰器,例如：
def profiled(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)

    wrapper.ncalls = lambda: ncalls
    return wrapper


# Example
@profiled
def add(x, y):
    return x + y
# 这个方式跟之前的效果几乎一样，除了对于 ncalls 的访问现在是通过一个被绑定
# 为属性的函数来实现
add(2,3)
add(5,6)
print(add.ncalls())