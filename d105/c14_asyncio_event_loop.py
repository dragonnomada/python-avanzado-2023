#
# AsyncIO es una librería que nos permite manejar
# el problema del Event-Loop de forma determinística
#

#
# AsyncIO está optimizado para 
# *Funciones Asíncronas*
# Las cuales son funciones extendidas que nos permiten
# ejecutar código capaz de esperar otros "awaitables".
#
# Las funciones asíncronas por defecto se ejecutan en hilos
# y sus resultados son "awaitables".
#

import asyncio

async def fetch_picture():
    import requests
    response = requests.get("https://randomuser.me/api")
    import json
    data = json.loads(response.text)
    results = data["results"]
    user = results[0]
    picture = user["picture"]["large"]
    return picture

# coro = fetch_picture() # Corountine

loop1 = asyncio.get_event_loop()

print("Esperando la imagen...")
# Locking...
picture = loop1.run_until_complete( fetch_picture() )

print("La imagen está lista")
print(picture)

