from concurrent.futures import ProcessPoolExecutor

#
# ThreadPoolExecutor - Recibe una tarea para ejecutarla en un hilo independiente
#                       (con memoria local a este programa)
# ProcessPoolExecutor - Recibe una tarea para ejecutarla en un proceso independiente
#                        (con memoria propia an su propio programa)
#

def write_random(id):
    # output/sample_{id}.txt
    words = ["manzana", "hola", "de", "el", "como", "hoy", "mundo", "pera", "ejemplo", "\n"]
    from random import choice
    from re import sub
    filename = f"output/sample_{id}.txt"
    with open(filename, "w") as file:
        for _ in range(1_000_000):
            word = choice(words)
            file.write(sub(r"\n\s", "\n", word + " "))
    return filename

# bootstap
if __name__ == "__main__":
    # SYNC
    # write_random(1)
    # write_random(2)
    # write_random(3)

    executor1 = ProcessPoolExecutor(max_workers=4) # ~ CPUs

    # <future> = executor.submit(<function>, <*args>)

    # === MANUAL ===
    # fut1 = executor1.submit(write_random, 123) # 0,700
    # fut2 = executor1.submit(write_random, 456) # 1,400
    # fut3 = executor1.submit(write_random, 789) # 2,100
    # fut3 = executor1.submit(write_random, 111) # 2,800
    # fut3 = executor1.submit(write_random, 222) # 3,500
    # fut3 = executor1.submit(write_random, 333) # 4,200

    # from concurrent.futures import wait

    # wait([fut1, fut2, fut3])

    # from concurrent.futures import as_completed

    # outputs = as_completed([fut1, fut2, fut3])

    # print(outputs)
    # ==============

    futures = [ executor1.submit(write_random, id) for id in [123, 456, 789, 111, 222, 333] ]

    from concurrent.futures import wait

    wait(futures)

    outputs = [ future.result() for future in futures ]

    print(outputs)
    

