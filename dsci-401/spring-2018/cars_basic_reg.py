# This illustrates a basic regression case.

import pandas as pd
import matplotlib.pyplot as plt
import pprint
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

cars = pd.read_csv('./data/cars.csv.')

# Get all non-mpg columns and use as features/predictors.
data_x = cars[list(cars)[1:]] 

# Get mpg column and use as response variable.
data_y = cars[list(cars)[0]] 

# ---------------- Part 0: Do a pairs plot to see potential relationships -------
sm = pd.plotting.scatter_matrix(cars, diagonal='kde')
# plt.tight_layout()
plt.show()

# ---------------- Part 1: Do a basic linear regression -------------------------

# Create a least squares linear regression model.
model = linear_model.LinearRegression()

# Training data used to train the algorithm, test is to assess performance.
# These should always be different - we will correct this below.
x_train, x_test, y_train, y_test = data_x, data_x, data_y, data_y


# Fit the model.
model.fit(x_train,y_train)

# Make predictions on test data and look at the results.
preds = model.predict(x_test)
#pprint.pprint(pd.DataFrame({'Actual':y_test, 'Predicted':preds}))

# ---------------- Part 2: Do linear regression with proper train/test split -------

# Create a least squares linear regression model.
model = linear_model.LinearRegression()

# Split training and test sets from main set. Note: random_state just enables results to be repeated.
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.2, random_state = 4)

# Fit the model.
model.fit(x_train,y_train)

# Make predictions on test data and look at the results.
preds = model.predict(x_test)
pprint.pprint(pd.DataFrame({'Actual':y_test, 'Predicted':preds}))
print('MSE, MAE, R^2, EVS: ' + str([mean_squared_error(y_test, preds), \
							   median_absolute_error(y_test, preds), \
							   r2_score(y_test, preds), \
							   explained_variance_score(y_test, preds)])) 

