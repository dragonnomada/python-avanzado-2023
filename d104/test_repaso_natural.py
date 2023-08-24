import numpy as np

x1 = np.random.normal(5, 1, 100_000) # 5.0
x2 = np.random.normal(2, 1, 100_000) # 2.0

d = x1.mean() - x2.mean()

print("Diferencia: {}".format(d))