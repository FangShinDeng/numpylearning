import numpy as np

# 基本指定過濾
arr = np.array([1,2,3])
x = [True, True, False]
newarr = arr[x]

print(newarr)

# 過濾出<9以下的數字
arr = np.array([10,9,8,7])
filter_arr = []

for i in arr:
    if i < 9:
        filter_arr.append(True)
        pass
    else: 
        filter_arr.append(False)
        pass
    pass

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# 過濾出基數數字
arr = np.array([11,12,13,14,15,6,7,8,9])
filter_arr = []
for element in arr:
    if element%2 == 1:
        filter_arr.append(True)
        pass
    else:
        filter_arr.append(False)
        pass
    pass

newarr = arr[filter_arr]
print(newarr)

# 直接從數組創建過濾器
arr = np.array([11,12,13,14,15,6,7,8,9])
newarr = arr > 10
print(arr[newarr])