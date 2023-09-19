# PROBLEMA DEL BLOQUEO: Ocurre cuándo un sistema queda bloqueado
# porque los hilos requieren los mismos recursos y no han sido liberados

import threading

# Variables tradicionales
frutas_pedidas = [(1, "pera"), (3, "piña"), (1, "mango")] # Realizar un pedido 1s 

# SOLUCIÓN: Vamos a crear una variable especial capaz de bloquearse y desbloquearse en los hilos
pedidos_bloqueados = threading.Lock() # Creamos una variable llamada `locker`

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
    print("El cliente pide una fruta")
    print("Los pedidos se encuentran:")
    if pedidos_bloqueados.locked():
        print(" >>> BLOQUEADOS")
    else:
        print(" >>> DESBLOQUEADOS")
    # TODO: Bloquear las frutas pedidas en lo que registramos la fruta
    #       Es decir, ningún otro cliente puede pedir una fruta durante 1s
    pedidos_bloqueados.acquire() # BLOQUEA LOS PEDIDOS
    print(f"Cliente {id} pide fruta {fruta}")
    print(f"Durante 1s aprox. verificaremos:")
    print(f"- Existencia de la fruta")
    print(f"- El cliente sea válido")
    print(f"- El cliente tenga fondos para realizar su pedido")
    if inventario[fruta] <= 0:
        print(f"Pedido rechazado del cliente {id} para la fruta {fruta}")
        # TODO: Desbloquear las frutas pedidas para permitir que otros usuarios pidan frutas
        #       Es decir, otro hilo puede disponer de frutas_pedidas
        # IMPORTANTE!!! NO OLVIDAR LIBERAR LAS VARIABLES
        # pedidos_bloqueados.release()
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
    pedidos_bloqueados.release()

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

# import threading

t1 = threading.Thread(target=hilo_recibe_pedidos_online)
t2 = threading.Thread(target=hilo_recibe_pedidos_en_tienda)

t1.start() # Iniciamos los pedidos online
t2.start() # Iniciamos los pedidos física

t1.join()
t2.join()