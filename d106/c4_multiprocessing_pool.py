#
# Pool
# -----------------------------------------
# El módulo `multiprocessing` dispone de una clase `Pool`
# que nos permite ejecutar tareas en *procesos* en lugar de hilos
# para hacer algo similar al `ThreadPoolExecutor` (resolver tareas por lotes/trabajores)
#

from multiprocessing import Pool

pool1 = Pool(processes=2) # Limitamos el números máximos a ejecutarse

def task(id):
    # from time import sleep
    # print(f"La tarea {id} ha comenzado a ejecutarse...")
    # sleep(5)
    # print(f"La tarea {id} ha finalizado :D")
    return 100 * id

# outputs = pool1.map(task, [1, 2, 3]) # inputs = [1, 2, 3]

outputs_async = pool1.map_async(task, [1, 2, 3])

outputs = outputs_async.get()

print(outputs) # [100, 200, 300]

