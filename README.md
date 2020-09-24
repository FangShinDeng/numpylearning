# Numpy 練習之路
    一樣先採用w3c的教學，參考路徑: https://www.w3schools.com/python/numpy_intro.asp
    
## 為何要用Numpy?
    其實Numpy最主要就是跟List做比較，Numpy的處理速度比Python List快很多，具體請找原理去學習其中奧秘，本篇直接先學習使用哦！

## 維度練習
    1. 創建不同維度的np.ndarray
    2. 檢查array維度
    3. 直接指定array維度
    4. 打印數組中指定元素

## 切片練習
    與List相同，只是搭配了多維數組的概念，指定區間及取值間隔都是一樣的

## 變數類型
    使用arr.dtype來查看類型, 轉換變數類型
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )

# copy and view 使用及修改
    x = arr.view
    x = arr.copy

# shape, reshape
    arr.shape 打印幾組元素，每組元素的數量
    注意使用時，後者一定要是相同數組數量的，不能[1,2],[1,2,3]，只能[1,2],[1,2]
    
    reshape 重塑數組, 將原本的數組重配

# Iterating 迭代
    使用 nditer 來直接打印不同維度的資料
    使用 ndenumerate 來加入索引

# Join 數組合併
    使用 concatenate 合併數組
    使用 stack, hstack, vstack, dstack 堆疊數組

# Split 數組拆分
    使用 split 來拆分數組，在依照拆分數組個別處理

# Search
    使用where, searchsorted來搜索出特定位置

# Sort 排列