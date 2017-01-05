# coding:utf-8
from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, show, rcParams
rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
v0 = 5
g = 9.81
t = linspace(0, 1, 1001)
y = v0 * t - 0.5 * g * t ** 2
plot(t, y)
xlabel('t(s)')
ylabel('y(m)')
show()
