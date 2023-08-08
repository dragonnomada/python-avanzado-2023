f = lambda x: 2 * x + 1

print(f(5))
print(f(1))
print(f(100))

def ordenar_lista(lista):
    lista = lista[:]


    lista_ordenada = []

    while len(lista) > 0:
        x = min(lista)
        xi = lista.index(x)

        lista.pop(xi)
        lista_ordenada.append(x)

    return lista_ordenada

print(ordenar_lista([2, 4, 3, 5, 6, 2, 7, 8, 5]))