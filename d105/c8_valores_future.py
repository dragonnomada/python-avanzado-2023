from concurrent.futures import Future

# Un objeto a "Futuro" es capaz de esperar por un resultado
# y notificar cuándo se encuentre listo

future_users = Future()

# El `callback` es un función cualquiera
# diseñada para ejecutarse tras algún evento
# es decir, es una función que será llamada por otra función
# y cuándo la segunda función lo desee
def users_done(future_users): # callback
    print("Recibiendo los usuarios prometidos a futuro...")
    print("Los usuarios están listos")
    # Recuperamos el resultado a futuro (ya está presente)
    users = future_users.result() # <- [...]
    # print(users)
    for user in users:
        print("{} {}, {} ({})".format(
            user["name"]["title"], 
            user["name"]["first"], 
            user["name"]["last"], 
            user["email"])
        )

# Registramos el callback `user_done`
# para ejecutarse cuándo el resultado a futuro sea ajustado
future_users.add_done_callback(users_done) 

# ...

# En algún momento yo puedo establecer el valor a futuro
# Ajustamos el valor prometido a futuro
# -> Se ejecuta el add_done_callback(<func>)
# print("Enviando los usuarios prometidos a futuro...")
# future_users.set_result(["pepe", "paco", "ana", "dafne"])

from time import sleep

def task_fetch_api_users(n):
    import requests

    print("Solicitando los usuarios al API...")

    sleep(10)

    response = requests.get(f"https://randomuser.me/api?results={n}")

    import json

    print("Recuperando los usuarios del JSON")
    users = json.loads(response.text)

    # print(users)

    print("Enviando los usuarios prometidos a futuro...")
    future_users.set_result(users["results"])

task_fetch_api_users(10)
