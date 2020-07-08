from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from cross_val import *

iris_data = datasets.load_iris()

#print(iris_data)

split = random_subsample_splits(iris_data["data"], iris_data["target"], 1, 0.7)[0]
#print(split)

train_data = split["train_data"]
test_data = split["test_data"]
train_labels = split["train_labels"]
test_labels = split["test_labels"]

print("Decision Tree Classifier----------------")
tree_mod = DecisionTreeClassifier().fit(train_data, train_labels)
predicted = list(tree_mod.predict(test_data))
actual = test_labels
print("Predicted: " + str(predicted))
print("Actual     " + str(actual))

print("SVM Classifier----------------")
svm_mod = svm.SVC().fit(train_data, train_labels)
predicted = list(svm_mod.predict(test_data))
actual = test_labels
print("Predicted: " + str(predicted))
print("Actual     " + str(actual))