# 实现远程方法调用
# 你想在一个消息传输层如 sockets 、 multiprocessing connections 或 ZeroMQ 的
# 基础之上实现一个简单的远程过程调用（RPC）。

# 将函数请求、参数和返回值使用 pickle 编码后，在不同的解释器直接传送 pickle 字
# 节字符串，可以很容易的实现 RPC。下面是一个简单的 PRC 处理器，可以被整合到
# 一个服务器中去：
# rpcserver.py
import pickle


class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                # Receive a message
                func_name, args, kwargs = pickle.loads(connection.recv())
                # Run the RPC and send a response
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


# 要使用这个处理器，你需要将它加入到一个消息服务器中。你有很多种选择，但是
# 使用 multiprocessing 库是最简单的。下面是一个 RPC 服务器例子：
from multiprocessing.connection import Listener
from threading import Thread


def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()


# Some remote functions
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


# Register with a handler
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)
# Run the server
rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')
