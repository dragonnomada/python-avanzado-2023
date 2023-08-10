# 
# Existe una librería llamada pytest
# que podemos instalar mediante `python3 -m pip install pytest`
#
# Podemos usar dicha librería para ejecutar pruebas:
# `python3 -m pytest c4_pytest_robot.py::test1`
#

from c2_simulador import Robot

def test1():
    r1 = Robot()

    r1.avanzar()
    r1.avanzar()
    r1.girar_derecha()
    r1.avanzar()

    assert r1.x == 1
    assert r1.y == 2

def test2():
    r1 = Robot()

    r1.avanzar()
    r1.avanzar()
    r1.girar_derecha()
    r1.girar_derecha()
    r1.avanzar()

    assert r1.x == 2
    assert r1.y == 2