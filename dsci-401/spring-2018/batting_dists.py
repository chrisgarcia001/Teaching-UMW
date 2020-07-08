# This illustrates fitting a polynomial regression case.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score

# Read in data
df = pd.read_csv('./data/batting-angles-distances.csv.')
print(df.head())

# Look at the raw data
#pd.plotting.scatter_matrix(df, diagonal='kde')
#plt.plot(df['Angle'],df['Distance'],'o')
#plt.show()

# Look at linear fit vs. quadratic fit (using seaborn)
pt1 = sns.lmplot(x="Angle", y="Distance", data=df, order=1, ci=None, scatter_kws={"s": 80})
pt2 = sns.lmplot(x="Angle", y="Distance", data=df, order=2, ci=None, scatter_kws={"s": 80})
plt.show()

# Get all non-mpg columns and use as features/predictors.
data_x = df[['Angle']]

# Build a quadratic transform function.
quad = PolynomialFeatures(degree=2)

# Transform the data into quadratic data.
data_x_2 = quad.fit_transform(data_x)

# Get mpg column and use as response variable.
data_y = df['Distance'] 

# ---------- Fit 1: Linear Fit (Order = 1) --------------------------------------------------------
# Split training and test sets from main set. Note: random_state just enables results to be repeated.
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.2, random_state = 4)
linear_mod = linear_model.LinearRegression()

# Fit the model.
linear_mod.fit(x_train,y_train)

# Make predictions on test data and look at the results.
preds = linear_mod.predict(x_test)
#pprint.pprint(pd.DataFrame({'Actual':y_test, 'Predicted':preds}))
print('MSE, MAE, R^2, EVS: ' + str([mean_squared_error(y_test, preds), \
							   median_absolute_error(y_test, preds), \
							   r2_score(y_test, preds), \
							   explained_variance_score(y_test, preds)])) 


# ---------- Fit 2: Quadratic Fit (Order = 2) --------------------------------------------------------
x_train, x_test, y_train, y_test = train_test_split(data_x_2, data_y, test_size = 0.2, random_state = 4)
quad_mod = linear_model.LinearRegression()
quad_mod.fit(x_train,y_train)

# Make predictions on test data and look at the results.
preds = quad_mod.predict(x_test)
#pprint.pprint(pd.DataFrame({'Actual':y_test, 'Predicted':preds}))
print('MSE, MAE, R^2, EVS: ' + str([mean_squared_error(y_test, preds), \
							   median_absolute_error(y_test, preds), \
							   r2_score(y_test, preds), \
							   explained_variance_score(y_test, preds)])) 

