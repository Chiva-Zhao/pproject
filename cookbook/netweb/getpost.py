# 对于简单的事情来说，通常使用 urllib.request 模块就够了。例如，发送一个简
# 单的 HTTP GET 请求到远程的服务上，可以这样做
from urllib import request, parse

url = 'http://httpbin.org/get'
params = {
    'name1': 'value1',
    'name2': 'value2'
}
# Encode the query string
querystring = parse.urlencode(params)
# Make a GET request and read the response
u = request.urlopen(url + '?' + querystring)
resp = u.read()
# 如果你需要使用 POST 方法在请求主体中发送查询参数，可以将参数编码后作为
# 可选参数提供给 urlopen() 函数，就像这样：
# Make a POST request and read the response
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()
# 如果你需要在发出的请求中提供一些自定义的 HTTP 头，例如修改 user-agent
# 字段, 可以创建一个包含字段值的字典，并创建一个 Request 实例然后将其传给
# urlopen() ，如下：
# Extra headers
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
req = request.Request(url, querystring.encode('ascii'), headers=headers)
# Make a request and read the response
u = request.urlopen(req)
resp = u.read()
# 如果需要交互的服务比上面的例子都要复杂，也许应该去看看 requests 库
# （https://pypi.python.org/pypi/requests）。例如，下面这个示例采用 requests 库重
# 新实现了上面的操作：
import requests

# Base URL being accessed
url = 'http://httpbin.org/post'
# Dictionary of query parameters (if any)
parms = {
    'name1': 'value1',
    'name2': 'value2'
}
# Extra headers
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
resp = requests.post(url, data=parms, headers=headers)
# Decoded text returned by the request
text = resp.text
# 关于 requests 库，一个值得一提的特性就是它能以多种方式从请求中返回响应结果
# 的内容。从上面的代码来看， resp.text 带给我们的是以 Unicode 解码的响应文本。
# 但是，如果去访问 resp.content ，就会得到原始的二进制数据。另一方面，如果访问
# resp.json ，那么就会得到 JSON 格式的响应内容。
# 下面这个示例利用 requests 库发起一个 HEAD 请求，并从响应中提取出一些
# HTTP 头数据的字段：
resp = requests.head('http://www.python.org/index.html')
status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']
# 下面是一个利用 requests 通过基本认证登录 Pypi 的例子：
resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user', 'password'))
# 下面是一个利用 requests 将 HTTP cookies 从一个请求传递到另一个的例子：
# First request
resp1 = requests.get(url)
# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)
# 最后一个例子是用 requests 上传内容：
url = 'http://httpbin.org/post'
files = {'file': ('data.csv', open('data.csv', 'rb'))}
r = requests.post(url, files=files)
# 对于真的很简单 HTTP 客户端代码，用内置的 urllib 模块通常就足够了。但是，
# 如果你要做的不仅仅只是简单的 GET 或 POST 请求，那就真的不能再依赖它的功能
# 了。这时候就是第三方模块比如 requests 大显身手的时候了。
# 例如，如果你决定坚持使用标准的程序库而不考虑像 requests 这样的第三方库，
# 那么也许就不得不使用底层的 http.client 模块来实现自己的代码。比方说，下面的
# 代码展示了如何执行一个 HEAD 请求：
from http.client import HTTPConnection
from urllib import parse

c = HTTPConnection('www.python.org', 80)
c.request('HEAD', '/index.html')
resp = c.getresponse()
print('Status', resp.status)
for name, value in resp.getheaders():
    print(name, value)
# 同样地，如果必须编写涉及代理、认证、 cookies 以及其他一些细节方面的代码，
# 那么使用 urllib 就显得特别别扭和啰嗦。比方说，下面这个示例实现在 Python 包索
# 引上的认证：
auth = request.HTTPBasicAuthHandler()
auth.add_password('pypi', 'http://pypi.python.org', 'username', 'password')
opener = request.build_opener(auth)
r = request.Request('http://pypi.python.org/pypi?:action=login')
u = opener.open(r)
resp = u.read()
# From here. You can access more pages using opener
# 坦白说，所有的这些操作在 requests 库中都变得简单的多。
# 在开发过程中测试 HTTP 客户端代码常常是很令人沮丧的，因为所有棘手的细节
# 问题都需要考虑（例如 cookies、认证、 HTTP 头、编码方式等）。要完成这些任务，
# 考虑使用 httpbin 服务（http://httpbin.org）。这个站点会接收发出的请求，然后以
# JSON 的形式将相应信息回传回来。下面是一个交互式的例子：
# >>> import requests
# >>> r = requests.get('http://httpbin.org/get?name=Dave&n=37',
# ... headers = { 'User-agent': 'goaway/1.0' })
# >>> resp = r.json
# >>> resp['headers']
# {'User-Agent': 'goaway/1.0', 'Content-Length': '', 'Content-Type': '',
# 'Accept-Encoding': 'gzip, deflate, compress', 'Connection':
# 'keep-alive', 'Host': 'httpbin.org', 'Accept': '*/*'}
# >>> resp['args']
# {'name': 'Dave', 'n': '37'}
# 在与同一个真正的站点进行交互前，先在 httpbin.org 这样的网站上做实验常常是
# 可取的办法。尤其是当我们面对 3 次登录失败就会关闭账户这样的风险时尤为有用
# （不要尝试自己编写 HTTP 认证客户端来登录你的银行账户）。
# 尽管本节没有涉及，request库还对许多高级的 HTTP 客户端协议提供了支持，
# 比如 OAuth。 requests 模块的文档（http://docs.python-requests.org) 质量很高