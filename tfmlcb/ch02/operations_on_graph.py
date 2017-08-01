# Operations on a Computational Graph
import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops

ops.reset_default_graph()
sess = tf.Session()

# Create tensors
# Create data to feed in the placeholder
x_vals = np.array([1., 3., 5., 7., 9.])
# Create the TensorFlow Placceholder
x_data = tf.placeholder(tf.float32)
# Constant for multilication
m = tf.constant(3.)
# We loop through the input values and print out the multiplication operation for each input.
# Multiplication
prod = tf.multiply(x_data, m)

# Output graph to Tensorboard
merged = tf.summary.merge_all(key='summaries')
if not os.path.exists('tensorboard_logs/'):
    os.makedirs('tensorboard_logs/')
my_writer = tf.summary.FileWriter('tensorboard_logs/', sess.graph)
for x in x_vals:
    print(sess.run(prod, feed_dict={x_data: x}))
