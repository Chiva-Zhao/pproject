# This script introduces various ways to create tensors in TensorFlow
import tensorflow as tf
from tensorflow.python.framework import ops

ops.reset_default_graph()
# Start a graph session
# Get graph handle with the tf.Session()
sess = tf.Session()

# Creating Tensors
# TensorFlow has built in function to create tensors for use in variables.
# For example, we can create a zero filled tensor of predefined shape using
# the tf.zeros() function as follows.
my_tensor = tf.zeros([1, 20])
print(sess.run(my_tensor))
# TensorFlow algorithms need to know which objects are variables and which are constants.
# For now we create a variable using the TensorFlow function tf.Variable() as follows.
my_var = tf.Variable(tf.zeros([1, 20]))
# Note that you can not run sess.run(my_var), this would result in an error.
# Because TensorFlow operates with computational graphs, we have to create a variable
# intialization operation in order to evaluate variables. We will see more of this later on.
# For this script, we can initialize one variable at a time by calling the variable method
# my_var.initializer.
sess.run(my_var.initializer)
print(sess.run(my_var))

row_dim = 2
col_dim = 3
zero_var = tf.Variable(tf.zeros([row_dim, col_dim]))
ones_var = tf.Variable(tf.ones([row_dim, col_dim]))
# Again, we can call the initializer method on our variables and run them to evaluate thier contents.
sess.run(zero_var.initializer)
sess.run(ones_var.initializer)
print(sess.run(zero_var))
print(sess.run(ones_var))

# Creating Tensors Based on Other Tensor's Shape
# If the shape of a tensor depends on the shape of another tensor, then we can use the
# TensorFlow built-in functions ones_like() or zeros_like().
zero_similar = tf.Variable(tf.zeros_like(zero_var))
ones_similar = tf.Variable(tf.ones_like(ones_var))
sess.run(ones_similar.initializer)
sess.run(zero_similar.initializer)
print(sess.run(ones_similar))
print(sess.run(zero_similar))

# Filling a Tensor with a Constant
# Here is how we fill a tensor with a constant.
fill_var = tf.Variable(tf.fill([row_dim, col_dim], -1))
sess.run(fill_var.initializer)
print(sess.run(fill_var))
# We can also create a variable from an array or list of constants.
# Create a variable from a constant
const_var = tf.Variable(tf.constant([8, 6, 7, 5, 3, 0, 9]))
# This can also be used to fill an array:
const_fill_var = tf.Variable(tf.constant(-1, shape=[row_dim, col_dim]))

sess.run(const_var.initializer)
sess.run(const_fill_var.initializer)
print(sess.run(const_var))
print(sess.run(const_fill_var))

# Creating Tensors Based on Sequences and Ranges
# We can also create tensors from sequence generation functions in TensorFlow.
# The TensorFlow function linspace() and range() operate very similar to the python/numpy equivalents.

# Linspace in TensorFlow
# Generates [0.0, 0.5, 1.0] includes the end Range in TensorFlow
linear_var = tf.Variable(tf.linspace(start=0.0, stop=1.0, num=3))
# Generates [6, 9, 12] doesn't include the end
sequence_var = tf.Variable(tf.range(start=6, limit=15, delta=3))
sess.run(linear_var.initializer)
sess.run(sequence_var.initializer)
print(sess.run(linear_var))
print(sess.run(sequence_var))

# Random Number Tensors