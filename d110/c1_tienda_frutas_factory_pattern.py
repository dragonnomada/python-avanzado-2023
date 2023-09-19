class Fruta:

    nombre = "FRUTA DESCONOCIDA"
    precio = 0.0
    existencias = 10

    def __init__(self, nombre, precio, existencias):
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def __str__(self):
        return "{} ${:.2f} ({} unidades)".format(self.nombre, self.precio, self.existencias)

#
# El patrón de diseño Factory define una función responsable de crear
# un objeto válido y de forma simple
# 

frutas_creadas = []

def crear_fruta(nombre = "FRUTA DESCONOCIDA", precio = 0.01, existencias = 0):
    if precio < 0.01:
        raise Exception("No se puede construir una fruta que cueste menos de 1 centavo")
    if precio <= 0.01 and existencias > 0:
        raise Exception("No se puede construir una fruta con 1 centavo o menos y al menos una existencia")
    if existencias < 0:
        raise Exception("No se puede construir una fruta con existencias negativas")
    if nombre.upper() in frutas_creadas:
        raise Exception("La fruta ya está registrada de otra forma")
    fruta = Fruta(nombre, precio, existencias)
    frutas_creadas.append(nombre.upper())
    return fruta

if __name__ == "__main__":
    
    manzana = crear_fruta(nombre="Manzana", precio=8, existencias=10)
    mango = crear_fruta(nombre="Mango", precio=16, existencias=4)
    pera = crear_fruta(nombre="Pera", precio=7, existencias=23)
    kiwi = crear_fruta(nombre="kiwi", precio=16, existencias=5)
    # manzana2 = crear_fruta(nombre="manzana", precio=9, existencias=10)
    # papaya = crear_fruta(nombre="Papaya", precio=0.01, existencias=1)

    print(manzana)
    print(mango)
    print(pera)
    print(kiwi)
    # print(manzana2)
    # print(papaya)