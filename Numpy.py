# numpy: entire array, different from list.
# a new kind of pyhton type, like float.
import numpy as np
height = np.array([1, 2, 3, 4, 5])
print(type(height))
weight = np.array([1, 2, 3, 4, 5])
print(type(weight))
sum = height + weight
print(sum)
#type coercion: change different data type to
np.array([True, 1, 2]) + np.array([3, 4, False])
# same as
np.array([4, 3, 0]) + np.array([0, 2, 2])


# create 2d, can be seen as list of list
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                [65.4, 59.2, 63.6, 88.4, 68.7]])
# change 1 float to string, all of the elements will change too
np_2d_string = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                [65.4, 59.2, 63.6, 88.4, "68.7"]])
# use print(), if not, just print last one.
print(type(np_2d_string))
# select one row
print(np_2d[1])
print(np_2d[0][3])# or [0, 3]
# select the same family both  
print(np_2d[:, 1:3])
## conda: means select all rows or cols
print(np_2d[:, 0])


# basic statistics
np.mean(np[:,0])
np.median(np[:,0])
np.corrcoef(np_city[:,0], np_city[:,1])
np.std(np_city[:,0])

# generate data
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))

# Heights of the goalkeepers use []
gk_heights = np_heights[np_positions == "GK"]
