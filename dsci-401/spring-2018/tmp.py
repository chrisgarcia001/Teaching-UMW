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
print(df.get_dummies().head())

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

# Create a label encoder.
le = LabelEncoder()


# Create a one-hot encoder to transform categorical variables.
enc = OneHotEncoder(categorical_features=[0, 6]) # Bad way.
enc = OneHotEncoder(categorical_features=cat_feature_inds(df)) # Better generic way - detect categorical features.

# Fit the encoders - first go through the label encoder then the one-hot encoder.
cat_inds = cat_feature_inds(df)

enc.fit(df.as_matrix())
