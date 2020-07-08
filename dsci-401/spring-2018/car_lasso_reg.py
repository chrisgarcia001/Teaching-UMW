# This illustrates how to use Lasso regression to handle cases with correlated predictors.
# Lasso minimizes the Objective = RSS + alpha * (sum of absolute value of coefficients)
# When alpha = 0 this is equivalent to ordinary least squsres. 
# By adjusting alpha (> 0) we can try differing coefficient penalties.


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

# Split data into  train/test sets
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.2, random_state = 4)

# ---------------- Part 0: Do a pairs plot to see potential relationships -------
#sm = pd.plotting.scatter_matrix(cars, diagonal='kde')
# plt.tight_layout()
#plt.show()


# ---------------- Part 1: Compare OLS vs. Lasso Regression -----------------------

# Fit the model.
# Create a least squares linear regression model.
base_mod = linear_model.LinearRegression()
base_mod.fit(x_train,y_train)

# Make predictions on test data and look at the results.
preds = base_mod.predict(x_test)
print('R^2 (Base Model): ' + str(r2_score(y_test, preds)))

# Show Lasso regression fits for different alphas.
alphas = [0.0, 0.01, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
for a in alphas:
	# Normalizing transforms all variables to number of standard deviations away from mean.
	lasso_mod = linear_model.Lasso(alpha=a, normalize=True, fit_intercept=True)
	lasso_mod.fit(x_train, y_train)
	preds = lasso_mod.predict(x_test)
	print('R^2 (Lasso Model with alpha=' + str(a) + '): ' + str(r2_score(y_test, preds)))
	
