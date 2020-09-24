from numpy import random

# 100中的隨機亂數
x = random.randint(100)
print(x)

# 0~1的隨機浮點數
x = random.rand()
print(x)

# 隨機數組
x = random.randint(100, size=(3))
print(x)

# 隨機指定維數及數量的數組
x = random.randint(100, size=(3,5))
print(x)

# 建立兩組隨機浮點數
x = random.rand(2)
print(x)

# 隨機指定數 choice
x = random.choice([3,4,5,6])
print(x)

# 隨機指定維度及數量數組
x = random.choice([3,4,5,6], size=(3,5))
print(x)