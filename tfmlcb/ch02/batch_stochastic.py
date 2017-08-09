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
# Loss Function
# For this, we choose the L2 loss. We can easily choose the L1 loss by replacing tf.square() with tf.abs().
# Add L2 loss operation to graph
loss = tf.square(my_output - y_target)
# Optimization and Initialization
# For the optimization function, we will choose the standard Gradient Descent Algorithm with a learning rate of 0.02.
# We also add and run a variable initialization operation.
# Create Optimizer
my_opt = tf.train.GradientDescentOptimizer(0.02)
train_step = my_opt.minimize(loss)
# Initialize variables
init = tf.global_variables_initializer()
sess.run(init)
# Train Model
# We run the training step for 100 iterations and print off the value of A and the loss every 5 iterations.
loss_stochastic = []
for i in range(100):
    rand_index = np.random.choice(100)
    rand_x = [x_vals[rand_index]]
    rand_y = [y_vals[rand_index]]
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    if (i + 1) % 5 == 0:
        print('Step #' + str(i + 1) + ' A = ' + str(sess.run(A)))
        temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
        print('Loss = ' + str(temp_loss))
        loss_stochastic.append(temp_loss)

# Batch Training
# We start by resetting the computational graph
# Batch Training:
# Re-initialize graph
ops.reset_default_graph()
sess = tf.Session()
# For Batch training, we need to declare our batch size.
# The larger the batch size, the smoother the convergence will be towards the optimal value.
# But if the batch size is too large, the optimization algorithm may get stuck in a local minimum,
# where a more stochastic convergence may jump out.
# Here, the we may change the batch size from 1 to 100 to see the effects of
# the batch size on the convergence plots at the end.
# Declare batch size
batch_size = 25
# Generate the Data
# The data we will create is 100 random samples from a Normal(mean = 1, sd = 0.1).
# The target will be an array of size 100 filled with the constant 10.0.
# We also create the necessary placeholders in the graph for the data and target.
# Note that here, our placeholders have shape [None, 1], where the batch size will
# take the place of the None dimension.
# Create data
x_vals = np.random.normal(1, 0.1, 100)
y_vals = np.repeat(10., 100)
x_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
# Model Variables and Operations
# We create the one variable in the graph, A. We then create the model operation,
# which is just the multiplication of the input data and A.
# Create variable (one model parameter = A)
A = tf.Variable(tf.random_normal(shape=[1, 1]))
# Add operation to graph
my_output = tf.matmul(x_data, A)
# Loss Function
# For this, we choose the L2 loss. We can easily choose the L1 loss by replacing tf.square() with tf.abs().
# Add L2 loss operation to graph
loss = tf.reduce_mean(tf.square(my_output - y_target))
# Optimization and Initialization
# For the optimization function, we will choose the standard Gradient Descent Algorithm
# with a learning rate of 0.02. We also add and run a variable initialization operation.
init = tf.global_variables_initializer()
sess.run(init)
# Create Optimizer
my_opt = tf.train.GradientDescentOptimizer(0.02)
train_step = my_opt.minimize(loss)
# Train Model
# We run the training step for 100 iterations and print off the value of A and the loss every 5 iterations.
# Note that here we select a batch of data instead of just one data point.
loss_batch = []
# Run Loop
for i in range(100):
    rand_index = np.random.choice(100, size=batch_size)
    rand_x = np.transpose([x_vals[rand_index]])
    rand_y = np.transpose([y_vals[rand_index]])
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    if (i + 1) % 5 == 0:
        print('Step #' + str(i + 1) + ' A = ' + str(sess.run(A)))
        temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
        print('Loss = ' + str(temp_loss))
        loss_batch.append(temp_loss)
# Plot Stochastic vs Batch Training
plt.plot(range(0, 100, 5), loss_stochastic, 'b-', label='Stochastic Loss')
plt.plot(range(0, 100, 5), loss_batch, 'r--', label='Batch Loss, size=20')
plt.legend(loc='upper right', prop={'size': 11})
plt.show()