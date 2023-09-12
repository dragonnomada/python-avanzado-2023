import threading

def task(id):
    print(f"Task started: {id}")
    from time import sleep
    print(f"Task {id} waiting...")
    sleep(5)
    print(f"Task {id} completed")
    return id ** 2

class MyTaskInThread(threading.Thread):

    id = None
    output = None

    def __init__(self, id):
        super().__init__() # La herencia en Python nos obliga a inicializar la clase base
                           # Para que `self` esté disponible (sino podría causar error)
        self.id = id

    def run(self):
        # code here ... or ... code in other place
        self.output = task(self.id)
    
if __name__ == "__main__":
    print("Defining threads...")

    inputs = [123, 456, 789, 111, 222, 333]

    print("inputs:", inputs)

    # 1. Definición de los hilos (Orientada a Objetos)
    threads = [ MyTaskInThread(id) for id in inputs ]

    print("Starting threads...")

    # 2. Inicialización o lanzamiento de los hilos
    [ t.start() for t in threads ]

    print("Waiting threads...")

    # 3. Sincronización o espera de los hilos
    [ t.join() for t in threads ]

    print("Threads is already finish")

    outputs = [ t.output for t in threads ]

    print("outputs:", outputs)