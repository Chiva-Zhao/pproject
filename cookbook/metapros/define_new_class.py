# 以编程方式定义类
# 你在写一段代码，最终需要创建一个新的类对象。你考虑将类的定义源代码以字符
# 串的形式发布出去。并且使用函数比如 exec() 来执行它，但是你想寻找一个更加优雅
# 的解决方案。
# 你可以使用函数 types.new class() 来初始化新的类对象。你需要做的只是提供
# 类的名字、父类元组、关键字参数，以及一个用成员变量填充类字典的回调函数。例如：
# stock.py
# Example of making a class manually from parts
# Methods
import collections


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}
# Make a class
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
# 这种方式会构建一个普通的类对象，并且按照你的期望工作：
s = Stock('ACME', 50, 91.1)
print(s, s.price, s.cost())
# 这 种 方 法 中， 一 个 比 较 难 理 解 的 地 方 是 在 调 用 完 types.new class() 对
# Stock. module 的赋值。每次当一个类被定义后，它的 module 属性包含定义
# 它的模块名。这个名字用于生成 repr () 方法的输出。它同样也被用于很多库，比如 pickle 。
# 因此，为了让你创建的类是“正确”的，你需要确保这个属性也设置正确了。
# 如果你想创建的类需要一个不同的元类，可以通过 types.new class() 第三个参
# 数传递给它。例如：
import abc

Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
print(Stock)
print(type(Stock))
# 第三个参数还可以包含其他的关键字参数。比如，一个类的定义如下：
# class Spam(Base, debug=True, typecheck=False):
#     pass
# 那么可以将其翻译成如下的 new class() 调用形式：
# Spam = types.new_class('Spam', (Base,),{'debug': True, 'typecheck': False},
# lambda ns: ns.update(cls_dict))
# new class() 第四个参数最神秘，它是一个用来接受类命名空间的映射对象的函
# 数。通常这是一个普通的字典，但是它实际上是 prepare () 方法返回的任意对象，
# 这个函数需要使用上面演示的 update() 方法给命名空间增加内容。
# 很 多 时 候 如 果 能 构 造 新 的 类 对 象 是 很 有 用 的。 有 个 很 熟 悉 的 例 子 是 调 用
# collections.namedtuple() 函数，例如：
Stock = collections.namedtuple('Stock', ['name', 'shares', 'price'])
print(Stock)
# namedtuple() 使用 exec() 而不是上面介绍的技术。但是，下面通过一个简单的变
# 化，我们直接创建一个类：
