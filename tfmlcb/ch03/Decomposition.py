# This script will use TensorFlow's function, tf.cholesky() to decompose our design matrix and
# solve for the parameter matrix from linear regression.
# For linear regression we are given the system  A⋅x=y . Here,  A  is our design matrix,
# x  is our parameter matrix (of interest), and  y is our target matrix (dependent values).
# For a Cholesky decomposition to work we assume that  A  can be broken up into a product of a
# lower triangular matrix,  L and the transpose of the same matrix,  LT.
# Note that this is when  A  is square. Of course, with an over determined system,
# A  is not square. So we factor the product  AT⋅A  instead. We then assume:AT⋅A=LT⋅L
# Given that A has a unique Cholesky decomposition, we can write our linear regression system as the following:
# LT⋅L⋅x=AT⋅y Then we break apart the system as follows: LT⋅z=AT⋅y and L⋅x=z
# The steps we will take to solve for  x  are the following
# 1.Compute the Cholesky decomposition of  A, where  AT⋅A=LT⋅L
# 2.Solve ( LT⋅z=AT⋅y) for  z .
# 3.Finally, solve ( L⋅x=z) for  x .
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops

ops.reset_default_graph()
sess = tf.Session()
# We use the same method of generating data as in the prior recipe for consistency.
# Create the data
x_vals = np.linspace(0, 10, 100)
y_vals = x_vals + np.random.normal(0, 1, 100)
# We generate the design matrix,  A.
# Create design matrix
x_vals_column = np.transpose(np.matrix(x_vals))
ones_column = np.transpose(np.matrix(np.repeat(1, 100)))
A = np.column_stack((x_vals_column, ones_column))
# Create y matrix
y = np.transpose(np.matrix(y_vals))
# Create tensors
A_tensor = tf.constant(A)
y_tensor = tf.constant(y)
# Now we calculate the square of the matrix  A  and the Cholesky decomposition.
# Find Cholesky Decomposition
tA_A = tf.matmul(tf.transpose(A_tensor), A_tensor)
L = tf.cholesky(tA_A)
# We solve the first equation. (see step 2 in the intro paragraph above)
# Solve L*y=t(A)*b
tA_y = tf.matmul(tf.transpose(A_tensor), y)
sol1 = tf.matrix_solve(L, tA_y)
# We finally solve for the parameter matrix by solving the
# second equation (see step 3 in the intro paragraph).
# Solve L' * y = sol1
sol2 = tf.matrix_solve(tf.transpose(L), sol1)
solution_eval = sess.run(sol2)
# Extract the coefficients and create the best fit line.
# Extract coefficients
slope = solution_eval[0][0]
y_intercept = solution_eval[1][0]
print('slope: ' + str(slope))
print('y_intercept: ' + str(y_intercept))
# Get best fit line
best_fit = []
for i in x_vals:
    best_fit.append(slope * i + y_intercept)
# Finally, we plot the fit with Matplotlib.
# Plot the results
plt.plot(x_vals, y_vals, 'o', label='Data')
plt.plot(x_vals, best_fit, 'r-', label='Best fit line', linewidth=3)
plt.legend(loc='upper left')
plt.show()
