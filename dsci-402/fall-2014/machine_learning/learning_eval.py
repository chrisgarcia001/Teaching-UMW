from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from cross_val import *

iris_data = datasets.load_iris()

svm_gen = lambda: svm.SVC()
tree_gen = lambda: DecisionTreeClassifier()

splits = random_subsample_splits(iris_data["data"], iris_data["target"], 10, 0.7)

print("Decision Tree Results---------------")
cross_validate(tree_gen, splits)

print("SVM Results-------------------------")
cross_validate(svm_gen, splits)
