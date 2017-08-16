# Linear Regression: The TensorFlow Way
# For this script, we introduce how to perform linear regression in the context of TensorFlow.
# We will solve the linear equation system:y=Ax+b
# With the Sepal length (y) and Petal width (x) of the Iris data.
# Performing linear regression in TensorFlow is a lot easier than trying to understand
# Linear Algebra or Matrix decompositions for the prior two recipes. We will do the following:
# 1.Create the linear regression computational graph output.
# This means we will accept an input,x and generate the output,  Ax+b.
# 2.We create a loss function, the L2 loss, and use that output with the
# learning rate to compute the gradients of the model variables,  A and b to minimize the loss.
# The benefit of using TensorFlow in this way is that the model can be routinely updated
# and tweaked with new data incrementally with any reasonable batch size of data.
# The more iterative we make our machine learning algorithms, the better.
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn import datasets
from tensorflow.python.framework import ops
ops.reset_default_graph()
sess = tf.Session()
# Next we load the Iris data from the Scikit-Learn library.
# Load the data
# iris.data = [(Sepal Length, Sepal Width, Petal Length, Petal Width)]
iris = datasets.load_iris()
x_vals = np.array([x[3] for x in iris.data])
y_vals = np.array([y[0] for y in iris.data])
# With most TensorFlow algorithms, we will need to declare a batch size for the placeholders and
# operations in the graph. Here, we set it to 25. We can set it to any integer between 1 and the size of the dataset.
# For the effect of batch size on the training, see Batch vs Stochastic Training