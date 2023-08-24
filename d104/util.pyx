def contar_multiplos_3(n):
    contador = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            contador += 1
    return contador