def foo_sync():
    from time import sleep
    print("Se ha iniciado la función foo, espera a que termine...")
    sleep(5)
    print("La función foo ha terminado")
    return 123

# print("Iniciando el programa")
# resultado = foo_sync() # Después de 5 segundos obtemos el resultado=123
# print("resultado =", resultado)
# print("Finalizando el programa")

async def foo_async():
    from concurrent.futures import ThreadPoolExecutor
    executor = ThreadPoolExecutor(max_workers=1)
    import asyncio
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, foo_sync)
    return result

import asyncio

async def main():
    tasks = [ asyncio.create_task(foo_async()) for _ in range(100) ] # Lista de 100-task

    for task in tasks:
        await task

    print("OK.")

loop_main = asyncio.get_event_loop()

loop_main.run_until_complete(main())




