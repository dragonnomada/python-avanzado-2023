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
# El patrón de diseño Builder define una nueva responsable de crear
# un objeto válido y de forma simple en diferentes fases 
# (cada fase representa un método de la clase Builder)
# 

class FrutaBuilder:

    fruta_resultante: Fruta = None

    nombre: str = None
    precio: float = None
    existencias: int = None

    frutas_creadas = []

    def asignar_nombre(self, nombre: str):
        assert type(nombre) == str
        assert not nombre.strip() == ""
        import re
        assert not re.match("^[A-Z][a-z]*$", nombre) == None
        assert not nombre.upper() in self.frutas_creadas
        self.nombre = nombre
        self.frutas_creadas.append(nombre.upper())
    
    def asignar_precio(self, precio: float = 0.01):
        assert type(precio) == float or type(precio) == int
        assert not precio < 0.01
        self.precio = precio
    
    def asignar_existencias(self, existencias: int = 0):
        assert type(existencias) == int
        assert not existencias <= 0
        assert not self.precio == None
        if self.precio == 0.01:
            assert existencias > 0
        self.existencias = existencias

    def build(self) -> Fruta:
        self.fruta_resultante = Fruta(self.nombre, self.precio, self.existencias)
        return self.fruta_resultante

if __name__ == "__main__":
    
    # manzanaBuilder = FrutaBuilder()
    # manzanaBuilder.asignar_nombre("Manzana")
    # manzanaBuilder.asignar_precio(8)
    # manzanaBuilder.asignar_existencias(10)
    # manzana = manzanaBuilder.build()

    # La ventaja de un builder es que es automatizable
    frutas_datos = [
        {
            "nombre": "Manzana",
            "precio": 8,
            "existencias": 10
        },
        {
            "nombre": "Mango",
            "precio": 16,
            "existencias": 4
        },
        {
            "nombre": "Pera",
            "precio": 7,
            "existencias": 23
        },
        {
            "nombre": "Kiwi",
            "precio": 20,
            "existencias": 5
        },
        {
            "nombre": "Manzana",
            "precio": 9,
            "existencias": 10
        },
        {
            "nombre": "papaya",
            "precio": 18,
            "existencias": 10
        },
    ]

    print(frutas_datos)

    frutas_objetos = []

    for fruta_dato in frutas_datos:
        try:
            builder = FrutaBuilder()
            builder.asignar_nombre(fruta_dato["nombre"])
            builder.asignar_precio(fruta_dato["precio"])
            builder.asignar_existencias(fruta_dato["existencias"])
            fruta = builder.build()
            frutas_objetos.append(fruta)
        except Exception as e:
            print("*" * 80)
            print("No se pudo crear la fruta:", fruta_dato)
            print("*" * 80)
    

    print(frutas_objetos)
    print("=" * 80)
    for fruta in frutas_objetos:
        print(fruta)
    print("-" * 80)
    total = sum(map(lambda fruta: fruta.precio, frutas_objetos))
    print("Total: ${:.2f}".format(total))
    print("Precio promedio: ${:.2f}".format(total / len(frutas_objetos)))