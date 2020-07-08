# Illustrates k-nearest neighbors on the web purchases data.

import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix

data = pd.read_csv('./data/website-purchases.csv')

# Get predictors - all non-Buy columns (Buy is column 0).
data_x = data[list(data[1:])]

# Get Buy column and use as response variable.
data_y = data['Buy'] 

# Split training and test sets from main set. Note: random_state just enables results to be repeated.
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.3, random_state = 4)

# Build a sequence of models for k = 2, 4, 6, 8, ..., 20.
ks = [2, 3, 6, 8, 10, 12, 14, 16, 18, 20]
for k in ks:
	# Create model and fit.
	mod = neighbors.KNeighborsClassifier(n_neighbors=k)
	mod.fit(x_train, y_train)

	# Make predictions - both class labels and predicted probabilities.
	preds = mod.predict(x_test)
	print('---------- EVALUATING MODEL: k = ' + str(k) + ' -------------------')
	# Look at results.
	print('Accuracy: ' + str(accuracy_score(y_test, preds)))
	print('Precison: ' + str(precision_score(y_test, preds)))
	print('Recall: ' + str(recall_score(y_test, preds)))
	print('F1: ' + str(f1_score(y_test, preds)))
	print('ROC AUC: ' + str(roc_auc_score(y_test, preds)))
	print("Confusion Matrix:\n" + str(confusion_matrix(y_test, preds)))

