import numpy as np

arr = np.array([1,2,3,4,5])

newarr = np.array_split(arr,4)

print(newarr) # [array([1, 2]), array([3]), array([4]), array([5])]
print(newarr[0]) # [1 2]

