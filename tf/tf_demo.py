# 基本的元素有如下三种：常量（constant）、可训练的变量（Variable）和不可训练的变量
import tensorflow as tf
import numpy as np

# 定义常量、同时把数据类型定义为能够进行 GPU 计算的 tf.float32 类型
x = tf.constant(1, dtype=tf.float32)
# 定义可训练的变量
y = tf.Variable(2, dtype=tf.float32)
# 定义不可训练的变量
z = tf.Variable(3, dtype=tf.float32, trainable=False)
x_add_y = x + y
y_sub_z = y - z
x_times_z = x * z
z_div_x = z / x
with tf.Session().as_default() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run([x, y, z, x_add_y, y_sub_z, z_div_x]))
# 用 Numpy 数组进行 Tensor 的初始化
x = tf.constant(np.array([[1, 2], [3, 4]]))
# Tensorflow 中对应于 np.sum 的方法
axis0 = tf.reduce_sum(x, axis=0)  # 将会得到值为 [ 4 6 ] 的 Tensor
axis1 = tf.reduce_sum(x, axis=1)  # 将会得到值为 [ 3 7 ] 的 Tensor
print(axis0, axis1)
