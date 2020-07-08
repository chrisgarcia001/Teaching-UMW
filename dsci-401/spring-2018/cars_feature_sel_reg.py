# This illustrates several feature selection methods for regression.

import pandas as pd
import matplotlib.pyplot as plt
import pprint
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import make_scorer
from sklearn.metrics import explained_variance_score
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import RFECV


cars = pd.read_csv('./data/cars.csv.')

# Get all non-mpg columns and use as features/predictors.
data_x = cars[list(cars)[1:]] 

# Get mpg column and use as response variable.
data_y = cars[list(cars)[0]] 

# ---------------- Part 0: Plot data, split data, and build a baseline model ----
# sm = pd.plotting.scatter_matrix(cars, diagonal='kde')
# plt.tight_layout()
# plt.show()

# Split training and test sets from main set. Note: random_state just enables results to be repeated.
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.2, random_state = 4)
base_model = linear_model.LinearRegression()

# Fit the model.
base_model.fit(x_train, y_train)

# Make predictions on test data and look at the results.
preds = base_model.predict(x_test)
pprint.pprint(pd.DataFrame({'Actual':y_test, 'Predicted':preds}))

print('MSE, MAE, R^2, EVS (Base Model): ' + str([mean_squared_error(y_test, preds), \
							   median_absolute_error(y_test, preds), \
							   r2_score(y_test, preds), \
							   explained_variance_score(y_test, preds)])) 	

# ---------------- Part 1: Use %ile-based feature selection to build the model --

# Create a percentile-based feature selector based on the F-scores. Get top 25% best features by F-test.
selector_f = SelectPercentile(f_regression, percentile=25)
selector_f.fit(x_train, y_train)

# Print the f-scores
for name, score, pv in zip(list(cars), selector_f.scores_, selector_f.pvalues_):
	print('F-score, p-value (' + name + '): ' + str(score) + ',  ' + str(pv))

# Get the columns of the best 25% features.	
xt_train, xt_test = selector_f.transform(x_train), selector_f.transform(x_test)

# Create a least squares linear regression model.
model = linear_model.LinearRegression()

# Fit the model.
model.fit(xt_train, y_train)

# Make predictions on test data and look at the results.
preds = model.predict(xt_test)
pprint.pprint(pd.DataFrame({'Actual':y_test, 'Predicted':preds}))

print('MSE, MAE, R^2, EVS (Top 25% Model): ' + \
							   str([mean_squared_error(y_test, preds), \
							   median_absolute_error(y_test, preds), \
							   r2_score(y_test, preds), \
							   explained_variance_score(y_test, preds)])) 	
						   
						   
# ---------------- Part 2: Use k-best feature selection to build the model --

# Create a top-k feature selector based on the F-scores. Get top 25% best features by F-test.
selector_f = SelectKBest(f_regression, k=3)
selector_f.fit(x_train, y_train)

# Get the columns of the best 25% features.	
xt_train, xt_test = selector_f.transform(x_train), selector_f.transform(x_test)

# Create a least squares linear regression model.
model = linear_model.LinearRegression()

# Fit the model.
model.fit(xt_train, y_train)

# Make predictions on test data and look at the results.
preds = model.predict(xt_test)
pprint.pprint(pd.DataFrame({'Actual':y_test, 'Predicted':preds}))

print('MSE, MAE, R^2, EVS (Top 3 Model): ' + \
							   str([mean_squared_error(y_test, preds), \
							   median_absolute_error(y_test, preds), \
							   r2_score(y_test, preds), \
							   explained_variance_score(y_test, preds)])) 	
						   						   
												   
# ---------------- Part 3: Use Recursive Feature Elimination with Cross Validation -

# Use RFECV to arrive at the approximate best set of predictors. RFECV is a greedy method.
selector_f = RFECV(estimator=linear_model.LinearRegression(), \
                   cv=5, scoring=make_scorer(r2_score))
selector_f.fit(x_train, y_train)

# Get the columns of the best 25% features.	
xt_train, xt_test = selector_f.transform(x_train), selector_f.transform(x_test)

# Create a least squares linear regression model.
model = linear_model.LinearRegression()

# Fit the model.
model.fit(xt_train, y_train)

# Make predictions on test data and look at the results.
preds = model.predict(xt_test)
pprint.pprint(pd.DataFrame({'Actual':y_test, 'Predicted':preds}))

print('MSE, MAE, R^2, EVS (RFECV Model): ' + \
							   str([mean_squared_error(y_test, preds), \
							   median_absolute_error(y_test, preds), \
							   r2_score(y_test, preds), \
							   explained_variance_score(y_test, preds)])) 	