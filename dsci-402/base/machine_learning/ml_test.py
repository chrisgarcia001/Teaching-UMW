from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from cross_val import *

iris_data = datasets.load_iris()

svm_gen = lambda: svm.SVC()
tree_gen = lambda: DecisionTreeClassifier()

split = random_subsample_splits(iris_data["data"], iris_data["target"], 1)[0]
#print(split)
train_data = split["train_data"]
test_data = split["test_data"]
train_labels = split["train_labels"]
test_labels = split["test_labels"]

print("Decision Tree Classifier-----")
tree_mod = DecisionTreeClassifier().fit(train_data, train_labels)
predicted = tree_mod.predict(test_data)
actual = test_labels
print("Predicted: " + str(list(predicted)))
print("Actual:    " + str(actual))


print("SVM Classifier-----")
svm_mod = svm.SVC().fit(train_data, train_labels)
predicted = svm_mod.predict(test_data)
actual = test_labels
print("Predicted: " + str(list(predicted)))
print("Actual:    " + str(actual))

