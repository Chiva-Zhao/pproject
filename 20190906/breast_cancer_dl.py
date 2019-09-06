# The Power of Deep Learning
# The idea of Deep Learning is to use multiple hidden layers to learn latent and complex data patterns,
# relationships, and representations to build a model that learns and generalizes well on the underlying
# data. Let’s take the previous example and convert it to a fully connected deep neural network (DNN)
# by introducing two more hidden layers. The following snippet builds and trains a DNN with the same
# configuration as our previous experiment only with the addition of two new hidden layers.
from keras import Sequential
from keras.layers import Dense
from sklearn.datasets import load_breast_cancer
from sklearn import metrics

cancer = load_breast_cancer()
# split to train and test data
x_train = cancer.data[:340]
y_train = cancer.target[:340]
x_test = cancer.data[340:]
y_test = cancer.target[340:]

model = Sequential()
model.add(Dense(15, input_dim=30, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=20, batch_size=50)
prediction = model.predict_classes(x_test)
print('Accuracy:', metrics.accuracy_score(y_true=y_test, y_pred=prediction))
print(metrics.classification_report(y_true=y_test, y_pred=prediction))
