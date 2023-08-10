#
# Las pruebas de fiabilidad/aseguramiento están enfocadas
# en determinar si una condición se cumple o no
# mediante `assert <condición>`, si True el código pasará y continuará
# pero si es False, el código se dentrá y marcará un error
#

from c2_simulador import Robot

r1 = Robot()

# print(r1)

# assert r1.x == 0
# assert r1.y == 0
# assert r1.d == 0

# r1.avanzar()

# print(r1)

# assert r1.x == 0
# assert r1.y == 1
# assert r1.d == 0

r1.avanzar() # 0, 1
r1.avanzar() # 0, 2
r1.girar_derecha()
r1.avanzar() # 1, 2
r1.avanzar() # 2, 2
r1.girar_izquierda()
r1.avanzar() # 2, 3
r1.girar_izquierda()
r1.avanzar() # 1, 3
r1.girar_derecha()
r1.avanzar() # 1, 4
r1.avanzar() # 1, 5
r1.avanzar() # 1, 6
r1.girar_izquierda()
r1.avanzar() # 2, 6
r1.avanzar() # 3, 6
r1.avanzar() # 4, 6
r1.avanzar() # 5, 6
r1.girar_izquierda()
r1.girar_izquierda()
r1.girar_izquierda()
r1.avanzar() # 5, 5

print(r1)

assert r1.x == 5
assert r1.y == 5
