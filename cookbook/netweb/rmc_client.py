# 为了从一个远程客户端访问服务器，你需要创建一个对应的用来传送请求的 RPC
# 代理类。例如
import pickle


class RPCProxy:
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result

        return do_rpc
# 要使用这个代理类，你需要将其包装到一个服务器的连接上面，例如：
from multiprocessing.connection import Client
c = Client(('localhost', 17000), authkey=b'peekaboo')
proxy = RPCProxy(c)
print(proxy.add(2,3))
print(proxy.sub(2,3))
# print(proxy.sub([1,2],4)) TypeError: unsupported operand type(s) for -: 'list' and 'int
# 要注意的是很多消息层（比如 multiprocessing ）已经使用 pickle 序列化了数据。
# 如果是这样的话，对 pickle.dumps() 和 pickle.loads() 的调用要去掉。
# RPCHandler 和 RPCProxy 的基本思路是很比较简单的。如果一个客户端想要调用
# 一个远程函数，比如 foo(1, 2, z=3) , 代理类创建一个包含了函数名和参数的元组
# ('foo', (1, 2), f'z': 3g) 。这个元组被 pickle 序列化后通过网络连接发生出去。
# 这一步在 RPCProxy 的 getattr () 方法返回的 do rpc() 闭包中完成。服务器接收
# 后通过 pickle 反序列化消息，查找函数名看看是否已经注册过，然后执行相应的函
# 数。执行结果 (或异常) 被 pickle 序列化后返回发送给客户端。我们的实例需要依赖
# multiprocessing 进行通信。不过，这种方式可以适用于其他任何消息系统。例如，
# 如果你想在 ZeroMQ 之上实习 RPC，仅仅只需要将连接对象换成合适的 ZeroMQ 的
# socket 对象即可

# 由于底层需要依赖 pickle，那么安全问题就需要考虑了（因为一个聪明的黑客可以
# 创建特定的消息，能够让任意函数通过 pickle 反序列化后被执行）。因此你永远不要
# 允许来自不信任或未认证的客户端的 RPC。特别是你绝对不要允许来自 Internet 的任
# 意机器的访问，这种只能在内部被使用，位于防火墙后面并且不要对外暴露。
# 作为 pickle 的替代，你也许可以考虑使用 JSON、 XML 或一些其他的编码格式
# 来序列化消息。例如，本机实例可以很容易的改写成 JSON 编码方案。还需要将
# pickle.loads() 和 pickle.dumps() 替换成 json.loads() 和 json.dumps() 即可：
