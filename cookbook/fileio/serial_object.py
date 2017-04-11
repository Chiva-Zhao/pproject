# 序列化 Python 对象
# 你需要将一个 Python 对象序列化为一个字节流，以便将它保存到一个文件、存储
# 到数据库或者通过网络传输它。
# 对于序列化最普遍的做法就是使用 pickle 模块。
import pickle

data = [2, 2.34, "hello"]
f = open('somefile', 'wb')
pickle.dump(data, f)
# 为了将一个对象转储为一个字符串，可以使用 pickle.dumps()
s = pickle.dumps(data)
print(s)
# 为了从字节流中恢复一个对象，使用 picle.load() 或 pickle.loads() 函数
# Restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)
print(data)
# Restore from a string
data = pickle.loads(s)
print(data)
# 对于大多数应用程序来讲， dump() 和 load() 函数的使用就是你有效使用 pickle
# 模块所需的全部了。它可适用于绝大部分 Python 数据类型和用户自定义类的对象实
# 例。如果你碰到某个库可以让你在数据库中保存/恢复 Python 对象或者是通过网络传
# 输对象的话，那么很有可能这个库的底层就使用了 pickle 模块

# pickle 是一种 Python 特有的自描述的数据编码。通过自描述，被序列化后的数据
# 包含每个对象开始和结束以及它的类型信息。因此，你无需担心对象记录的定义，它
# 总是能工作。举个例子，如果要处理多个对象，你可以这样做
import pickle

f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('somedata', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
# 你还能序列化函数，类，还有接口，但是结果数据仅仅将它们的名称编码成对应的代码对象
import math
import pickle

print(pickle.dumps(math.cos))
# 千万不要对不信任的数据使用 pickle.load()。
# pickle 在加载时有一个副作用就是它会自动加载相应模块并构造实例对象。
# 但是某个坏人如果知道 pickle 的工作原理，
# 他就可以创建一个恶意的数据导致 Python 执行随意指定的系统命令。
# 因此，一定要保证 pickle 只在相互之间可以认证对方的解析器的内部使用

# 有些类型的对象是不能被序列化的。这些通常是那些依赖外部系统状态的对象，
# 比如打开的文件，网络连接，线程，进程，栈帧等等。用户自定义类可以通过提
# 供 getstate () 和 setstate () 方法来绕过这些限制。如果定义了这两个方法，
# pickle.dump() 就会调用 getstate () 获取序列化的对象。类似的， setstate ()
# 在反序列化时被调用,参考coutdown.py
import countdown

c = countdown.Countdown(30)
# After a few moments
f = open('cstate.p', 'wb')
pickle.dump(c, f)
f.close()
f = open('cstate.p', 'rb')
pickle.load(f)
