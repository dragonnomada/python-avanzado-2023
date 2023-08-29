from concurrent.futures import Future
from threading import Timer
from time import sleep

future = Future()

def done_future():
    future.set_result({ "success": True, "result": "ok" })

timer = Timer(5, done_future)

timer.start()

while not future.done():
    print("Esperando...")
    sleep(1)

print("Future finalizado:", future.result())