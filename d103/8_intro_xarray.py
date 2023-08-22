# python3 -m pip install xarray
import xarray as xr

# XArray es una librería para la manipulación de arreglos de Numpy y Pandas
# para simplificar el acceso a los datos de las Dimensiones a través de Coordenadas
# Es decir, cada coordena tiene asociado un vector de índices, con los que podemos
# hacer selecciones.

# XArray tiene dos tipos principales el DataArray (~DataFrame) y el DataSet (~Multiple-DataFrames)

# El DataArray se divide en 3 piezas:
# - Data: La matriz de valores asociadas a cada dimensión (n-array)
# - Dims: Los nombres para cada dimensión
# - Coords: Los índices para seleccionar dentro de cada coordenada

data = [
    [23, 24, 32, 38],
    [21, 22, 35, 39],
    [18, 21, 28, 41],
    [15, 22, 33, 37],
    [23, 21, 34, 29],
]

dims = ("FECHA", "CIUDAD")

coords = {
    "FECHA": ["2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01", "2023-06-01"],
    "CIUDAD": ["CDMX", "TOLUCA", "PACHUCA", "MONTERREY"]
}

data_temperaturas = xr.DataArray(data, coords, dims)

print(data_temperaturas)

print("-" * 80)
print(data_temperaturas.sel(FECHA="2023-02-01"))
print("-" * 80)
print(data_temperaturas.sel(CIUDAD="CDMX"))

# Numpy | Pandas
print(data_temperaturas.sel(CIUDAD="CDMX").data)
print(data_temperaturas.sel(CIUDAD="CDMX").data.mean())

print("-" * 80)
print(data_temperaturas.sel(CIUDAD="CDMX", FECHA="2023-05-01").data)
print("-" * 80)
print(data_temperaturas.sel(CIUDAD=["CDMX", "PACHUCA"], FECHA="2023-05-01").data)
print("-" * 80)
print(data_temperaturas.sel(CIUDAD=["CDMX", "PACHUCA"]).to_dataframe(name="TEMPERATURA").T)
print(data_temperaturas.sel(CIUDAD=["CDMX", "PACHUCA"]).to_numpy().T)

#

import pandas as pd

data_analis = pd.DataFrame(data_temperaturas.sel(CIUDAD=["CDMX", "PACHUCA"]).to_numpy().T, index=["CDMX", "PACHUCA"], columns=["2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01", "2023-06-01"])

print(data_analis)

# DataSet - Es una colección de DataArrays con las mismas dimensiones y coordenas

data1 = pd.DataFrame({
    "MONTERREY": [ [34, 85.1, True], [28, 56.1, False] ],
    "CDMX": [ [23, 95.2, True], [21, 76.5, False] ]
})

print(data1)
print(data1["MONTERREY"])
# print(data1["MONTERREY"][:, 0]) # :(

data1.info()

data_temperaturas = xr.DataArray(
    data=[
        [23, 28],
        [19, 27],
        [21, 29],
    ],
    dims=("FECHA", "CIUDAD"),
    coords={
        "FECHA": ["2023-08-01", "2023-08-02", "2023-08-03"],
        "CIUDAD": ["CDMX", "MONTERREY"]
    }
)

data_humedades = xr.DataArray(
    data=[
        [81, 78],
        [56, 81],
        [29, 90],
    ],
    dims=("FECHA", "CIUDAD"),
    coords={
        "FECHA": ["2023-08-01", "2023-08-02", "2023-08-03"],
        "CIUDAD": ["CDMX", "MONTERREY"]
    }
)

data_lluvias = xr.DataArray(
    data=[
        [True, False],
        [True, True],
        [False, True],
    ],
    dims=("FECHA", "CIUDAD"),
    coords={
        "FECHA": ["2023-08-01", "2023-08-02", "2023-08-03"],
        "CIUDAD": ["CDMX", "MONTERREY"]
    }
)

# El DataSet es una colección de DataArrays para manipular de
# forma unificada todos los datos

dataset1 = xr.Dataset({
    "TEMPERATURAS": data_temperaturas,
    "HUMEDADES": data_humedades,
    "LLUVIAS": data_lluvias
})

print(dataset1)
print("=" * 80)
print(dataset1["TEMPERATURAS"])
print("=" * 80)
print(dataset1["HUMEDADES"])
print("=" * 80)
print(dataset1["LLUVIAS"])
print("=" * 80)
print(dataset1.sel(FECHA="2023-08-02", CIUDAD="CDMX"))
print(dataset1.sel(CIUDAD="CDMX"))
print(dataset1.sel(CIUDAD="CDMX").data_vars["TEMPERATURAS"].data)
print(dataset1.sel(CIUDAD="CDMX").data_vars["HUMEDADES"].data)
print(dataset1.sel(CIUDAD="CDMX").data_vars["LLUVIAS"].data)
print("=" * 80)
print(dataset1.sel(CIUDAD="CDMX", FECHA=["2023-08-01", "2023-08-03"]).data_vars["TEMPERATURAS"].data)
print(dataset1.sel(CIUDAD="CDMX", FECHA=["2023-08-01", "2023-08-03"]).data_vars["HUMEDADES"].data)
print(dataset1.sel(CIUDAD="CDMX", FECHA=["2023-08-01", "2023-08-03"]).data_vars["LLUVIAS"].data)
print("=" * 80)
print(dataset1.sel(CIUDAD="CDMX", FECHA=["2023-08-01", "2023-08-03"]).data_vars["TEMPERATURAS"].data.mean())
print(dataset1.sel(CIUDAD="CDMX", FECHA=["2023-08-01", "2023-08-03"]).data_vars["HUMEDADES"].data.max())
print(dataset1.sel(CIUDAD="CDMX", FECHA=["2023-08-01", "2023-08-03"]).data_vars["LLUVIAS"].data.mean())
print("=" * 80)
print(dataset1.sel(CIUDAD=["CDMX", "MONTERREY"], FECHA=["2023-08-01", "2023-08-03"]).data_vars["TEMPERATURAS"].data)
print(dataset1.sel(CIUDAD=["CDMX", "MONTERREY"], FECHA=["2023-08-01", "2023-08-03"]).data_vars["HUMEDADES"].data)
print(dataset1.sel(CIUDAD=["CDMX", "MONTERREY"], FECHA=["2023-08-01", "2023-08-03"]).data_vars["LLUVIAS"].data)

# python3 -m pip install scipy
dataset1.to_netcdf("temperatura_humedad_lluvia.nc") # NetCDF
dataset1.data_vars["TEMPERATURAS"].to_pandas().to_csv("temperaturas.csv") # CSV
dataset1.data_vars["HUMEDADES"].to_pandas().to_csv("humedades.csv") # CSV
dataset1.data_vars["LLUVIAS"].to_pandas().to_csv("lluvias.csv") # CSV

dataset2 = xr.open_dataset("temperatura_humedad_lluvia.nc") # NetCDF

print(dataset2) 

dataset3 = xr.Dataset({
    "TEMPERATURAS": xr.DataArray(pd.read_csv("temperaturas.csv"), dims=("FECHA", "CIUDAD")),
    "HUMEDADES": pd.read_csv("humedades.csv"),
    "LLUVIA": pd.read_csv("lluvias.csv")
})

print(dataset3)