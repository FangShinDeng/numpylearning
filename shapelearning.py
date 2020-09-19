import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) # 打印元素及數組數量

arr1 = np.array([[1,2],[3,4],[5,6]])


print(arr.shape)
print(arr1.shape)

arr = np.array([1,2,3,4,5,6,7,8,9])
newarr = arr.reshape(3,3)

print(newarr)
print(newarr.shape)
print(newarr.base)