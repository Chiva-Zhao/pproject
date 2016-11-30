# coding:utf-8
from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, show, rcParams

rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
l = linspace(1, 3, 3)
# print(l)
v = l ** 3
print(v)
plot(l, v)
xlabel('边长L')
ylabel('体积V')
show()
