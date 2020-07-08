# This illustrates building a regression with categorical features.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score

# Read in data
df = pd.read_csv('./data/election-2000.csv.')
print(df.head())

# Look at the raw data
pd.plotting.scatter_matrix(df, diagonal='kde')

# Get a list of the categorical features for a given dataframe. Move to util file for future use!
def cat_features(dataframe):
	td = pd.DataFrame({'a':[1,2,3], 'b':[1.0, 2.0, 3.0]})
	return filter(lambda x: not(dataframe[x].dtype in [td['a'].dtype, td['b'].dtype]), list(dataframe))

# Get the indices of the categorical features for a given dataframe. Move to util file for future use!	
def cat_feature_inds(dataframe):
	td = pd.DataFrame({'a':[1,2,3], 'b':[1.0, 2.0, 3.0]})
	enums = zip(list(dataframe), range(len(list(dataframe))))
	selected = filter(lambda (name, ind): not(dataframe[name].dtype in [td['a'].dtype, td['b'].dtype]), enums)
	return map(lambda (x, y): y, selected)

print(cat_feature_inds(df))

# Remove the 'State' column - we don't want it.
del df['State']

# Transform the df to a one-hot encoding.
df = pd.get_dummies(df, columns=cat_features(df))

print(df.head())

# Get all non-Bush% columns as features.
features = list(df)
features.remove('Bush%')

# Select x and y data
data_x = df[features]

# Get bush column and use as response variable.
data_y = df['Bush%'] 

# ---------- Create Linear Fit --------------------------------------------------------
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




