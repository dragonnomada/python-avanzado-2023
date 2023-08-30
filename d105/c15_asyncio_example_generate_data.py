def task_generate_data(n):
    from time import time
    start = time()
    with open(f"output/gen_{n}.txt", "w") as f:
        for i in range(1, n + 1):
            f.write("*" * i + "\n")
    return time() - start

def task_generate_first_2k_sync():
    times = []
    for i in range(1, 2_000):
        time = task_generate_data(i)
        times.append(time)
    return times

def task_generate_first_2k_async():
    from concurrent.futures import ThreadPoolExecutor

    executor1 = ThreadPoolExecutor(max_workers=2)

    futures = []

    for i in range(1, 2_000):
        futures.append( executor1.submit(task_generate_data, i) )

    from concurrent.futures import wait

    wait(futures)

    return [future.result() for future in futures]

async def task_generate_first_2k_asyncio():
    import asyncio

    from concurrent.futures import ThreadPoolExecutor

    executor1 = ThreadPoolExecutor(max_workers=2)

    loop1 = asyncio.get_event_loop()
    
    futures = []

    for i in range(1, 2_000):
        future = loop1.run_in_executor(executor1, task_generate_data, i)
        futures.append(future)

    times = []
    for future in futures:
        await asyncio.ensure_future(future, loop=loop1)
        times.append(future.result())

    return times

# times = task_generate_first_2k_sync()
# times = task_generate_first_2k_async()
import asyncio
loop2 = asyncio.get_event_loop()
times = loop2.run_until_complete(task_generate_first_2k_asyncio())

print(sum(times) / len(times))

    