from sklearn.datasets import load_breast_cancer
from keras.models import Sequential
from keras.layers import Dense

# load the cancel data
cancer = load_breast_cancer()
x_train = cancer.data[:340]
y_train = cancer.target[:340]
x_test = cancer.data[340:]
y_test = cancer.target[340:]
# The next step of the process is to define the model architecture using the keras model class. We see that
# our input vector is having 30 attributes so we will have a shallow network having one hidden layer of half
# the units (neurons), i.e., we will have 15 units in the hidden layer. We add a one unit output layer to predict
# either 1 or 0 based on whether the input data point is benign or malignant.
model = Sequential()
model.add(Dense(15, input_dim=30, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Here we have defined a sequential keras model, which is having a dense hidden layer of 15 units.
# The dense layer means a fully connected layer so it means that each of those 15 units (neurons) is fully
# connected to the 30 input features. The output layer for our example is a dense layer with the sigmoid
# activation. The sigmoid activation is used to convert a real valued input into a binary output (1 or 0). Once
# we have defined the model we will then compile the model by supplying the necessary optimizer, loss
# function, and the metric on which we want to evaluate the model performance
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
# Here we used a loss function of binary_crossentropy, which is a standard loss function for binary
# classification problems. For the optimizer, we used rmsprop, which is an upgrade from the normal gradient
# descent algorithm. The next step is to fit the model using the fit function.
model.fit(x_train, y_train, epochs=20, batch_size=50)
# Here, the epochs parameter indicates one complete forward and backward pass of all the training
# examples. The batch_size parameter indicates the total number of samples which are propagated through
# the NN model at a time for one backward and forward pass for training the model and updating the gradient.

# Thus if you have 100 observations and your batch size is 10, each epoch will consist of 10 iterations where 10
# observations (data points) will be passed through the network at a time and the weights on the hidden layer
# units will be updated. However we can see that the overall loss and training accuracy remains the same.
# Which means the model isn’t really learning anything from the looks of it!

# The API for keras again follows the convention for scikit-learn models, hence we can use the predict
# function to predict for the data points in the test set. In fact we use predict_classes to get the actual class
# label predicted for each test data instance
prediction = model.predict_classes(x_test)

# Let’s evaluate the model performance by looking at the test data accuracy and other performance
# metrics like precision, recall, and F1 score. Do not despair if you do not understand some of these terms, as
# we will be covering them in detail in Chapter 5. For now, you should know that scores closer to 1 indicate
# better results i.e., an accuracy of 1 would indicate 100% model accuracy, which is perfection. Luckily,
# scikit-learn provides us with necessary performance metric measuring APIs.
from sklearn import metrics

print('Accuracy:', metrics.accuracy_score(y_true=y_test, y_pred=prediction))
print(metrics.classification_report(y_true=y_test, y_pred=prediction))
# We achieve an overall accuracy and F1 score of 91% and we can see that we also have an F1 score of 83%
# as compared to 0% from the previous model, for class label 0 (malignant). Thus you can clearly get a feel of
# the power of Deep Learning, which is evident by just introducing more hidden layers in our network, which
# enabled our model to learn better representations of our data. Try experimenting with other architectures or
# even introducing regularization aspects like dropout.