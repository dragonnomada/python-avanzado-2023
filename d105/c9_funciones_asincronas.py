#
# Las funciones asíncronas son funciones especiales
# capaces de esperar a otras funciones asíncronas
# es decir, son funciones con la capacidad de esperar otras funciones
# para formar un flujo lineal en la espera asíncrona de peticiones
#

from time import sleep

async def fetch_api_users(n):
    import requests

    sleep(5)

    response = requests.get(f"https://randomuser.me/api?results={n}")

    import json

    data = json.loads(response.text)

    return data["results"]

async def print_users():
    for n in [3, 5, 10]:
        users = await fetch_api_users(n) # LINEAL :D

        for user in users:
            print("{} {}".format(user["name"]["first"], user["name"]["last"]))

        print("-" * 80)

import asyncio

loop = asyncio.get_event_loop()

loop.run_until_complete(print_users())