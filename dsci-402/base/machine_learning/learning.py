from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from cross_val import *

iris_data = datasets.load_iris()

svm_gen = lambda: svm.SVC()
tree_gen = lambda: DecisionTreeClassifier()

kfold_data = kfold_splits(iris_data["data"], iris_data["target"], 5)

print("----Decision Tree Classifier Results----")
cross_validate(tree_gen, kfold_data)

print("----SVM Results----")
cross_validate(svm_gen, kfold_data)
