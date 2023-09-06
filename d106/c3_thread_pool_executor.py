#
# ThreadPoolExecutor
# ------------------------------------------------------
# El `executor` es un componente capaz de registrar ejecutar y ejecutar tareas por nosotros
# colocándolas automáticamente en un hilo (evitamos crear hilos directamente)
#

from concurrent.futures import ThreadPoolExecutor

executor1 = ThreadPoolExecutor(max_workers=4)

def task(id):
    from time import sleep
    print(f"La tarea {id} ha comenzado a ejecutarse...")
    sleep(5)
    print(f"La tarea {id} ha finalizado :D")

# Sync (15s)
# task(1)
# task(2)
# task(3)

# Async threading
# from threading import Thread

# threads = []
# for id in [1, 2, 3]:
#     t = Thread(target=task, args=(id,))
#     threads.append(t)

# print("Inicializando los hilos...")
# [t.start() for t in threads]
# print("Esperando los hilos...")
# [t.join() for t in threads]
# print("Todos los hilos finalizaron :)")

# Async Executor

import asyncio

loop = asyncio.get_event_loop()

loop.run_in_executor(executor1, task, 1)
loop.run_in_executor(executor1, task, 2)
loop.run_in_executor(executor1, task, 3)