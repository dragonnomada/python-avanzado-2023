#
# DECORATOR: Función que decora a otra función
# TARGET: Una función que cumple un objetivo específico y genérico
# WRAPPER: Función que transforma las entradas y salidas del objetivo
#

# El decorador (DECORATOR) sustituye la función objetivo (TARGET)
# por la función de envoltura (WRAPPER)

productos = []

def tienda_agregar_producto(registrar_producto):
    def wrapper():
        producto = registrar_producto() # El wrapper atrapa la salida normal del TARGET
        productos.append(producto) # Y hace algo con esa salida
        return producto
    return wrapper

@tienda_agregar_producto
def registrar_producto_terminal():
    id = input("ID: ")
    nombre = input("NOMBRE: ")
    precio = input("PRECIO: ")
    # TODO: Validaciones o más cosas
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": float(precio)
    }
    return producto # Esto es lo que devuelve la función normal (TARGET)

@tienda_agregar_producto
def registrar_producto_archivo():
    with open("producto.txt", "r") as file:
        id = file.readline()
        nombre = file.readline()
        precio = file.readline()
        # TODO: Validaciones o más cosas
        producto = {
            "id": id,
            "nombre": nombre,
            "precio": float(precio)
        }
        return producto
    
if __name__ == "__main__":
    # producto1 = registrar_producto_terminal()
    # print(producto1)

    registrar_producto_terminal()
    registrar_producto_terminal()

    print(productos)