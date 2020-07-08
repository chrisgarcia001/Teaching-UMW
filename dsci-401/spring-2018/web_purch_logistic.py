# Illustrates 2-class logistic regression.

import pandas as pd
from sklearn import linear_model
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

# Build the model.
log_mod = linear_model.LogisticRegression()
log_mod.fit(x_train, y_train)

# Make predictions - both class labels and predicted probabilities.
preds = log_mod.predict(x_test)
pred_probs = log_mod.predict_proba(x_test)
prob_pos = pred_probs.transpose()[1]  # P(X = 1) is column 1
prob_neg = pred_probs.transpose()[0]  # P(X = 0) is column 0

#print(pred_probs)

# Look at results.
pred_df = pd.DataFrame({'Actual':y_test, 'Predicted Class':preds, 'P(1)':prob_pos, 'P(0)':prob_neg})
print(pred_df.head(15))
print('Accuracy: ' + str(accuracy_score(y_test, preds)))
print('Precison: ' + str(precision_score(y_test, preds)))
print('Recall: ' + str(recall_score(y_test, preds)))
print('F1: ' + str(f1_score(y_test, preds)))
print('ROC AUC: ' + str(roc_auc_score(y_test, preds)))
print("Confusion Matrix:\n" + str(confusion_matrix(y_test, preds)))

