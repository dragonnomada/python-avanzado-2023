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

class Venta:
    next_venta_id = 1 # Propiedad compartida a toda la clase 
                      # (self.next_venta_id -> Venta.next_venta_id)

    producto = None
    pago = None

    def __init__(self, producto) -> None:
        self.producto = producto
        self.pago = Pago()
        self.pago.id = Venta.next_venta_id # Singleton
        Venta.next_venta_id += 1

    def get_total(self):
        return self.producto.get_precio() * 1.15
    
    def get_ticket(self):
        total = self.get_total()
        self.pago.pagar(total)
        print("Producto vendido:", self.producto.id)
        print("ID de pago:", self.pago.id)
        print("Cadena de pago:", self.pago.cadena)
        print("Total pagado:", total)

if __name__ == "__main__":
    producto1 = Producto()
    producto1.id = 123
    producto1.precio = 17.5

    venta1 = Venta(producto1)

    print(venta1.get_total())

    venta1.get_ticket()
    
    venta2 = Venta(producto1)

    print(venta2.get_total())

    venta2.get_ticket()