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
print("目前維度:" + format(arr.ndim))

# 檢查數組元素
arr = np.array([1,2,3,4,5])
print(arr[0])
print(arr[1])

# 數組元素相加
print(arr[4]+arr[2])

# 2維數組抓取內容，打印資料
arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("調出2維數組資料:",arr3[0, 4])

# 3維數組抓取內容，打印資料
arr4 = np.array([[[1,2,3],[4,5,6]],[[11,22,33],[44,55,66]]])
print("調出3維數組資料:",arr4[0,1,2])

# 負索引
print("從後面調資料",arr4[0,1,-2])