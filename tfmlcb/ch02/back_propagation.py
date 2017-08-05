# Implementing Back Propagation
# For this recipe, we will show how to do TWO separate examples,
# a regression example, and a classification example.
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops

ops.reset_default_graph()
sess = tf.Session()

# A Regression Example
# We create a regression example as follows. The input data will be 100 random samples
# from a normal (mean of 1.0, stdev of 0.1). The target will be 100 constant values of 10.0.
# We will fit the regression model:  x_data * A = target_values
# Theoretically, we know that A should be equal to 10.0.
# We start by creating the data and targets with their respective placholders
x_vals = np.random.normal(1, 0.1, 100)
y_vals = np.repeat(10., 100)
x_data = tf.placeholder(shape=[1], dtype=tf.float32)
y_target = tf.placeholder(shape=[1], dtype=tf.float32)
# We now create the variable for our computational graph, A.
# Create variable (one model parameter = A)
A = tf.Variable(tf.random_normal(shape=[1]))
# We add the model operation to the graph. This is just multiplying the input data by A to get the output.
# Add operation to graph
my_output = tf.multiply(x_data, A)
# Next we have to specify the loss function.
# This will allow TensorFlow to know how to change the model variables.
# We will use the L2 loss function here. Note: to use the L1 loss function, change tf.square() to tf.abs().
# Add L2 loss operation to graph
loss = tf.square(my_output - y_target)
# Now we initialize all our variables. For specificity here,
# this is initializing the variable A on our graph with a random standard normal number.
# Initialize variables
init = tf.global_variables_initializer()
sess.run(init)
# We need to create an optimizing operations. Here we use the standard GradientDescentOptimizer(),
# and tell TensorFlow to minimize the loss. Here we use a learning rate of 0.02, but feel
# free to experiment around with this rate, and see the learning curve at the end.
# However, note that learning rates that are too large will result in the algorithm not converging.
# Create Optimizer
my_opt = tf.train.GradientDescentOptimizer(0.02)
train_step = my_opt.minimize(loss)

# Running the Regression Graph!
# Here we will run the regression computational graph for 100 iterations,
# printing out the A-value and loss every 25 iterations.
# We should see the value of A get closer and closer to the true value of 10, as the loss goes down.
# Run Loop
for i in range(100):
    rand_index = np.random.choice(100)
    rand_x = [x_vals[rand_index]]
    rand_y = [y_vals[rand_index]]
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    if (i + 1) % 25 == 0:
        print('Step #' + str(i + 1) + ' A=' + str(sess.run(A)))
        print('Loss = ' + str(sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})))

# Classification Example
# For the classification example, we will create an x-sample made of two different normal
# distribution inputs, Normal(mean = -1, sd = 1) and Normal(mean = 3, sd = 1).
#  For each of these the target will be the class 0 or 1 respectively.
# The model will fit the binary classification: If sigmoid(x+A) < 0.5 then predict class 0, else class 1.
# Theoretically, we know that A should take on the value of the negative average of the two means: -
#  (mean1 + mean2)/2. We start by resetting the computational graph:
ops.reset_default_graph()
sess = tf.Session()
# We generate the data that we will feed into the graph. Note that the x_vals are the combination of
# two separate normals, and the y_vals are the combination of two separate constants (two classes).
# We also create the relevant placeholders for the model.
# Create data
x_vals = np.concatenate((np.random.normal(-1, 1, 50), np.random.normal(3, 1, 50)))
y_vals = np.concatenate((np.repeat(0., 50), np.repeat(1., 50)))
x_data = tf.placeholder(shape=[1], dtype=tf.float32)
y_target = tf.placeholder(shape=[1], dtype=tf.float32)
# We now create the one model variable, used for classification.
# We also set the initialization function, a random normal, to have a mean far
# from the expected theoretical value.
# Initialized to be around 10.0 Theoretically around -1.0
# Create variable (one model parameter = A)
A = tf.Variable(tf.random_normal(mean=10, shape=[1]))
# Now we add the model operation to the graph. This will be the adding of the variable A to the data.
# Note that the sigmoid() is left out of this operation,
# because we will use a loss function that has it built in.
# We also have to add the batch dimension to each of the target and input values
# to use the built in functions.
# Add operation to graph
# Want to create the operstion sigmoid(x + A)
# Note, the sigmoid() part is in the loss function
my_output = tf.add(x_data, A)
# Now we have to add another dimension to each (batch size of 1)
my_output_expanded = tf.expand_dims(my_output, 0)
y_target_expanded = tf.expand_dims(y_target, 0)
# Add classification loss (cross entropy)
xentropy = tf.nn.sigmoid_cross_entropy_with_logits(logits=my_output_expanded, labels=y_target_expanded)
# Now we declare the optimizer function. Here we will be using the standard gradient descent
# operator with a learning rate of 0.05.
# Create Optimizer
my_opt = tf.train.GradientDescentOptimizer(0.05)
train_step = my_opt.minimize(xentropy)
# Next we create an operation to initialize the variables and then run that operation
# Initialize variables
init = tf.global_variables_initializer()
sess.run(init)
# Running the Classification Graph!
# Now we can loop through our classification graph and print the values of A and the loss values.
# Run loop
for i in range(1400):
    rand_index = np.random.choice(100)
    rand_x = [x_vals[rand_index]]
    rand_y = [y_vals[rand_index]]
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    if (i + 1) % 200 == 0:
        print('Step #' + str(i + 1) + ' A = ' + str(sess.run(A)))
        print('Loss = ' + str(sess.run(xentropy, feed_dict={x_data: rand_x, y_target: rand_y})))
# Now we can also see how well we did at predicting the data by creating an accuracy function
# and evaluating them on the known targets.
# Evaluate Predictions
predictions = []
for i in range(len(x_vals)):
    x_val = [x_vals[i]]
    prediction = sess.run(tf.round(tf.sigmoid(my_output)), feed_dict={x_data: x_val})
    predictions.append(prediction[0])
accuracy = sum(x == y for x, y in zip(predictions, y_vals)) / 100.
print('Ending Accuracy = ' + str(np.round(accuracy, 2)))
