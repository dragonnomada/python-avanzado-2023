from rx import of
from rx import operators as op

source = of(1, 2, 3)

composed = source.pipe(
    op.map(lambda x: x ** 2)
)

composed.subscribe(lambda y: print(f"Y={y}"))