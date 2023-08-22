# Numpy - Big-O o(n)
# Listas - Big-O o(n^2)

a = [1, 2, 3, 4, 5]

import numpy as np

x = np.zeros(3_000)
# x = [0 for _ in range(3_000)]

print(x)

x = np.linspace(-np.pi, np.pi, 100) # arreglo 1-D (100)
y1 = np.cos(x) # Arreglo 1-D (100)
y2 = np.sin(x)
y3 = np.tan(x)

# import matplotlib.pyplot as plt

# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)

# plt.ylim(-1, 1)

# plt.show()

import pandas as pd

data1 = pd.DataFrame({
    "X": x,   # X: [-3.14, ..., 3.14]
    "Y1": y1, # Y1: [-1, ..., -1]
    "Y2": y2, # Y2: [-0, ...,  +0]
    "Y3": y3  # Y3: [+0, ..., -0]
})

print(data1)

# Numpy: Acceso a los datos y la dimensionalidad

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(A) # 2-D (3, 3)

print(A[0]) # 1-D (3)

print(A[:, 0]) # 1-D (3)
print(A[:, 1]) # 1-D (3)
print(A[:, 2]) # 1-D (3)

B = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(B) # 2-D (2, 4)

print(B[0]) # 1-D (4)
print(B[1]) # 1-D (4)

print(B[:, 0]) # 1-D (2)
print(B[:, 1]) # 1-D (2)
print(B[:, 2]) # 1-D (2)
print(B[:, 3]) # 1-D (2)

print(B.shape)

C = np.array([
    [ [1, 2], [3, 4], [5, 6] ],
    [ [7, 8], [9, 0], [0, 1] ]
])

print(C) # 3-D (2, 3, 2)

print(C.ndim) # 3
print(C.shape) # (2, 3, 2)

print(C[1, 1]) # [9, 0]
print(C[1, 1, 0]) # 9

print(C[:, 1, 0]) # [3, 9]
print(C[:, 2, 1]) # [6, 1]

print(C[:, :, 1]) # [ [2, 4, 6], [8, 0, 1] ]

# PANDAS -> 2D (DataFrame)

# 2-EJES (FECHA, CIUDAD)

temperaturas = np.array([
    [38, 32, 40],
    [35, 33, 35],
    [36, 39, 38],
])

print(temperaturas[0].mean()) # 36.6666...
print(temperaturas[1].mean()) # 34.3333...
print(temperaturas[2].mean()) # 37.6666...

print(temperaturas[:, 0].mean()) # 36.3333...
print(temperaturas[:, 1].mean()) # 34.6666...
print(temperaturas[:, 2].mean()) # 37.6666...

data_temperaturas = pd.DataFrame({
    "ACAPULCO": [38, 35, 36],
    "CD_JUAREZ": [32, 33, 39],
    "MONTERREY": [40, 35, 38]
}, index=["2023-01-01", "2023-01-02", "2023-01-03"])

print(data_temperaturas)

print(data_temperaturas["ACAPULCO"]) # [38, 35, 36] (Formato de Series de Pandas)

print(data_temperaturas["ACAPULCO"].mean()) # 36.3333...
print(data_temperaturas["CD_JUAREZ"].mean()) # 34.6666...
print(data_temperaturas["MONTERREY"].mean()) # 37.6666...

print(data_temperaturas.T)
print(data_temperaturas.T["2023-01-01"].values) # [38, 32, 40]
print(data_temperaturas.T["2023-01-01"].mean()) # 36.6666...
print(data_temperaturas.T["2023-01-02"].mean()) # 34.3333...
print(data_temperaturas.T["2023-01-03"].mean()) # 37.6666...

print(data_temperaturas["ACAPULCO"].quantile(0.05))
print(data_temperaturas["ACAPULCO"].quantile(0.25))
print(data_temperaturas["ACAPULCO"].quantile(0.50))
print(data_temperaturas["ACAPULCO"].quantile(0.75))
print(data_temperaturas["ACAPULCO"].quantile(0.95))

import seaborn as sns
import matplotlib.pyplot as plt

# sns.boxplot(data_temperaturas)

# plt.show()

# sns.boxplot(data_temperaturas.T)

# plt.show()

# sns.kdeplot(data_temperaturas)
# sns.pairplot(data_temperaturas)

# plt.show()

data_temperaturas = pd.DataFrame({
    "ACAPULCO": [38, 35, 36],
    "CD_JUAREZ": [32, 33, 39],
    "MONTERREY": [40, 35, 38]
})

# sns.jointplot(data_temperaturas, kind='scatter')
# sns.jointplot(data_temperaturas, kind='hex')
# sns.jointplot(data_temperaturas, kind='kde')

plt.show()


