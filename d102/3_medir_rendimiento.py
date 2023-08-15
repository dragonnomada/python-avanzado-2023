import timeit

times = timeit.repeat(
    #stmt="y = [xi ** 2 for xi in x]", # ~3.8s
    stmt="y = list(map(lambda xi: xi ** 2, x))", # ~6.16s
#     stmt=
# """
# y = []
# for xi in x:
#     y.append(xi ** 2)
# """, # ~4.4s
    setup="x=list(range(1, 1_000_001))",
    number=1,
    repeat=100
)

total = sum(times)
delta = sum(times) / len(times)

print(total)
print(delta)