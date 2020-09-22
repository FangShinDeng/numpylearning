import numpy as np

# 使用 np.concatenate 來做合併行為
# 一維合併
arr1 = np.array([1,2,3]) 
arr2 = np.array([4,5,6])
array1 = np.concatenate((arr1,arr2))
print(array1)

# 二維合併
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
array2 = np.concatenate((arr1,arr2), axis=1)
print(array2)

# 使用 Stack 堆疊
arr1 = np.array([1,2,3]) 
arr2 = np.array([4,5,6])
array = np.stack(((arr1),(arr2)))
print(array)

# hstack 延行堆疊
arr1 = np.array([1,2,3]) 
arr2 = np.array([4,5,6])
array = np.hstack(((arr1),(arr2)))
print(array) # [1 2 3 4 5 6]

# vstack 延列堆疊
arr1 = np.array([1,2,3]) 
arr2 = np.array([4,5,6])
array = np.vstack(((arr1),(arr2)))
print(array) 

# dstack 深度堆疊
arr1 = np.array([1,2,3]) 
arr2 = np.array([4,5,6])
array = np.dstack(((arr1),(arr2)))
print(array) 


