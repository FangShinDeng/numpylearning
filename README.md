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
    