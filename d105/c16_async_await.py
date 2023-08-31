url1 = "https://raw.githubusercontent.com/dragonnomada/python-avanzado-2023/main/datasets/titanic.csv"
url2 = "https://raw.githubusercontent.com/dragonnomada/python-avanzado-2023/main/datasets/report1_spotify.csv"

# def fetch_sync(url):
#     import requests
#     response = requests.get(url)
#     return response.content

# # SYNC uno tras otro
# for _ in range(100):
#     fetch_sync(url1)
# print("Solicitando URL 1...")
# titanic = fetch_sync(url1)
# print("BYTES: ", len(titanic))
# print("Contenido de la URL 1 descargado")

# print("Solicitando URL 2...")
# spotify = fetch_sync(url2)
# print("BYTES: ", len(spotify))
# print("Contenido de la URL 2 descargado")

# ASYNC usando tuplas
# print("Solicitando URL 1 y URL 2...")
# titanic, spotify = fetch_sync(url1), fetch_sync(url2)

# print("BYTES TITANIC:", len(titanic), "BYTES SPOTIFY:", len(spotify))

async def fetch_async(url):
    # 1. Definir un Executor que ejecutará en un hilo la tarea (requests.get)
    from concurrent.futures import ThreadPoolExecutor
    executor1 = ThreadPoolExecutor(max_workers=1)

    # 2. Definimos la función objetivo/tarea que será ejecutada en el hilo (requests.get)
    import requests
    
    # 3. Creamos un Event-Loop que espere a que termine el executor de resolver la tarea (requests.get)
    import asyncio
    loop1 = asyncio.get_event_loop()
    
    # 4. Esperar a que termine el Executor de hacer la tarea en el Event-Loop (await ...)
    response = await loop1.run_in_executor(executor1, requests.get, url)
    
    # 5. El resultado es el response similar al response síncrono (response = requests.get(url))
    #    Pero envuelto en un hilo asíncrono para reducir el estrés y aumentar el rendimiento
    return response.content

import asyncio

async def download(n):
    print(f"Solicitando el CSV del titanic... x{n} veces")
    
    tasks = []
    
    for _ in range(n):
        # print("Solicitando el CSV del titanic...")
        # titanic = loop2.run_until_complete(fetch_async(url1))
        task = asyncio.create_task(fetch_async(url1)) # Crea un tarea y la ejecuta inmediatamente
        tasks.append(task)
        # print("TITANIC BYTES:", len(titanic))
    
    for task in tasks:
        await task

    print("Finalizado")

loop2 = asyncio.get_event_loop()

loop2.run_until_complete(download(100))

