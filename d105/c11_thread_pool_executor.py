#
# Un ejecutor es un objeto encargado de ejecutar una función
# con sus parámetros definidos.
#
# El resultado del ejecutor será un `Future` que contenga
# la salida de la función.
#
# Todas la funciones ejecutadas por el ejecutor se harán
# en hilos disponibles en su definición.
#
# Es decir, el ejecutor tiene asociado una piscina de hilos
# que están disponibles para ejecutar tareas/funciones
# y pueden ser ocupadas a disposición, cuándo un hilo
# es ocupado en una tarea, la función se ejecuta con
# sus parámetros en el hilo y cuándo finaliza regresa
# a la piscina para volver a estar disponible.
#

from concurrent.futures import ThreadPoolExecutor

executor1 = ThreadPoolExecutor(max_workers=2)

def fetch_picture():
    import requests
    response = requests.get("https://randomuser.me/api")
    import json
    data = json.loads(response.text)
    results = data["results"]
    user = results[0]
    picture = user["picture"]["large"]
    return picture

if __name__ == "__main__":
    import sys
    if sys.argv[1] == "sync":
        print("Usando el modo síncrono")

        # 1. Ejecutar 10 tareas en secuencia
        for _ in range(10):
            # 2. Llamamos a la tarea y esperamos a que
            #    se resuelva para continuar la secuencia
            fetch_picture()

    elif sys.argv[1] == "async":
        print("Usando el modo asíncrono")

        # 1. Creamos una lista que retenga los futures
        #    prometidos por el ejecutor para cada tarea
        #    que le mandamos
        futures = []

        # 2. Ejecutamos 10 tareas en secuencia
        for _ in range(10):
            # 3. Ejecutamos la tarea en forma diferida
            #    a través del ejecutor, es decir,
            #    el ejecutor se encargará de ejecutar
            #    nuestra tarea y nos devolverá inmediatamente
            #    un `Future` que será resuelto a futuro
            future_picture = executor1.submit(fetch_picture)
            # 4. Guardamos el `Future` que contendrá el resultado
            #    de la ejecución de la tarea a futuro
            futures.append(future_picture)

        from concurrent.futures import wait

        # 5. Espera todos los `Future` listados
        #    para sincronizar el código (linealizarlo)
        wait(futures)

        # 6. Recorremos todos los `Future` que se suponen
        #    finalizados para recuperar el valor a futuro
        for future_picture in futures:
            # 7. Recuperamos el valor a futuro
            picture = future_picture.result()

            # 8. Procesamos el valor a futuro como se deba
            print(picture)

    else:
        print("Modo no reconocido usa:")
        print(" <file>.py sync | async")
