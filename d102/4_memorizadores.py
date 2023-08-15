# Un memorizador permite mantener en caché/memoria
# el resultado de una función cuándo es llamada con los mismos parámetros
# es decir, guarda el resultado para llamada a la función
# bajo los mismos parámetros (y supone que el resultado no varia)
# Ejemplo, f(a, b) -> ... c | f(a, b) -> c

from functools import lru_cache

@lru_cache # Decoramos la función fibo, para que guarde caché/memorice automáticamente
def fibo(n):
    print(f"Calculando el número de fibonacci ({n})...")
    if n <= 1:
        print(f"fibo({n}) = 1")
        return 1
    r = fibo(n - 1) + fibo(n - 2)
    print(f"fibo({n}) = {r}")
    return r

fibo(20)
fibo(20)