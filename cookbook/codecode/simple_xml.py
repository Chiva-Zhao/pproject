# 从一个简单的 XML 文档中提取数据。
# 可以使用 xml.etree.ElementTree 模块从简单的 XML 文档中提取数据。为了演
# 示，假设你想解析 Planet Python 上的 RSS 源
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)
e = doc.find('channel/item')
print(e, e.tag, e.text)
# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
    print()
# xml.etree.ElementTree.parse() 函数解析整个 XML 文档并将其转换成一个文档
# 对象。然后，你就能使用 find() 、 iterfind() 和 findtext() 等方法来搜索特定的
# XML 元素了。这些函数的参数就是某个指定的标签名，例如 channel/item 或 title
# 每次指定某个标签时，你需要遍历整个文档结构。每次搜索操作会从一个起始元
# 素开始进行。同样，每次操作所指定的标签名也是起始元素的相对路径。例如，执行
# doc.iterfind('channel/item') 来搜索所有在 channel 元素下面的 item 元素。 doc
# 代表文档的最顶层 (也就是第一级的 rss 元素)。然后接下来的调用 item.findtext()
# 会从已找到的 item 元素位置开始搜索。
# ElementTree 模块中的每个元素有一些重要的属性和方法，在解析的时候非常有
# 用。 tag 属性包含了标签的名字， text 属性包含了内部的文本，而 get() 方法能获取
# 属性值。

# 有一点要强调的是 xml.etree.ElementTree 并不是 XML 解析的唯一方法。对于
# 更高级的应用程序，你需要考虑使用 lxml 。它使用了和 ElementTree 同样的编程接
# 口，因此上面的例子同样也适用于 lxml。你只需要将刚开始的 import 语句换成 from
# lxml.etree import parse 就行了。 lxml 完全遵循 XML 标准，并且速度也非常快，
# 同时还支持验证， XSLT，和 XPath 等特性
