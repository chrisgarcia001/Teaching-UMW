from cross_val import *

columns = [range(20), range(20,40), range(40,60)]
data = map(list, zip(*columns))
labels = range(60,80)

# print(random_subsample_splits(data, labels, 2))
# print("\n\n")
# print(kfold_splits(data, labels, 4))
# print("\n\n")
# print(leave_one_out_splits(data, labels))
 
tp = [1,2,1,2,1,2,1,2,1,2,1]
ta = [1,1,1,1,2,2,1,1,2,2,2]
#print(post_pad("ab", 5) + "c")
confusion_matrix(tp, ta)