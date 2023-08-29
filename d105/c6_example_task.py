def task_write_file(n):
    with open(f"output/demo.txt", "w") as f:
        for _ in range(n):
            f.write("Hola mundo ..." * 100 + "\n")

# Síncrona
# task_write_file(100_000)

# Asíncrona
from threading import Thread

hilo = Thread(target=task_write_file, args=(100_00,))

hilo.start()

print("Se inicializó la tarea")

hilo.join()

print("Se completó la tarea")