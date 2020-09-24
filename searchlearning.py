import numpy as np

arr = np.array([1,2,3,4,5])
x = np.where(arr == 4)
print(x)
print(type(x)) # tuple

# 打印偶數的位置
arr = np.array([1,2,3,4,5])
x = np.where(arr%2 == 0)
print(x)
for i in x:
    print(arr[i])
    pass

# np.searchsorted 打印陣列序數
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,6)
print(x)

# 會依照大小排列出應該補進[2,4,10]的位置
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 10])
print(x)