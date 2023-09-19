# PROBLEMA DE LA INANICIÓN: Es que un hilo tenga mayor prioridad
# en el uso de recursos y los acapare, dejando a otros hilos sin recursos

import threading

# Variables tradicionales
frutas_pedidas = [(1, "pera"), (3, "piña"), (1, "mango")] # Realizar un pedido 1s 

# SOLUCIÓN: Vamos a crear una variable especial capaz de bloquearse y desbloquearse en los hilos
pedidos_bloqueados = threading.Lock() # Creamos una variable llamada `locker`

cambio_tienda = threading.Lock()
tienda_online = False
tienda_fisica = True

def toggle_tienda():
    global tienda_online, tienda_fisica
    with cambio_tienda:
        # ESTRATEGIA 1: 1x1
        if tienda_online:
            tienda_online = False
            tienda_fisica = True
        else:
            tienda_fisica = False
            tienda_online = True

# pedidos_bloequeados.acquire() - Provocamos que la variable se bloquee
# pedidos_bloequeados.release() - Provocamos que la variable se desbloquee
# pedidos_bloequeados.locked() - Nos indica si la variable está bloqueada o no

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
    # print(f"El cliente {id} pide una fruta {fruta}")
    # print("Los pedidos se encuentran:")
    # if pedidos_bloqueados.locked():
    #     print(f" >>> BLOQUEADOS ({id})")
    # else:
    #     print(f" >>> DESBLOQUEADOS ({id})")
    # print(f"Cliente {id} pide fruta {fruta}")
    # print(f"Durante 1s aprox. verificaremos:")
    # print(f"- Existencia de la fruta")
    # print(f"- El cliente sea válido")
    # print(f"- El cliente tenga fondos para realizar su pedido")
    if inventario[fruta] <= 0:
        # print(f"Pedido RECHAZADO del cliente {id} para la fruta {fruta}")
        return
    # print(f"Hay {inventario[fruta]} existencias de la fruta {fruta}")
    import time
    time.sleep(1) # Tardamos 1s en agregar la fruta
    frutas_pedidas.append((id, fruta)) # Agregamos el registro
    inventario[fruta] -= 1
    if inventario[fruta] < 0:
        raise Exception(f"El pedido provocó existencias negativas para la fruta {fruta}")

def hilo_recibe_pedidos_online():
    # Simulamos que cae un pedido cada 20s
    while True:
        # Realizando el pedido para el cliente
        import random
        id = random.randint(1, 11) # Un entero aleatorio entre 1 y 10
        fruta = random.choice(["manzana", "pera", "papaya", "piña"])
        if tienda_online:
            print(f"Tienda ONLINE realizará pedido para cliente {id} con fruta {fruta}")
            # VAMOS A GARANTIZAR QUE LA VARIABLE ESTÉ DESBLOQUEADA O ESPERAR HASTA QUE SE DESBLOQUEE
            with pedidos_bloqueados: # Bloquea y libera una variable automáticamente
                # Bloquea
                cliente_pide_fruta(id, fruta)
                # Desbloquea
            toggle_tienda()
        import time
        time.sleep(5)

def hilo_recibe_pedidos_en_tienda():
    # Simulamos que cae un pedido cada 1s
    while True:
        # Realizando el pedido para el cliente
        import random
        id = random.randint(1, 11) # Un entero aleatorio entre 1 y 10
        fruta = random.choice(["manzana", "kiwi", "mango", "fresa", "coco", "pera", "papaya", "piña"])
        if tienda_fisica:
            print(f"Tienda FISICA realizará pedido para cliente {id} con fruta {fruta}")
            # VAMOS A GARANTIZAR QUE LA VARIABLE ESTÉ DESBLOQUEADA O ESPERAR HASTA QUE SE DESBLOQUEE
            with pedidos_bloqueados:
                # Bloquea
                cliente_pide_fruta(id, fruta)
                # Desbloquea
            toggle_tienda()
        import time
        time.sleep(1)

# import threading

t1 = threading.Thread(target=hilo_recibe_pedidos_online)
t2 = threading.Thread(target=hilo_recibe_pedidos_en_tienda)

t1.start() # Iniciamos los pedidos online
t2.start() # Iniciamos los pedidos física

t1.join()
t2.join()