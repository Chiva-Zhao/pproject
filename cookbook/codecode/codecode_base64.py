# 编码解码 Base64 数据
# base64 模块中有两个函数 b64encode() and b64decode() 可以帮你解决这个问题。
# Some byte data
s = b'hello'
import base64

# Encode as Base64
a = base64.b64encode(s)
print(a)
# Decode from Base64
print(base64.b64decode(a))
# Base64 编码仅仅用于面向字节的数据比如字节字符串和字节数组。此外，编码处
# 理的输出结果总是一个字节字符串。如果你想混合使用 Base64 编码的数据和 Unicode
# 文本，你必须添加一个额外的解码步骤。
a = base64.b64encode(s).decode('ascii')
print(a)
# 当解码 Base64 的时候，字节字符串和 Unicode 文本都可以作为参数。
# 但是， Unicode 字符串只能包含 ASCII 字符