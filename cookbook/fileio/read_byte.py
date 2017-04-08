# 读写二进制文件，比如图片，声音文件等等
# 使用模式为 rb 或 wb 的 open() 函数来读取或写入二进制数据
# Read the entire file as a single byte string
# with open('somefile.bin', 'rb') as f:
#     data = f.read()
# Write binary data to a file
# with open('somefile.bin', 'wb') as f:
#     f.write(b'Hello World')
# 在读取二进制数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜
# 在的陷阱。特别需要注意的是，索引和迭代动作返回的是字节的值而不是字节字符串
t = 'Hello World'
for c in t:
    print(c)
b = b'hello world'
for c in b:
    print(c)
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
    print(text)
with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
# 二进制 I/O 还有一个鲜为人知的特性就是数组和 C 结构体类型能直接被写入，而
# 不需要中间转换为自己对象
import array

nums = array.array('i', [1, 2, 3, 4])
print(nums)
with open('data.bin', 'wb') as f:
    f.write(nums)
# 这个适用于任何实现了被称之为” 缓冲接口” 的对象，这种对象会直接暴露其底层
# 的内存缓冲区给能处理它的操作。二进制数据的写入就是这类操作之一。
# 很多对象还允许通过使用文件对象的 readinto() 方法直接读取二进制数据到其底
# 层的内存中去
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
print(a)
with open('data.bin', 'rb') as f:
    f.readinto(a)
print(a)