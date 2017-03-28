# 在字符串中处理 html 和 xml
import html


def simple():
    s = 'Elements are written as "<tag>text</tag>".'
    t = 'Spicy Jalapeño'
    print(html.escape(s, quote=False))
    print(t.encode('ascii', errors='xmlcharrefreplace'))


def more():
    s = 'Spicy &quot;Jalape&#241;o&quot.'
    print(html.unescape(s))
    t = 'The prompt is &gt;&gt;&gt;'
    from xml.sax.saxutils import unescape
    print(unescape(t))

# simple()
more()
