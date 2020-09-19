import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype) # int32

arr = np.array(["apple","banana"])
print(arr.dtype) #<U6

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr) #
print(arr.dtype) 

arr = np.array([1, 2, 3, 4], dtype='i4') # 4bytes
print(arr) # [1 2 3 4]
print(arr.dtype) # int32

# 轉換變數類型為整數
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# 轉換變數類型為布林
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

