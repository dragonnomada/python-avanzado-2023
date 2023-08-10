#
# Podemos usar `python3 -m cProfile c5_benchmarks_simulador.py`
#

def calcular_primos(total):
    primos = []

    n = 2

    while len(primos) < total:
        esPrimo = True
        for p in primos:
            if n % p == 0:
                esPrimo = False

        if esPrimo:
            primos.append(n)

        n += 1

    return primos

calcular_primos(1_000)