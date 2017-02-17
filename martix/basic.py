from numpy import *
import numpy as np

# 创建常见的矩阵
a1 = array([1, 2, 3])
print(a1)
a1 = mat(a1)
print(a1)
data1 = mat(zeros((3, 3)));
# 创建一个3*3的零矩阵，矩阵这里zeros函数的参数是一个tuple类型(3,3)
data2 = mat(ones((2, 4)));
# 创建一个2*4的1矩阵，默认是浮点型的数据，如果需要时int类型，可以使用dtype=int
data3 = mat(random.rand(2, 2));
# 这里的random模块使用的是numpy中的random模块，random.rand(2,2)创建的是一个二维数组，需要将其转换成#matrix
data4 = mat(random.randint(10, size=(3, 3)));
# 生成一个3*3的0-10之间的随机整数矩阵，如果需要指定下界则可以多加一个参数
data5 = mat(random.randint(2, 8, size=(2, 5)))
# 产生一个2-8之间的随机整数矩阵
data6 = mat(eye(2, 2, dtype=int));
# 产生一个2*2的对角矩阵

a1 = [1, 2, 3];
a2 = mat(diag(a1));
# 生成一个对角线为1、2、3的对角矩阵

# 常见的矩阵运算
# 矩阵相乘
a1 = mat([1, 2]);
a2 = mat([[1], [2]]);
# 1*2的矩阵乘以2*1的矩阵，得到1*1的矩阵
a3 = a1 * a2;
print(a1, a2, a3)

# 矩阵对应元素相乘
a1 = mat([1, 1]);
a2 = mat([2, 2]);
a3 = multiply(a1, a2);
print(a1, a2, a3)

# 矩阵点乘
a1 = mat([2, 2]);
a2 = a1 * 2;
print(a2)

# 矩阵求逆
# 求矩阵matrix([[0.5,0],[0,0.5]])的逆矩阵
a1 = mat(eye(2, 2) * 0.5);
a2 = a1.I;
print(a1, a2)

# 矩阵转置
a1 = mat([[1, 1], [0, 0]]);
a2 = a1.T;
print(a1, a2)

# 矩阵行列式
a = mat(random.randint(10, size=(3, 3)))
det = np.linalg.det(a)
print(a)
print("行列式")
print(det)
# 计算矩阵对应行列的最大、最小值、和
a1 = mat([[1, 1], [2, 3], [4, 2]]);
a2 = a1.sum(axis=0);  # 列和，这里得到的是1*2的矩阵
a3 = a1.sum(axis=1);  # 行和，这里得到的是3*1的矩阵
a4 = sum(a1[1, :]);  # 计算第一行所有列的和，这里得到的是一个数值
print(a1, a2, a3, a4)
a1.max();  # 计算a1矩阵中所有元素的最大值,这里得到的结果是一个数值
a2 = max(a1[:, 1]);  # 计算第二列的最大值，这里得到的是一个1*1的矩阵
a1[1, :].max();  # 计算第二行的最大值，这里得到的是一个一个数值

np.max(a1, 0);  # 计算所有列的最大值，这里使用的是numpy中的max函数
np.max(a1, 1);  # 计算所有行的最大值，这里得到是一个矩阵

np.argmax(a1, 0);  # 计算所有列的最大值对应在该列中的索引
np.argmax(a1[1, :]);  # 计算第二行中最大值对应在改行的索引

# 矩阵的分隔，同列表和数组的分隔一致。
a = mat(ones((3, 3)));
b = a[1:, 1:];  # 分割出第二行以后的行和第二列以后的列的所有元素
# 矩阵的合并
a = mat(ones((2, 2)));
b = mat(eye(2));
c = vstack((a, b));  # 按列合并，即增加行数
d = hstack((a, b));  # 按行合并，即行数不变，扩展列数

# 矩阵、列表、数组的转换
l1 = [[1], 'hello', 3];
a = array([[2], [1]]);
dimension = a.ndim;
m, n = a.shape;
number = a.size;  # 元素总个数
str = a.dtype;  # 元素的类型

a1 = [[1, 2], [3, 2], [5, 2]];  # 列表
a2 = array(a1);  # 将列表转换成二维数组
a3 = array(a1);  # 将列表转化成矩阵
a4 = array(a3);  # 将矩阵转换成数组
a5 = a3.tolist();  # 将矩阵转换成列表
a6 = a2.tolist();  # 将数组转换成列表

a1 = [1, 2, 3];
a2 = array(a1);
a3 = mat(a1);
a4 = a2.tolist();  # 这里得到的是[1,2,3]
a5 = a3.tolist();  # 这里得到的是[[1,2,3]]
a6 = (a4 == a5);  # a6=False
a7 = (a4 is a5[0]);  # a7=True,a5[0]=[1,2,3]

dataMat = mat([1]);
val = dataMat[0, 0];  # 这个时候获取的就是矩阵的元素的数值，而不再是矩阵的类型

# 特征值和特征向量
A = np.mat(np.random.randint(10, size=(3, 3)))
a, b = np.linalg.eig(A)
print(a, b)
