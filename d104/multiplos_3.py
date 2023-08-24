contador = 0

for i in range(1, 1_000_001):
    if i % 3 == 0:
        contador += 1

print("Hay {} múltiplos de 3 del 1 al 1,000,000".format(contador))
