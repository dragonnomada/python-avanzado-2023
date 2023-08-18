import numpy as np

x1 = np.random.uniform(-1, 1, 5) # .uniform(a, b, n) ~ numpy.random

print(x1)

print("-" * 60)

import random

x2 = []

for i in range(5):
    x2.append(random.uniform(-1, 1)) # .append(e) ~ lista de python

print(x2)

print("-" * 60)

x3 = [ random.uniform(-1, 1) for _ in range(5) ]

print(x3)

print("=" * 60)

# Código inicializador
setup = """
import numpy as np
"""

# Código evaluador
code = """
x = np.random.uniform(-1, 1, 1_000)
"""

import timeit
import numpy as np

times = timeit.repeat(stmt=code, setup=setup, number=1, repeat=1_000)

print(np.mean(times) / 1e-6) # ~ microsegundos

print("-" * 60)

# Código inicializador
setup = """
import random
"""

# Código evaluador
code = """
x = [random.uniform(-1, 1) for _ in range(1_000)]
"""

import timeit
import numpy as np

times = timeit.repeat(stmt=code, setup=setup, number=1, repeat=1_000)

print(np.mean(times) / 1e-6) # ~ microsegundos

print("-" * 60)

# Código inicializador
setup = """
import random
"""

# Código evaluador
code = """
x = []

for _ in range(1_000):
    x.append(random.uniform(-1, 1))
"""

import timeit
import numpy as np

times = timeit.repeat(stmt=code, setup=setup, number=1, repeat=1_000)

print(np.mean(times) / 1e-6) # ~ microsegundos