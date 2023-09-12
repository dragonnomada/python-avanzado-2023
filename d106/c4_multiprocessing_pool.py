#
# Pool
# -----------------------------------------
# El módulo `multiprocessing` dispone de una clase `Pool`
# que nos permite ejecutar tareas en *procesos* en lugar de hilos
# para hacer algo similar al `ThreadPoolExecutor` (resolver tareas por lotes/trabajores)
#

from multiprocessing import Pool

def task(id):
    from time import sleep
    print(f"La tarea {id} ha comenzado a ejecutarse...")
    sleep(5)
    print(f"La tarea {id} ha finalizado :D")
    return 100 * id

# Obligatorio en el uso de multi-procesamiento
if __name__ == "__main__":
    pool1 = Pool(processes=4) # Limitamos el números máximos a ejecutarse

    # pool.map -> inputs => func | process 1: func(inputs[0]) / process 2: func(inputs[0]) / ...
    outputs = pool1.map(task, [1, 2, 3, 4, 5, 6, 7]) # inputs = [1, 2, 3]

    # pool.map_asyc -> inputs => func :: obj.get()
    # outputs_async = pool1.map_async(task, [1, 2, 3])
    # ...
    # outputs = outputs_async.get()

    print(outputs) # [100, 200, 300]

