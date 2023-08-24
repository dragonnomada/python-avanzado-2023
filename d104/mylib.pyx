# def ordernar_lista(lista):
#     lista = lista[:] # Copiamos la lista 
#     lista_2 = []
#     while len(lista) > 0:
#         x = min(lista)
#         lista_2.append(x)
#         lista.remove(x)
#     return lista_2

# La instrucción `cdef` nos permite inyectar
# declaraciones nativas de C al momento de
# la transformación, sirve para declarar variables
# nativas y funciones nativas

from libc.stdlib cimport malloc

cdef int[:] ordenar_lista(int[:] lista, int n):
    lista = lista[:]
    cdef int* lista_2 = <int*>malloc(n * sizeof(int))
    cdef int j = 0
    cdef int x = 0
    while len(lista) > 0:
        x = min(lista)
        lista_2[j] = x
        j += 1
        lista.remove(x)
    cdef int[:] sorted_lista = <int[:n]>lista_2
    return sorted_lista

# ~3.5s -> ~3.2s -> ~0.9s