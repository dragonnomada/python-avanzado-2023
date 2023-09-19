# Variables tradicionales
frutas_pedidas = [(1, "pera"), (3, "piña"), (1, "mango")] # Realizar un pedido 1s 

inventario = {
    "manzana": 1,
    "pera": 1,
    "mango": 1,
    "fresa": 1,
    "coco": 1,
    "kiwi": 1,
    "papaya": 1,
    "piña": 1,
}

def cliente_pide_fruta(id, fruta):
    # TODO: Bloquear las frutas pedidas en lo que registramos la fruta
    #       Es decir, ningún otro cliente puede pedir una fruta durante 1s
    print(f"Cliente {id} pide fruta {fruta}")
    print(f"Durante 1s aprox. verificaremos:")
    print(f"- Existencia de la fruta")
    print(f"- El cliente sea válido")
    print(f"- El cliente tenga fondos para realizar su pedido")
    if inventario[fruta] <= 0:
        print(f"Pedido rechazado del cliente {id} para la fruta {fruta}")
        # TODO: Desbloquear las frutas pedidas para permitir que otros usuarios pidan frutas
        #       Es decir, otro hilo puede disponer de frutas_pedidas
        return
    print(f"Hay {inventario[fruta]} existencias de la fruta {fruta}")
    import time
    time.sleep(1) # Tardamos 1s en agregar la fruta
    frutas_pedidas.append((id, fruta)) # Agregamos el registro
    inventario[fruta] -= 1
    if inventario[fruta] < 0:
        raise Exception(f"El pedido provocó existencias negativas para la fruta {fruta}")
    # TODO: Desbloquear las frutas pedidas para permitir que otros usuarios pidan frutas
    #       Es decir, otro hilo puede disponer de frutas_pedidas

def hilo_recibe_pedidos_online():
    # Simulamos que cae un pedido cada 20s
    while True:
        # Realizando el pedido para el cliente
        import random
        id = random.randint(1, 11) # Un entero aleatorio entre 1 y 10
        # fruta = random.choice(["manzana", "pera", "papaya", "piña"])
        fruta = "coco"
        print(f"Tienda ONLINE realizará pedido para cliente {id} con fruta {fruta}")
        cliente_pide_fruta(id, fruta)
        import time
        time.sleep(5)

def hilo_recibe_pedidos_en_tienda():
    # Simulamos que cae un pedido cada 1s
    while True:
        # Realizando el pedido para el cliente
        import random
        id = random.randint(1, 11) # Un entero aleatorio entre 1 y 10
        # fruta = random.choice(["manzana", "kiwi", "mango", "fresa", "coco", "pera", "papaya", "piña"])
        fruta = "coco"
        print(f"Tienda FÍSICA realizará pedido para cliente {id} con fruta {fruta}")
        cliente_pide_fruta(id, fruta)
        import time
        time.sleep(1)

import threading

t1 = threading.Thread(target=hilo_recibe_pedidos_online)
t2 = threading.Thread(target=hilo_recibe_pedidos_en_tienda)

t1.start() # Iniciamos los pedidos online
t2.start() # Iniciamos los pedidos física

t1.join()
t2.join()