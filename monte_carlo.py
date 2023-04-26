import math
import random

r = 2
print(math.pi * r ** 2)

# Метод Монте-Карла
sq = (2*r) ** 2
count = 0
n = 100000
for i in range(n):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    if x ** 2 + y ** 2 <= r ** 2:
        count += 1
sc = sq * count / n
print(sc, count / n)
