a = -3
b = 3

n = 41

# a + 0d, a + d, a + 2d, a + 3d, ..., b = a * (n - 1) b

# b = a + (n - 1)*d
# d = (b - a) / (n - 1)

d = (b - a) / (n - 1)

x = [a + i * d for i in range(n)] # Lista generada

# x = []
# for i in range(0, n):
#     x.append(a + i * d)

print(x)

from math import cos

y1 = [ cos(xi) for xi in x ] # Lista transformada
# x -> cos(x) -> y

print(y1)

y2 = list(map(lambda xi: cos(xi), x))

print(y2)

import matplotlib.pyplot as plt

plt.plot(x, y1, "ro--")
plt.plot(x, y2, "b*--")

plt.show()