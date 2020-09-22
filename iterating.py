import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

for i in arr:
    print(i)
    pass

for i in arr:
    print(i)
    if i == 5:
        break
    pass

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

for i in arr:
    print(i)
    pass


for i in arr:
    for j in i:
        print(j)
        pass
    pass

for i in np.nditer(arr): # 使用nditer來直接打印不同維度的資料
    print(i) 
    pass

print("間隔")
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for i in np.nditer(arr): # 使用nditer來直接打印不同維度的資料
    print(i) 
    pass

# 使用 ndenumerate() 來加入索引
arr = np.array([[1,2,3,4],[5,6,7,8]])
for idx, i in np.ndenumerate(arr):
    print(idx, i)
    pass