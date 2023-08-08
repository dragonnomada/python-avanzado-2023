# Colecciones

## Listas
frutas = ["Manaza", "Mango", "Kiwi", "Fresa"]

frutas.append("Guayaba")
frutas.insert(0, "Melón")

for fruta in frutas:
    print(f"{fruta} - {len(fruta)}")

frutas.pop(3) # Kiwi
frutas.pop() # Melón

print(frutas)

## Tuplas

puntos = [
    (23.4, -16.8),
    (34.5, 67.8),
    (23.4, 32.1),
    (13.24, 14.23),
    (56.78, 76.54),
    (-89.01, 10.98),
]

for x, y in puntos:
    print(x, y, x + y)

nombres = ["Ana", "Beto", "Carlos"]
edades = [23, 45, 67]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} ({edad} años)")