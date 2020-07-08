from cross_val import *

columns = [range(20), range(20, 40), range(40, 60)]
data = map(list, zip(*columns))
labels = range(60, 80)
#print(data[:5])
#print(random_subsample_splits(data, labels, 2))
print(kfold_splits(data, labels, 4))


