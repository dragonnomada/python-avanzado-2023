def suma(a, b):
    return a + b

c = suma(1, 2)

print(c)

def elevar_cuadrado(x):
    return x ** 2

print(elevar_cuadrado(10))

y = list(map(elevar_cuadrado, [1, 2, 3, 4, 5, 6]))

print(y)

def elevar_cuadrado_menos_promedio(x):
    global p # Accede al valor de p cuándo llega a la función
    return (x - p) ** 2

p = sum([1, 2, 3, 4, 5, 6]) / len([1, 2, 3, 4, 5, 6])

y = list(map(elevar_cuadrado_menos_promedio, [1, 2, 3, 4, 5, 6]))

print(y)

def descargar_url():
    global url
    print(f"Descargando {url}...")

url = "http://fake.com/1.pdf"
a = 123
b = 456
# ...
descargar_url()
url = "http://fake.com/2.png"
descargar_url()

context = {
    "a": False,
    "b": False,
    "c": False,
    "ans": 0
}

def task1():
    global context
    # ... sleep(60)
    context["a"] = True
    context["ans"] = 1

def task2():
    global context
    while not context["a"]:
        # ... sleep(.01)
        continue
    print("La tarea 1 fue resuelta, por lo que obtenemos el ans")
    # ...
    context["ans"] = context["ans"] * 2
    context["b"] = True

def task3():
    global context
    # ...
    context["c"] = True
