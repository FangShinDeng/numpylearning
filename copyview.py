import numpy as np

# copy 用法
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# view 用法
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# base 用法
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()

print(x.base) # None
print(y.base) # [1 2 3 4 5]