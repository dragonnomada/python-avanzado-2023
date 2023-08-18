import pandas as pd

d1 = pd.read_csv("../datasets/spotify_top_200.csv", sep=";")

d1.info()

columns = list(d1.columns)

columns = columns[:11] + [columns[14]] # Las primeras 11 más la 14 (15va)

print(columns)

# d1 = d1[ ["Rank", "Title", "Nationality"] ] # Enmascarar las columnas

d1 = d1[ columns ] # Filtramos las columnas de análisis

print(d1.head(5))
print(d1.tail(5))
print(d1.sample(5))

nationalities = d1["Nationality"] # Recupera la serie asociada a la columna

print(nationalities.unique())

# Los predicados son comparaciones lógicas que aplicamos a una columna
# Por ejemplo, SERIE == VALOR | SERIE > VALOR | SERIE <= VALOR
# Produce una serie con valores True o False que se considera
# Una máscada para el DataFrame
# Es decir, DATAFRAME[ SERIE_MÁSCARA_LÓGICA ] -> SUB_DATAFRAME
# * Nota: Una columna del DataFrame equivale a una Serie
esDeMexico = d1["Nationality"] == "Mexico"

print(esDeMexico)

esBailable = d1["Danceability"] >= 0.8

print(esBailable)

# esDeMexicoYBailable = (d1["Nationality"] == "Mexico") & (d1["Danceability"] >= 0.8)
esDeMexicoYBailable = esDeMexico & esBailable

d1_mexico = d1[ esDeMexico ]
d1_bailables = d1[ esBailable ]
d1_mexico_bailable = d1[ esDeMexicoYBailable ]

print("% Mexicana: {:.1f}".format(esDeMexico.mean() * 100))
print("% Bailable: {:.1f}".format(esBailable.mean() * 100))
print("% Mexicana y Bailable: {:.1f}".format(esDeMexicoYBailable.sum() / esDeMexico.sum() * 100))

# print(d1[ d1["Nationality"] == "Mexico" ])

report1 = d1[ ["Danceability", "Nationality"] ].groupby("Nationality").mean()

print(report1)

report1.to_csv("../datasets/report1_spotify.csv")