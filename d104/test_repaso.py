from repaso import diff_means

import numpy as np

x1 = np.random.normal(5, 1, 100_000) # 5.0
x2 = np.random.normal(2, 1, 100_000) # 2.0

d = diff_means(x1, x2)

print("Diferencia: {}".format(d))