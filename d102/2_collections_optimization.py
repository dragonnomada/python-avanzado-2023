# def generar_puntos(n):
#     puntos = []
#
#     for i in range(n):
#         xi = int(random.gauss(4, 3.2))
#         yi = int(random.gauss(6, 4.2))
#       
#         puntos.append( (xi, yi) )
#
#     return puntos

from random import gauss as g

#
# Genera la función generar_punto que recibe un entero n
# que devuelve una lista generada que dice:
# Coloca una 2-tupla con la llamada a la función g (gass)
# convertida a entero
# -> Para un rango de n valores
# 

# Lista generada: [ <valor-x> for x in seq ]

def generar_puntos(n):
    assert type(n) == int
    return [ ( int(g(20, 4)), int(g(45, 5)) ) for _ in range(n) ]

class Contador:
    conteo = 0
    def inc(self):
        self.conteo += 1
    def dec(self):
        self.conteo -= 1
    def __str__(self) -> str:
        return "C={}".format(self.conteo)

contadores = [Contador()] * 5 # CUIDADO!

print(contadores)
print(list(map(lambda c: c.conteo, contadores)))

contadores[0].inc()

print(list(map(lambda c: c.conteo, contadores)))

contadores = [ Contador() for _ in range(5) ]

print(contadores)
print(list(map(lambda c: c.conteo, contadores)))

contadores[0].inc() # Primer elemento
contadores[4].inc() # Quinto elemento
contadores[4].inc()
# contadores[5].inc() # ERROR: El índice 5 está fuera de rango

print(list(map(lambda c: c.conteo, contadores)))

# map(T, x) -> y = [ T(xi) for xi in x ]

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = list(map(lambda xi: xi ** 2, x))

print(x)
print(y)

print("-" * 40)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [ xi ** 2 for xi in x ]

print(x)
print(y)



