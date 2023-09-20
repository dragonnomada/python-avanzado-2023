class Producto:
    id = 0
    precio = 0.0
    def get_precio(self):
        return self.precio

class Pago:
    id = 0
    cadena = ""
    def pagar(self, total):
        print("pagando...", total)
        import random
        self.cadena = "".join([ chr(random.randint(65, 88)) for _ in range(32) ])
        return self.cadena

class Articulo:
    producto = None
    pago = None

    def __init__(self, producto, pago) -> None:
        self.producto = producto
        self.pago = pago

    def get_precio(self):
        return self.producto.get_precio()
    
    def pagar(self):
        total = self.producto.get_precio()
        return self.pago.pagar(total)
    
if __name__ == "__main__":
    producto = Producto()
    producto.id = 123
    producto.precio = 17.5
    pago = Pago()
    pago.id = 101

    articulo = Articulo(producto, pago)

    print(articulo.get_precio())
    print(articulo.pagar())