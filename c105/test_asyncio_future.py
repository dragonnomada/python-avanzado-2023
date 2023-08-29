import asyncio
from concurrent.futures import Future
from time import sleep
from threading import Timer

future = Future()

async def hello():
    def done():
        future.set_result("Ok")

    timer = Timer(5, done)

    timer.start()

loop = asyncio.get_event_loop()

# asyncio.ensure_future(hello())
loop.run_until_complete(hello())

print(future.result())