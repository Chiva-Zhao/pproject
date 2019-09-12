from sklearn import datasets
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
import numpy as np

diabetes = datasets.load_diabetes()
y = diabetes.target
x = diabetes.data

# split our data into separate test and train sets of data (train is used to train the model and
# test is used for model performance testing and evaluation).
x_train = x[:310]
y_train = y[:310]
x_test = x[310:]
y_test = y[310:]
# Then we will define the model we want to use and the parameter space for one of the model’s
# hyperparameters. Here we will search the parameter alpha of the Lasso model. This parameter basically
# controls the strictness our regularization.
lasso = Lasso(random_state=0)
alphas = np.logspace(-4, 0.5, 30)
# Then we will initialize an estimator that will identify the model to be used. Here we notice that the
# process is identical for both learning a single model and a grid search of models, i.e. they both are objects of
# the estimator class
estimator = GridSearchCV(lasso, dict(alpha=alphas))
estimator.fit(x_train, y_train)
estimator.best_estimator_
estimator.best_score_
estimator.predict(x_test)
