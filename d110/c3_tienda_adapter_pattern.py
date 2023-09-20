class Producto:

    _id: int = 0
    _nombre: str = "NO ASIGNADO"
    _precio: float = 0.01
    _pagado: bool = False

    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_precio(self) -> float:
        return self._precio
    
    def set_precio(self, precio):
        # TODO: Validar que el nuevo precio sea correcto
        assert precio >= 0.01
        self._precio = precio
    
    def is_pagado(self) -> bool:
        return self._pagado

    def pagar(self):
        self._pagado = True

    def __init__(self, id: int, nombre: str, precio: float) -> None:
        self._id = id
        self._nombre = nombre
        self._precio = precio

    def __str__(self) -> str:
        return "[{}] {} ${:.2f} (PAGADO={})".format(self._id, self._nombre, self._precio, self._pagado)

class Carrito:

    productos: [Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def quitar_producto(self, id: int) -> [Producto]:
        productos_eliminados = [producto for producto in self.productos if producto.get_id() == id]
        self.productos = [producto for producto in self.productos if not producto.get_id() == id]
        return productos_eliminados
    
    def calcular_total(self):
        total = sum([ producto.get_precio() for producto in self.productos ])

        # total = 0
        # for producto in self.productos:
        #     total = total + producto.get_precio()

        return total
    
    def pagar_productos(self):
        total = self.calcular_total()
        print(f"PAGANDO {len(self.productos)} productos...")
        print("POR PAGAR: ${:.2f}".format(total))
        import time
        time.sleep(5)
        [ producto.pagar() for producto in self.productos ]
        print("PAGADO: Se está imprimiendo el recibo...")
        print("PAGO EXISTOSO")

class ProductoOnline:

    # El adaptador se basa en adaptar un objeto de otra naturaleza
    # para hacerlo compable (hacía enfrente)
    # o retrocompatible (hacía atrás)
    producto = None

    def __init__(self, producto) -> None:
        self.producto = producto

    def get_id(self):
        return self.producto.get_id()

    def get_precio(self):
        print("Aumentando impuesto")
        precio_original = self.producto.get_precio()
        precio_con_iva = precio_original * 1.16
        # TODO: Otras reglas de negocio, por ejemplo, impuestos a alimentos, gasolinas, etc
        return precio_con_iva
    
    def pagar(self):
        # TODO: Adaptamos el producto, para modificar la forma de pago
        print(f"Registrando el pago del producto {self.producto.get_id()}")
        print(f"Enviando un correo al usuario que inició sesón...")
        print("PAGO GENERADO para el producto:", self.producto)

if __name__ == "__main__":

    producto1 = Producto(123, "Coca Cola", 17.5)
    producto2 = Producto(456, "Pepsi", 19.99)
    producto3 = Producto(111, "Gansito", 21.5)

    carrito1 = Carrito()

    # SI QUEREMOS ADAPTAR LOS PRODUCTOS
    producto1 = ProductoOnline(producto1)
    producto2 = ProductoOnline(producto2)
    producto3 = ProductoOnline(producto3)

    carrito1.agregar_producto(producto1)
    carrito1.agregar_producto(producto2)
    carrito1.agregar_producto(producto3)

    carrito1.pagar_productos()

