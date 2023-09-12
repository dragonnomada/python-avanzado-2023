from concurrent.futures import ThreadPoolExecutor

def task(id):
    print(f"Task started: {id}")
    from time import sleep
    print(f"Task {id} waiting...")
    sleep(5)
    print(f"Task {id} completed")
    return id ** 2

if __name__ == "__main__":
    executor1 = ThreadPoolExecutor(max_workers=4) # Máximo de hilos

    future1 = executor1.submit(task, 123)
    future2 = executor1.submit(task, 456)
    future3 = executor1.submit(task, 789)
    future4 = executor1.submit(task, 111)
    future5 = executor1.submit(task, 222)
    future6 = executor1.submit(task, 333)

    from concurrent.futures import wait
    wait([future1, future2, future3, future4, future5, future6])

    # from concurrent.futures import as_completed
    # outputs = as_completed([future1, future2, future3, future4, future5, future6])

    outputs = [ future.result() for future in [future1, future2, future3, future4, future5, future6] ]

    print(outputs)