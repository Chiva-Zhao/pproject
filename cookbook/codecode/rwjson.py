# 读写 JSON 数据
# json 模块提供了一种很简单的方式来编码和解码 JSON 数据。其中两个主要的函
# 数是 json.dumps() 和 json.loads() ，要比其他序列化函数库如 pickle 的接口少得多
import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data)
print(json_str)
data = json.loads(json_str)
print(data)
# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load()
# 来编码和解码 JSON 数据
# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)
# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)
print(json.dumps(False))
d = {'a': True,
     'b': 'Hello',
     'c': None}
print(json.dumps(d))
# 如果你试着去检查 JSON 解码后的数据，你通常很难通过简单的打印来确定它的
# 结构，特别是当数据的嵌套结构层次很深或者包含大量的字段时。为了解决这个问题，
# 可以考虑使用 pprint 模块的 pprint() 函数来代替普通的 print() 函数。它会按照
# key 的字母顺序并以一种更加美观的方式输出。下面是一个演示如何漂亮的打印输出
# Twitter 上搜索结果的例子
from urllib.request import urlopen
from pprint import pprint
from collections import OrderedDict

# u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
# resp = json.loads(u.read().decode('utf-8'))
# pprint(resp)
# 一般来讲， JSON 解码会根据提供的数据创建 dicts 或 lists。如果你想要创建其他
# 类型的对象，可以给 json.loads() 传递 object pairs hook 或 object hook 参数。例如，
# 下面是演示如何解码 JSON 数据并在一个 OrderedDict 中保留其顺序的例子
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)


# 下面是如何将一个 JSON 字典转换为一个 Python 对象例子
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(s, object_hook=JSONObject)
print(data.name, data.shares, data.price)
# 最后一个例子中， JSON 解码后的字典作为一个单个参数传递给 init () 。然
# 后，你就可以随心所欲的使用它了，比如作为一个实例字典来直接使用它。
# 在编码 JSON 的时候，还有一些选项很有用。如果你想获得漂亮的格式化字符串后
# 输出，可以使用 json.dumps() 的 indent 参数。它会使得输出和 pprint() 函数效果类
# 似。比如
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
print(json.dumps(data, indent=4))


# 对象实例通常并不是 JSON 可序列化的。例如：
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)


# json.dumps(p)
# 如果你想序列化对象实例，你可以提供一个函数，它的输入是一个实例，返回一个
# 可序列化的字典
def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


# 如果你想反过来获取这个实例，可以这样做
classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


# 下面是如何使用这些函数的例子：
p = Point(2, 3)
print(vars(p))
s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unserialize_object)
print(a, a.x, a.y)
