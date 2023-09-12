from concurrent.futures import Future

def task(id):
    print(f"Task started: {id}")
    from time import sleep
    print(f"Task {id} waiting...")
    sleep(5)
    print(f"Task {id} completed")
    return id ** 2

def task_in_future(id, callback):
    output_future = Future()

    output_future.add_done_callback(callback)

    def in_thread():
        output = task(id)
        output_future.set_result(output)

    import threading

    threading.Thread(target=in_thread).start()

if __name__ == "__main__":
    futures_and_ids = []

    inputs = [123, 456, 789, 111, 222, 333]

    [ task_in_future(id, lambda future: futures_and_ids.append((id, future))) for id in inputs ]

    # PROBLEMA: La lista de futures_and_ids no se va a llenar hasta que los callbacks sean llamados

    futures = [ future for id, future in futures_and_ids ]
    
    from concurrent.futures import wait

    wait(futures)

    from concurrent.futures import as_completed

    outputs = as_completed(futures)

    ids = [ id for id, future in futures_and_ids ]

    print(list(zip(ids, outputs)))
