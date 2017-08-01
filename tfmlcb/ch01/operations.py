# This function introduces various operations in TensorFlow
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops

ops.reset_default_graph()
sess = tf.Session()

# Arithmetic Operations
# TensorFlow has multiple types of arithmetic functions.
# Here we illustrate the differences between div(), truediv() and floordiv().
# div() : integer of division (similar to base python /)
# truediv() : will convert integer to floats.
# floordiv() : float of div()
print(sess.run(tf.div(3, 4)))
print(sess.run(tf.truediv(3, 4)))
print(sess.run(tf.floordiv(3.0, 4.0)))
# Mod function:
print(sess.run(tf.mod(22., 5.)))
# Cross Product:
print(sess.run(tf.cross([1., 0, 0], [0., 1., 0.])))
# Trig functions-Sine, Cosine, and Tangent:
print(sess.run(tf.sin(3.1416)))
print(sess.run(tf.cos(3.1416)))
print(sess.run(tf.div(tf.sin(3.1416 / 4.), tf.cos(3.1416 / 4.))))
# Custom operations
# Here we will create a polynomial function:f(x) = 3 * x^2 - x + 10
test_nums = range(15)
def custom_polynomial(x_val):
    # Return 3x^2 - x + 10
    return (tf.subtract(3 * tf.square(x_val), x_val) + 10)
print(sess.run(custom_polynomial(11)))
# What should we get with list comprehension:
expected_output = [3 * x * x - x + 10 for x in test_nums]
print(expected_output)
# TensorFlow custom function output:
for num in test_nums:
    print(sess.run(custom_polynomial(num)))
