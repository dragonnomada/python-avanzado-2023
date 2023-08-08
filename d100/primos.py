primos = []

n = 2

while len(primos) < 100:
    # Determinar si n es un número primo
    # agregar n a la lista de primos

    esPrimo = True

    for p in primos:
        if n % p == 0:
            esPrimo = False
    
    if esPrimo:
        primos.append(n)

    n += 1

print(primos)