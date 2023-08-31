from reactivex import create

frutas = ["Manzana", "Mango", "Kiwi", "Pera"]
colores = ["Rojo", "Amarillo", "Verde", "Naranja", "Café"]

def frutas_on_time(observer, scheduler):
    from time import sleep
    from random import choice

    # for _ in range(100):
    while True:
        fruta = choice(frutas) + " " + choice(colores)
        observer.on_next(fruta)
        sleep(1)

    # observer.on_completed()

source1 = create(frutas_on_time)

# source1.subscribe(lambda fruta: print(f"Fruta = {fruta}"))

from reactivex import operators

# El flujo acepta una "tubería" de operadores, es decir, 
# operadores que serán aplicados en secuencia (pipe-operators)

source2 = source1.pipe(
    operators.map(lambda fruta: fruta.split(" ")),
    operators.filter(lambda parts: parts[1] == "Rojo"),
    operators.map(lambda parts: parts[0] + " " + parts[1])
)

source2.subscribe(lambda fruta: print(f"Fruta *roja = {fruta}"))


