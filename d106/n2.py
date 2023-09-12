def task(id):
    print(f"Task started: {id}")
    from time import sleep
    print(f"Task {id} waiting...")
    sleep(5)
    print(f"Task {id} completed")
    return id ** 2

if __name__ == "__main__":
    import threading

    inputs = [123, 456, 789, 111, 222, 333]
    
    print("inputs:", inputs)

    # 1. Definición de los hilos
    threads = [ threading.Thread(target=task, args=(id,)) for id in inputs ]

    # 2. Inicialización de los hilos
    [ t.start() for t in threads ]

    # 3. Sincronización o espera de los hilos
    outputs = [ t.join() for t in threads ]

    print("outputs:", outputs)