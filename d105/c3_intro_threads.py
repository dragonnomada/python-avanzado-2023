#
# Los hilos son tareas que se ejecutan en procesos independientes
# y ejecutan funciones sin bloquear el hilo principal.
#
# Los hilos tienen dos métodos importantes:
# - Un método llamado `start()` que inicia el hilo (ejecuta la función asociada)
# - Un método llamado `join()` que retiene el hilo actual hasta que el hilo termine 
#   (se espera a que la función asociada finalice)
#

# PASO 1 - Definir las funciones en forma de tareas a resolver

from time import sleep

def task1(): # ~40s finalizar
    print("TASK1 INCIALIZADO")
    for i in range(40):
        print("TASK 1: Valor de i={}".format(i))
        sleep(1) # Pausamos la ejecución 1s para simular una tarea que dura 1s
    print("TASK1 FINALIZADO")

def task2(): # ~25s finalizar
    print("TASK2 INCIALIZADO")
    for j in range(5):
        print("TASK 2: Valor de j={}".format(j))
        sleep(5) # Pausamos la ejecución 5s para simular una tarea que dura 5s
    print("TASK2 FINALIZADO")

# SIN EL USO DE HILOS:
# task1() ~+40s
# task2() ~+25s (~65s)
# ... (~65s)

# PASO 2 - Crear un hilo por cada tarea a resolver

from threading import Thread

t1 = Thread(target=task1) # Creamo un hilo que al inicializarse ejecute `task1`
t2 = Thread(target=task2) # Creamo un hilo que al inicializarse ejecute `task2`

t1.start() # +0s
t2.start() # +0s

print("Los hilos han sido ejecutados...")
print("Espera a que finalicen")
print("...")

# PASO 3 - Sincronizamos/Esperamos que los hilos hayan finalizado

t1.join() # Se espera hasta que el hilo 1 finalice (~+40)
t2.join() # Se espara hasta que el hilo 2 finalice (~+0)

print("Ambos hilos han finalizado")