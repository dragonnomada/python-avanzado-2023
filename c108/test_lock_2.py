import threading

counter = threading.Lock() # Crea un objeto bloqueable
display_show = threading.Lock() # Crea un objeto bloqueable
count = 0 # Guarda el valor del contador

display_show.acquire() # Mantiene la pantalla bloqueada inicialmente

def task1(): # Incrementa el contador y lo mantiene bloqueado por 5 segundos
    global count # Permite modificar la variable `count`
    from time import sleep

    while True:
        display_show.release() # Libera la pantalla para mostrar el valor del contador
        print("Tarea 1: Aumentar el contador y bloquearlo durante 5 segundos")
        print("[Tarea 1]: Bloquea el contador")
        counter.acquire() # Bloquea el contador
        print("[Tarea 1]: Incrementando el valor por 5 segundos...")
        count += 1 # Incrementa el valor del contador
        sleep(5) # Pausa durante 5 segundos
        print("[Tarea 1]: Valor incrementado")
        print("[Tarea 1]: Desbloquea el contador")
        counter.release() # Desbloquea el contador
        print("[Tarea 1]: Contador desbloquado")

def task2(): # Reporta el valor del contador, esperando a ser liberado
    while True:
        with display_show: # Espera a que la pantalla sea liberada
            print("Tarea 2: Mostrar el valor del contador, esperando a ser desbloqueado")
            with counter: # Espera a que el contador sea liberado
                print("[Tarea 2] Valor del contador:", count)
                display_show.acquire() # Bloquea la pantalla (Ya imprimió el contador)

# Creamos los hilos
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()