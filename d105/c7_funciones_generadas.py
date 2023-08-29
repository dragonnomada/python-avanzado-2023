#
# Las funciones generadas son aquellas 
# que contien la palabra reservada `yield`
#
# Y su propósito es generar valores en forma diferida e iterativa
# Sirven para esperar a que los valores estén listos 
# sin bloquear el procesamiento
#

from time import sleep

def generar_primos(total):
    primos = []

    n = 2

    while len(primos) < total:
        # for-else
        for p in primos:
            if n % p == 0:
                break
        else: # El `else` será ejecutado si el iterador no es roto
            primos.append(n)
            sleep(1)
            # Reporta el siguiente valor aunque la función todavía no termine
            yield n # Sabemos que `n` es el próximo primo
            # Con `yield` reportamos el valor

        n += 1

    return primos

# print(generar_primos(20))

generador1 = generar_primos(5)

p1 = next(generador1)
print("Primo[1]=", p1)
p2 = next(generador1)
print("Primo[2]=", p2)
p3 = next(generador1)
print("Primo[3]=", p3)
p4 = next(generador1)
print("Primo[4]=", p4)
p5 = next(generador1)
print("Primo[5]=", p5)

# Las funciones generadas pueden ser iteradas y cada valor reportado
# retenido en el iterador
for primo in generar_primos(40): # MECANISMO TIPO FEED/XRSS
    print(primo)