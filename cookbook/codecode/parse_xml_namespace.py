# 利用命名空间解析 XML 文档
from xml.etree.ElementTree import parse, iterparse

doc = parse('ns_demo.xml')
print(doc.findtext('author'))
print(doc.find('content'))
# A query involving a namespace (doesn't work)
print(doc.find('content/html'))
# Works if fully qualified
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))
# Doesn't work
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title'))
# Fully qualified
print(doc.findtext(
    'content/{http://www.w3.org/1999/xhtml}html/{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))


# 你可以通过将命名空间处理逻辑包装为一个工具类来简化这个过程
class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(doc.find(ns('content/{html}html')))
print(doc.findtext(ns('content/{html}html/{html}head/{html}title')))
# 解析含有命名空间的 XML 文档会比较繁琐。上面的 XMLNamespaces 仅仅是允许你
# 使用缩略名代替完整的 URI 将其变得稍微简洁一点。
# 很不幸的是，在基本的 ElementTree 解析中没有任何途径获取命名空间的信息。
# 但是，如果你使用 iterparse() 函数的话就可以获取更多关于命名空间处理范围的信息。
for evt, elem in iterparse('ns_demo.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)
# 最后一点，如果你要处理的 XML 文本除了要使用到其他高级 XML 特性外，还要
# 使用到命名空间，建议你最好是使用 lxml 函数库来代替 ElementTree 。例如， lxml
# 对利用 DTD 验证文档、更好的 XPath 支持和一些其他高级 XML 特性等都提供了更好的支持