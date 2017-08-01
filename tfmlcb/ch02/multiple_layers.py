# Working With Multiple Layers
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import os
from tensorflow.python.framework import ops

ops.reset_default_graph()
sess = tf.Session()

# Create Tensors
# Here we will create a small image of size 4x4 pixels and propagate it through multiple layers.
# Create a small random 'image' of size 4x4
x_shape = [1, 4, 4, 1]
x_val = np.random.uniform(size=x_shape)
# Create the Data Placeholder
x_data = tf.placeholder(tf.float32, shape=x_shape)

# First Layer: Moving Window (Convolution)
# Our first layer will be a spatial moving window of size [2x2] with stride 2
# (in both height and width directions)
# To make this a moving window average, the value of the filter will be all 0.25.
# Create a layer that takes a spatial moving window average
# Our window will be 2x2 with a stride of 2 for height and width
# The filter value will be 0.25 because we want the average of the 2x2 window
my_filter = tf.constant(0.25, shape=[2, 2, 1, 1])
my_strides = [1, 2, 2, 1]
mov_avg_layer= tf.nn.conv2d(x_data, my_filter, my_strides,
                            padding='SAME', name='Moving_Avg_Window')
