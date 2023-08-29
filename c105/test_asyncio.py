import asyncio

async def hello():
    await asyncio.sleep(5)

    print("Hello, async!")

coro = hello()

print(coro)

loop = asyncio.get_event_loop()

loop.run_until_complete(coro)