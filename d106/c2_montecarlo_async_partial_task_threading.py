#
# Método de Montencarlo
# ---------------------------------------------------
# Consiste en un problema basado en una solución
# que construye en el tiempo con valores aleatorios
# Podemos dividir la solución para paralelizarla 
#

from random import uniform

def task_hints_partial(k):
    # hints = 0
    # for _ in range(k):
    #     x = uniform(-1, 1)
    #     y = uniform(-1, 1)
    #     d = (x ** 2 + y ** 2) ** 0.5
    #     if d <= 1:
    #         hints += 1
    # return hints
    return sum([ (uniform(-1, 1) ** 2 + uniform(-1, 1) ** 2) ** 0.5 <= 1 \
                for _ in range(k)])

# Total
n_samples = 10_000_000

# print(task_hints_partial(n_samples))
# print(task_hints_partial(2_500_000))
# print(task_hints_partial(2_500_000))
# print(task_hints_partial(2_500_000))
# print(task_hints_partial(2_500_000))

# Lotes / Batches
m_chunks = 4

hints_list = []

def task():
    k = int(n_samples / m_chunks)
    hints = task_hints_partial(k)
    hints_list.append(hints)

from threading import Thread

threads = []

for _ in range(m_chunks):
    t = Thread(target=task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(hints_list)
print(sum(hints_list))
print(sum(hints_list) / n_samples)

pi = 4 * sum(hints_list) / n_samples

print("𝜋 ≃", pi)