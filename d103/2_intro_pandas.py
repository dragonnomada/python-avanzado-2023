#
# Pandas es una librería especializada basada en numpy para
# manipular Series y DataFrames.
#

# python3 -m pip install pandas
import pandas as pd

# Series de datos
# Una serie equivale a un vector 1-D de datos
# Las series soportan algunas cosas adicionales en los métodos
# útiles como en numpy y las operaciones clásicas (+, -, *, /, **, ...)

import numpy as np

# s1 = pd.Series([1., 2, 3, 4, 5])
# s1 = pd.Series([1, 2, 3, 4, 5], index=["A", "B", "C", "D", "E"])
s1 = pd.Series([1., 2, 3, 4, 5], dtype=np.float16)

s1.name = "Calificaciones"

print(s1)

s1 = pd.Series([1.78, 1.83, 1.56, 1.52, 1.69, 1.68, 1.49], name="ALTURA")
s2 = pd.Series([84, 98, 62, 63, 67, 80, 35], name="PESO")

# python3 -m pip install seaborn
import seaborn as sns # Librería mejorada de matplotlib
import matplotlib.pyplot as plt

# Grafica comenta para no detener el programa
#sns.scatterplot(x=s1, y=s2)
#plt.show()

# Correlación de Pearson:
# +1 - Correlación directa SUBE-SUBE
# ~0 - Correlación nula (no es explicativo)
# -1 - Correlación inversa SUBE-BAJA (BAJA-SUBE)
print(s1.corr(s2))

# Como una fórmula de Excel: Creamos una nueva serie a partir de otras
s3 = s2 / s1 ** 2 # Dividimos cada elemento de s2 entre cada elemento de s1 ** 2
print(s3)

# Ejemplo para calcular la desviación estándar de s1

# Aplicando una transformación directa de arreglos
# s1 -> es en fondo un arreglo
# s1 resta a cada elemento el promedio de la serie s1
# s1.mean() es un escalar que representa el promedio de todos los elementos de s1
# s1 - s1.mean() | A cada elemento de la serie s1 resta el escalar s1.mean()
# Lo anterior produce otra serie (la serie desplazada por la media)
# t2 ~= s1 - s1.mean() | s2 ** 2 -> A cada elemento de la serie desplazada por la media, 
#                                   elevalo al cuadrado
# t3 ~= t2 ** 2 | t3.sum() -> Suma todos los elementos de la serie de los elementos 
#                             desplazados por la media, elevados al cuadrado
# t4 ~= t3 / s1.size -> Obtenemos el arreglo de la varianza (suma de los elementos 
#                       desplazados por la media elevados al cuadro 
#                       entre el número de elementos)
# t5 ~= t4 ** 1/2 -> La raíz cuadrada de la varianza
ds1 = (((s1 - s1.mean()) ** 2).sum() / (s1.size - 1)) ** 0.5

print(ds1)
print(s1.std()) # Tipo Student (Quitando un grado de libertad)

# DataFrame
# Es un conjunto de series que representan una tabla
# Por ejemplo, como en una hoja de cálculo podemos tener
# múltiples columnas, el DataFrame consistiría en múltiples
# Series unidas y nombradas, que representan una tabla
# o conjunto de datos etiquetados.

df1 = pd.DataFrame({
    "A": [1.78, 1.67, 1.98],
    "B": [79.5, 68.9, 102.4]
})

print(df1)

s1 = df1["A"] # Cada columna equivale a una serie
s2 = df1["B"]

s3 = s2 / s1 ** 2

df1["C"] = s3

print(df1)

# Pandas nos permite cargar los DataFrames desde:
# - Archivos CSV
# - Archivos EXCEL
# - Archivos JSON
# - Consultas SQL
# - ...

# También podemos exportar los resultados de un DataFrame
# en formatos inversos, por ejemplo, guardar un CSV, Excel, JSON, SQL, ...

