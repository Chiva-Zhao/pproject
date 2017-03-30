# 你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为一个字节字符串
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
x = 94522842520747284487117727783387188


def simple():
    print(len(data))
    print(int.from_bytes(data, 'little'), int.from_bytes(data, 'big'))
    print(x.to_bytes(16, 'little'), x.to_bytes(16, 'big'))


simple()
