# Illustrates an SVM classifier on the glass data.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import tree
from data_util import *

data = pd.read_csv('./data/iris.csv')

print(data.head())

# Select x and y data
features = list(data)
features.remove('Species')
data_x = data[features]
data_y = data['Species']

# Convert the different class labels to unique numbers with label encoding.
le = preprocessing.LabelEncoder()
data_y = le.fit_transform(data_y)

# Split training and test sets from main set.
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.3, random_state = 4)

# Build and evaluate 2 models: one with Gini Impurity criteria and one with Information Gain criteria.
print('----------- DTREE WITH GINI IMPURITY CRITERION ------------------')
dtree_gini_mod = tree.DecisionTreeClassifier(criterion='gini')
dtree_gini_mod.fit(x_train, y_train)
preds_gini = dtree_gini_mod.predict(x_test)
print_multiclass_classif_error_report(y_test, preds_gini)

print('\n----------- DTREE WITH ENTROPY CRITERION -----------------------')
dtree_entropy_mod = tree.DecisionTreeClassifier(criterion='entropy')
dtree_entropy_mod.fit(x_train, y_train)
preds_entropy = dtree_entropy_mod.predict(x_test)
print_multiclass_classif_error_report(y_test, preds_entropy)
