# 你需要读取包含嵌套或者可变长记录集合的复杂二进制格式的数据。这些数据可能
# 包含图片、视频、电子地图文件等
# struct 模块可被用来编码/解码几乎所有类型的二进制的数据结构。为了解释清楚
# 这种数据，假设你用下面的 Python 数据结构来表示一个组成一系列多边形的点的集合
polys = [
    [(1.0, 2.5), (3.5, 4.0), (2.5, 1.5)],
    [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
    [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)],
]

import struct


class StructField:
    '''
    Descriptor representing a simple structure field
    '''

    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


# 这里我们使用了一个描述器来表示每个结构字段，每个描述器包含一个结构兼容
# 格式的代码以及一个字节偏移量，存储在内部的内存缓冲中。在 get () 方法中，
# struct.unpack from() 函数被用来从缓冲中解包一个值，省去了额外的分片或复制操
# 作步骤。
# Structure 类就是一个基础类，接受字节数据并存储在内部的内存缓冲中，并被
# StructField 描述器使用。这里使用了 memoryview() ，我们会在后面详细讲解它是用
# 来干嘛的。
# 使用这个代码，你现在就能定义一个高层次的结构对象来表示上面表格信息所期望
# 的文件格式
class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num_polys = StructField('<i', 36)


# 下面的例子利用这个类来读取之前我们写入的多边形数据的头部数据：
f = open('polys.bin', 'rb')
phead = PolyHeader(f.read(40))
print(phead.file_code == 0x1234)
print(print(phead.min_x))
print(phead.min_y)
print(phead.max_x)
print(phead.max_y)
print(phead.num_polys)


# 任何时候只要你遇到了像这样冗余的类定义，你应该考虑下使用类装饰器或元类。
# 元类有一个特性就是它能够被用来填充许多低层的实现细节，从而释放使用者的负担。
# 下面我来举个例子，使用元类稍微改造下我们的 Structure 类：
class StructureMeta(type):
    '''
    Metaclass that automatically creates StructField descriptors
    '''

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<', '>', '!', '@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


# 使用新的 Structure 类，你可以像下面这样定义一个结构：
class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]


f = open('polys.bin', 'rb')
phead = PolyHeader(f.read(40))
print(phead.file_code == 0x1234)
print(print(phead.min_x))
print(phead.min_y)
print(phead.max_x)
print(phead.max_y)
print(phead.num_polys)


# 一旦你开始使用了元类，你就可以让它变得更加智能。例如，假设你还想支持嵌套
# 的字节结构，下面是对前面元类的一个小的改进，提供了一个新的辅助描述器来达到
# 想要的效果
class NestedStruct:
    '''
    Descriptor representing a nested structure
    '''

    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:
            self.offset + self.struct_type.struct_size]
            result = self.struct_type(data)
            # Save resulting structure back on instance to avoid
            # further recomputation of this step
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    '''
    Metaclass that automatically creates StructField descriptors
    '''

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname,
                        NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


# 在这段代码中， NestedStruct 描述器被用来叠加另外一个定义在某个内存区域上
# 的结构。它通过将原始内存缓冲进行切片操作后实例化给定的结构类型。由于底层的
# 内存缓冲区是通过一个内存视图初始化的，所以这种切片操作不会引发任何的额外的
# 内存复制。相反，它仅仅就是之前的内存的一个叠加而已。另外，为了防止重复实例
# 化，描述器保存了该实例中的内部结构对象
# 使用这个新的修正版，你就可以像下面这样编写：

class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
    ]


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),  # nested struct
        (Point, 'max'),  # nested struct
        ('i', 'num_polys')
    ]
f = open('polys.bin', 'rb')
phead = PolyHeader(f.read(40))
print(phead.file_code == 0x1234)
print(print(phead.min_x))
print(phead.min_y)
print(phead.max_x)
print(phead.max_y)
print(phead.num_polys)