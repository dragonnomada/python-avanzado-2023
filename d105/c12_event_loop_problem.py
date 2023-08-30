#
# Cuándo necesitamos sincronizar el código por un hilo
# que no está formalizado como podría ser Future
# la estrategia más directa es preguntar si ya acabó
# pero, tenemos que preguntar ¡¡¡todo!!! el tiempo
#

picture = None

def fetch_picture():
    global picture # Advierto que usaré y reemplazaré
                   # la variable global 
                   # (antes de la llamada a la función)
    from time import sleep
    sleep(2)
    picture = "https://fake.com/no-existe.png"

from threading import Thread

Thread(target=fetch_picture).start() # Se comienza a descargar la imagen (toma 2s)

import time

# Bloqueo del hilo principal hasta que se cumpla una condición
i = 0
# PROBLEMA DEL EVENT-LOOP
# -> Hasta cuándo se generará un evento en un ciclo indeterminado
# ! Necesitamos bloquear el programa (hilo principal)
#   hasta que `picture` tenga un valor que no sea `None`
while picture == None:
    print(f"Esperando... ({i})")
    i += 1
    time.sleep(0.1) # ¿Cómo saber el tiempo mínimo que deberíamos esperar?

print("La imagen está lista")
print(picture)

