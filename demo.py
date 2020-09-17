import numpy as np

arr = np.array([1,2,3,4,5])
arr2 = [1,2,3,4,5]
print(arr) # [1 2 3 4 5]
print(arr2) # [1,2,3,4,5]

print(type(arr)) # <class 'numpy.ndarray'>
print(type(arr2)) # <class 'list'>

print(np.__version__) # 1.19.2



# 0維度
arr1 = np.array(42)
print(arr1)

# 1維度
arr2 = np.array([1,2,3,4,5])
print(arr2)

# 2維度
arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr3)

# 3維度
arr4 = np.array([[[1,2,3],[4,5,6]],[[11,22,33],[44,55,66]],[[1,2,3],[4,5,6]],[[11,22,33],[44,55,66]]])
print(arr4)

# 檢查多少維度
print(arr1.ndim) # 0 
print(arr2.ndim) # 1
print(arr3.ndim) # 2
print(arr4.ndim) # 3

# 高維度數組
arr = np.array([1,2,3,4], ndmin = 5)
print(arr)
print(arr.ndim)