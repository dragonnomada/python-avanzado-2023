def ordernar_lista(lista):
    lista = lista[:] # Copiamos la lista 

    lista_2 = []
    while len(lista) > 0:
        x = min(lista)
        lista_2.append(x)
        lista.remove(x)
    return lista_2