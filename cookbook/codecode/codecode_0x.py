# 编码和解码十六进制数
# 将一个十六进制字符串解码成一个字节字符串或者将一个字节字符串编码成一
# 个十六进制字符串。

# Initial byte string
s = b'hello'
# Encode as hex
import binascii

h = binascii.b2a_hex(s)
print(h)
# Decode back to bytes
print(binascii.a2b_hex(h))
# 类似的功能同样可以在 base64 模块中找到
import base64

h = base64.b16encode(s)
print(h)
print(base64.b16decode(h))
# 大部分情况下，通过使用上述的函数来转换十六进制是很简单的。上面两种技术的
# 主要不同在于大小写的处理。函数 base64.b16decode() 和 base64.b16encode() 只能
# 操作大写形式的十六进制字母，而 binascii 模块中的函数大小写都能处理。
# 还有一点需要注意的是编码函数所产生的输出总是一个字节字符串。如果想强制以
# Unicode 形式输出，你需要增加一个额外的解码步骤
h = base64.b16encode(s)
print(h)
print(h.decode('ascii'))
# 在解码十六进制数时，函数 b16decode() 和 a2b hex() 可以接受字节或 unicode 字
# 符串。但是， unicode 字符串必须仅仅只包含 ASCII 编码的十六进制数
