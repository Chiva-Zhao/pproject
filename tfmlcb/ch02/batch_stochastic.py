# Batch and Stochastic Training
# This python function illustrates two different training methods: batch and stochastic training.
# For each model, we will use a regression model that predicts one model variable.
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops

ops.reset_default_graph()
sess = tf.Session()
# Stochastic Training
# Generate Data
# The data we will create is 100 random samples from a Normal(mean = 1, sd = 0.1).
# The target will be an array of size 100 filled with the constant 10.0.
# We also create the necessary placeholders in the graph for the data and target.
# Note that we use a shape of [1] for stochastic training.
x_vals = np.random.normal(1, 0.1, 100)
y_vals = np.repeat(10, 100)
x_data = tf.placeholder(shape=[1], dtype=tf.float32)
y_target = tf.placeholder(shape=[1], dtype=tf.float32)
# Model Variables and Operations
# We create the one variable in the graph, A. We then create the model operation,
# which is just the multiplication of the input data and A.
# Create variable (one model parameter = A)
A = tf.Variable(tf.random_normal(shape=[1]))
# Add operation to graph
my_output = tf.multiply(x_data, A)
