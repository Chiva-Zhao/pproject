import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import os
from tensorflow.python.framework import ops

ops.reset_default_graph()
sess = tf.Session()

# Create the Tensors, Constants, and Placeholders
# We start by creating an array to feed in to a placeholder (note the agreements on the dimensions).
# We then declare some graph constants to use in the operations.
# Create data to feed in
my_array = np.array([[1., 3., 5., 7., 9.],
                     [-2., 0., 2., 4., 6.],
                     [-6., -3., 0., 3., 6.]])
# Duplicate the array for having two inputs
x_vals = np.array([my_array, my_array + 1])
# Declare the placeholder
x_data = tf.placeholder(tf.float32, shape=(3, 5))
# Declare constants for operations
m1 = tf.constant([[1.], [0.], [-1.], [2.], [4.]])
m2 = tf.constant([[2.]])
a1 = tf.constant([[10.]])
# We start with matrix multiplication (A[3x5] * m1[5x1]) = prod1[3x1]
# 1st Operation Layer = Multiplication
prod1 = tf.matmul(x_data, m1)
# Second operation is multiplication of prod1[3x1] by m2[1x1], which results in prod2[3x1]
# 2nd Operation Layer = Multiplication
prod2 = tf.matmul(prod1, m2)
# The third operation is matrix addition of prod2[3x1] to a1[1x1],
# This makes use of TensorFlow's broadcasting.
# 3rd Operation Layer = Addition
add1 = tf.add(prod2, a1)
# Create and Format Tensorboard outputs for viewing
merged = tf.summary.merge_all(key='summaries')
if not os.path.exists('tensorboard_logs/'):
    os.makedirs('tensorboard_logs/')
my_writer = tf.summary.FileWriter('tensorboard_logs/', sess.graph)
# Evaluate and Print Output
for x in x_vals:
    print(sess.run(add1, feed_dict={x_data: x}))