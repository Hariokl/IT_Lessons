#  Метод Монте-Карло
import math
import random

a = 2
r = a / 2
print(math.pi*r**2)

sq = a ** 2
n = 1000
count = 0
for i in range(n):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    if x ** 2 + y ** 2 <= r ** 2:
        count += 1

sc = sq * count / n
print(sc)
