#
# El multiprocesamiento es similar al uso de hilos, pero con las siguientes diferencias:
# - Los hilos son subrutinas dentro de un mismo programa que comparten memoria y recursos
#   es decir, dos hilos, podrían bloquearse al querer modificar la misma variable o archivo
#   esto debido a que Python sólo ejecuta una instrucción a la vez (no dos)
# - El multiprocesamiento ocurre en procesos independiente con memoria y recursos independientes
#   es decir, dos procesos similares, se ejecutan como dos programas distintos
#
# hilo => Un programa ejecutándose (foo.py)
# proceso => Un mismo programa ejecutándose por cada proceso (foo.py (1), foo.py (2), ..., foo.py (n))
#   * Nota: El procesamiento pide memoria y recursos individuales por cada proceso
#   - Comentario: Un proceso equivale a un clúster/fork
#                 Un hilo representa una división del hilo principal dentro del mismo del programa
#                 y proceso sería una división de los recursos a nivel sistema operativo
#

import multiprocessing
# import threading

# === Versión orientada a objetos ===

# class A:
#     def __init__(self, x):
#         self.x = x

# class B(A):
#     def __init__(self, x, y):
#         super(B, self).__init__(x) # Reemplazo/uso del constructor superior
#         self.y = y

# Herencia MyProcess <- Process
class MyProcess (multiprocessing.Process):

    def __init__(self, id, message):
        # Inicializador de la clase base (-> multiprocessing.Process)
        super(MyProcess, self).__init__() # constructor
        self.id = id
        self.message = message

    # run() se ejecuta sobre un hilo, en multiproceso y con acceso al self
    # este método se ejecuta automáticamente cuando llamemos a .start() del proceso
    def run(self):
        # import time
        # time.sleep(20)
        import requests
        url = "https://randomuser.me/api?seed={}".format(id)
        response = requests.get(url)
        data = response.json()
        results = data["results"]
        user = results[0]
        name = user["name"]["first"] + " " + user["name"]["last"]
        print(self.message, name)

print("hola")

# Estamos obligados a no colocar código esparcido (código no-controlado)
# Esto ocurre porque el proceso es un programa independiente de python
# -> c1_multiprocessing.py => c1_multiprocessing.py
#                          => c1_multiprocessing.py
#                          => c1_multiprocessing.py
# Necesitamos realizar el código de ejecución de manera formal 
# (sólo si el archivo corresponde al módulo)
if __name__ == "__main__":
    print("-" * 80)

    # proceso = MyProcess(1, "El usuario es:")

    # # Ejecuta run() sobre el hilo actual
    # # proceso.run()

    # # Ejecuta run() en un "hilo" (en un proceso)
    # proceso.start()

    # # Espera (bloquea el hilo actual) hasta que el proceso finalice
    # proceso.join()

    # Cada MyProcess se ejecutará en un programa diferente
    # !!! IMPORTANTE: No ejecutar más procesos que los núcleos de la máquina
    procesos = [ MyProcess(i, f"Process {i}:") for i in [98, 123, 97, 34] ]

    [proceso.start() for proceso in procesos]


