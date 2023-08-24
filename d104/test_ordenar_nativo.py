from mylib_nativo import ordernar_lista

lista = [1, 2, 3, 9, 8, 7, 4, 5, 6, 3, 2, 1]

ultima_lista_ordenada = None

for _ in range(1_000_000):
    ultima_lista_ordenada = ordernar_lista(lista)

print(ultima_lista_ordenada)