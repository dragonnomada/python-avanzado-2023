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
    task_in_future(123, lambda future: print("Task 1:", future.result()))
    task_in_future(456, lambda future: print("Task 2:", future.result()))
    task_in_future(789, lambda future: print("Task 3:", future.result()))
    task_in_future(111, lambda future: print("Task 4:", future.result()))
    task_in_future(222, lambda future: print("Task 5:", future.result()))
    task_in_future(333, lambda future: print("Task 6:", future.result()))