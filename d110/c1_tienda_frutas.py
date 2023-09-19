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

if __name__ == "__main__":
    # Creación de los objetos fruta no está controlada
    # Riesgos:
    # 1. El programador tiene que recordar los parámetros de construcción:
    #    - ¿Cuál es el primer parámetro (nombre, precio o existencias)?
    #    - ¿Qué valores son válidos en la construcción (se pueden negativos)?
    # 2. No podemos validar que el objeto se esté construyendo con valores válidos
    # 3. No es reutilizable la construcción
    manzana = Fruta("Manzana", 8, 10)
    mango = Fruta("Mango", 16, 4)
    pera = Fruta("Pera", 7, 23)
    kiwi = Fruta("kiwi", 16, 5)
    manzana2 = Fruta("mazana", 9, 10)

    print(manzana)
    print(mango)
    print(pera)
    print(kiwi)
    print(manzana2)