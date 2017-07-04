import json


class RPCProxy:
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(json.dumps((name, args, kwargs)))
            result = json.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result

        return do_rpc
# 实现 RPC 的一个比较复杂的问题是如何去处理异常。至少，当方法产生异常时服
# 务器不应该奔溃。因此，返回给客户端的异常所代表的含义就要好好设计了。如果你
# 使用 pickle，异常对象实例在客户端能被反序列化并抛出。如果你使用其他的协议，那
# 得想想另外的方法了。不过至少，你应该在响应中返回异常字符串。我们在 JSON 的
# 例子中就是使用的这种方式。
# 对 于 其 他 的 RPC 实 现 例 子， 我 推 荐 你 看 看 在 XML-RPC 中 使 用 的
# SimpleXMLRPCServer 和 ServerProxy 的实现