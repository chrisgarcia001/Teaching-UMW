# Illustrates different ML testing & optimization methods on the glass data.

import pandas as pd
from sklearn import linear_model
from sklearn import svm 
from sklearn import naive_bayes
from sklearn import ensemble 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV


data = pd.read_csv('./data/glass.csv')

# Get features and response data.
features = list(data)
features.remove('Type')
data_x = data[features]
data_y = data['Type']

# Create training and test sets for later use.
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.3, random_state = 4)

# ----- PART 1: Basic Cross Validation with SVM --------
mod = svm.SVC(C=2.5)

# Illustrate the 3 major CV approaches. We will use accuracy or F1 macro as our scoring criteria in examples below.
# For a list of all premade scoring criteria see http://scikit-learn.org/stable/modules/model_evaluation.html
k_fold = KFold(n_splits=5, shuffle=True, random_state=4) # Shuffling is needed since classes are ordered.
k_fold_scores = cross_val_score(mod, data_x, data_y, scoring='f1_macro', cv=k_fold)
print('CV Scores (K-Fold): ' + str(k_fold_scores))

loo = LeaveOneOut() 
loo_scores = cross_val_score(mod, data_x, data_y, cv=loo) # Use accuracy scoring (default) since each test case has one element.
print('CV Scores (Avg. of Leave-One-Out): ' + str(loo_scores.mean()))

shuffle_split = ShuffleSplit(test_size=0.2, train_size=0.8, n_splits=5)
ss_scores = cross_val_score(mod, data_x, data_y, scoring='accuracy', cv=shuffle_split)
print('CV Scores (Shuffle-Split): ' + str(ss_scores))

# ----- PART 2: Grid Search + Cross Validation with RF --------
# Optimize a RF classifier and test with grid search.

# Below - notice that n_estimators and max_depth are both params of RF. This is how we specify params with different values to try.
param_grid = {'n_estimators':[5, 10, 50, 100], 'max_depth':[3, 6, None]} 

# Find the best RF and use that. Do a 5-fold CV and score with f1 macro.
optimized_rf = GridSearchCV(ensemble.RandomForestClassifier(), param_grid, cv=5, scoring='f1_macro') 

optimized_rf.fit(x_train, y_train) # Fit the optimized RF just like it is a single model - it essentially is!

print('Grid Search Test Score (Random Forest): ' + str(optimized_rf.score(x_test, y_test)))


# --- PART 3: Model ensemble illustrations ---------------------
# Here is a Bagging classifier that builds many SVM's.
bagging_mod = ensemble.BaggingClassifier(linear_model.LogisticRegression(), n_estimators=200)
k_fold = KFold(n_splits=5, shuffle=True, random_state=4) # Shuffling is needed since classes are ordered.
bagging_mod_scores = cross_val_score(bagging_mod, data_x, data_y, scoring='f1_macro', cv=k_fold)
print('CV Scores (Bagging NB) ' + str(bagging_mod_scores))

# Here is a basic voting classifier with CV and Grid Search.
m1 = svm.SVC()
m2 = ensemble.RandomForestClassifier()
m3 = naive_bayes.GaussianNB()
voting_mod = ensemble.VotingClassifier(estimators=[('svm', m1), ('rf', m2), ('nb', m3)], voting='hard')

# Set up params for combined Grid Search on the voting model. Notice the convention for specifying 
# parameters foreach of the different models.
param_grid = {'svm__C':[0.2, 0.5, 1.0, 2.0, 5.0, 10.0], 'rf__n_estimators':[5, 10, 50, 100], 'rf__max_depth': [3, 6, None]}
best_voting_mod = GridSearchCV(estimator=voting_mod, param_grid=param_grid, cv=5)
best_voting_mod.fit(x_train, y_train)
print('Voting Ensemble Model Test Score: ' + str(best_voting_mod.score(x_test, y_test)))



