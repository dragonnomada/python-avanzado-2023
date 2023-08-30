#
# AsyncIO es una librería que nos permite manejar
# el problema del Event-Loop de forma determinística
#

import asyncio

# 1. Creamos un Event-Loop
loop1 = asyncio.get_event_loop()

from concurrent.futures import Future

future_picture = loop1.create_future()

def fetch_picture():
    from time import sleep
    sleep(2)
    print("Imagen lista, ajustando en `Future`...")
    future_picture.set_result("https://fake.com/no-existe.png")

print("Solicitando imagen...")
from threading import Thread
Thread(target=fetch_picture).start()
# fetch_picture()
print("Esperando la imagen...")

# 2. Sincronizamos un código a futuro o asíncrono
loop1.run_until_complete(asyncio.ensure_future(future_picture, loop=loop1))

print("La imagen ya está lista")
print(future_picture.result())