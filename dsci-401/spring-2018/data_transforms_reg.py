# This illustrates how to use scikit's data preprocessing capabilities.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn import preprocessing

cars = pd.read_csv('./data/cars.csv.')

# Get all non-mpg columns and use as features/predictors.
data_x = cars[list(cars)[1:]] 

# Get mpg column and use as response variable.
data_y = cars[list(cars)[0]]


# ---------------- Part 1: Do data preprocessing: impute values and scale ----------

# Imputing the column means for missing values (strategy=mean) by column (axis=0. axis=1 means by row).
# For more customizing options see 
# http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Imputer.html#sklearn.preprocessing.Imputer
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
data_x = imp.fit_transform(data_x)


# Normalize all predictors to range between 0 and 1.
data_x_norm = preprocessing.normalize(data_x, axis=0)

# Alternative - standardize all features to a column-based z-score.
data_x_std = preprocessing.scale(data_x)

print(data_x_std)

# Many other kinds of scaling possible. For more options see
# http://scikit-learn.org/stable/modules/preprocessing.html


# ---------------- Part 2: Do linear regression with proper train/test split -------

# Use data_std as our transformed data.
data_x = data_x_std

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

