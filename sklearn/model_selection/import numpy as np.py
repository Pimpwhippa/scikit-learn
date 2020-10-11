import numpy as np
from sklearn.model_selection import GroupTimeSeriesSplit
groups = ['a' ,'a' ,'a' ,'b','b' , 'b','c' ,'c' ,'c' ,'d' ,'d' ,'d']
n_samples = len(groups)
n_samples = _num_samples(X)

X = y = np.ones(n_samples)
gtss = GroupTimeSeriesSplit(n_splits=3)
for train_index, test_index in gtss.split(X, y, groups):
    print("TRAIN:", train_index, "TEST:", test_index)

groups = np.array(['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd'])
