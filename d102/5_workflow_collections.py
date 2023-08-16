# Flujo tracional

calificaciones = [8.9, 5.7, 7.8, 9.2, 7.9, 10.0, 9.2, 8.1, 6.7, 7.8]
edades = [23, 25, 27, 34, 32, 20, 29, 18, 26, 28]

# Modelo: I = ((c - cp)^2 + 1) / ((e - ep)^2 + 1)

# sum = 0
# total = 0
# for calif in calificaciones:
#   sum += calif
#   total += 1

cp = sum(calificaciones) / len(calificaciones)

ep = sum(edades) / len(edades)

calificaciones_dif = [(c - cp) ** 2 + 1 for c in calificaciones]
# calificaciones_dif = list(map(lambda c: (c - cp) ** 2 + 1, calificaciones))
# calificaciones_dif = []
# for c in calificaciones:
#     calificaciones_dif.append((c - cp) ** 2 + 1)

print(calificaciones_dif)

edades_dif = [(e - ep) ** 2 + 1 for e in edades]

print(edades_dif)

y = []

for i in range(len(calificaciones)):
    ci = calificaciones_dif[i]
    ei = edades_dif[i]
    y.append(ci / ei)

print(y)

# ================================================

calificaciones = [8.9, 5.7, 7.8, 9.2, 7.9, 10.0, 9.2, 8.1, 6.7, 7.8]
edades = [23, 25, 27, 34, 32, 20, 29, 18, 26, 28]

def modelo(calificacion, edad):
    # La función marca el uso de variables globales externas 
    # al cuerpo de la función, las cuales deben estar
    # previamente definidas
    global calificacion_prom, edad_prom
    return ((calificacion - calificacion_prom) ** 2 + 1) / ((edad - edad_prom) ** 2 + 1)

calificacion_prom = sum(calificaciones) / len(calificaciones)
edad_prom = sum(edades) / len(edades)

y = [ modelo(calificacion, edad) \
        for calificacion, edad in zip(calificaciones, edades) ]

print(y)

# ================================================

cc = [8.9, 5.7, 7.8, 9.2, 7.9, 10.0, 9.2, 8.1, 6.7, 7.8]
ee = [23, 25, 27, 34, 32, 20, 29, 18, 26, 28]

y = [ ((c - sum(cc) / len(cc)) ** 2 + 1) / ((e - sum(ee) / len(ee)) ** 2 + 1) \
        for c, e in zip(cc, ee) ]

print(y)
