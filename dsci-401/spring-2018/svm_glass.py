# Illustrates a support vector machine (SVM) classifier on the glass data.

import pandas as pd
from sklearn import svm 
from sklearn.model_selection import train_test_split
from data_util import *

data = pd.read_csv('./data/glass.csv')

# Get features and response data.
features = list(data)
features.remove('Type')
data_x = data[features]
data_y = data['Type']

# Split training and test sets from main set. Note: random_state just enables results to be repeated.
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.3, random_state = 4)

# Build a sequence of models for different n_est and depth values. **NOTE: c=1.0 is equivalent to the default.
cs = [0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
for c in cs:
	# Create model and fit.
	mod = svm.SVC(C=c)
	mod.fit(x_train, y_train)

	# Make predictions - both class labels and predicted probabilities.
	preds = mod.predict(x_test)
	print('---------- EVALUATING MODEL: C = ' + str(c) + ' -------------------')
	# Look at results.
	print_multiclass_classif_error_report(y_test, preds)

