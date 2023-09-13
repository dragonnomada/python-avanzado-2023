# def foo(name):
#     return f"Hola {name}"

# mensaje = foo("Pepe") # str -> "Hola Pepe"

# print(mensaje)

#
# Un decorador es una función que recibe otra función para hacer algo con ella,
# Por ejemplo, pasarle parámetros o mandarla a llamar y usar sus resultados
#

# Una función decoradora es una función que recibe a otra como parámetros
# ésta función tiene que devolver la función decorada, es decir,
# tiene devolver una función que calcule el resultado tomando en cuenta
# a la otra función, para crear una modificación del resultado original 
# (función no-decorada) y la alteración de nuestra función decoradora
def add_date(func):
    # Creamos una función intermedia que llame a la función a decorar
    # y decore el resultado para modificarlo o hacer algo más avanzado
    def compute_result():
        result = func()
        from datetime import datetime
        now = datetime.now().isoformat()
        # Regresamos el resultado decorado
        return f"[{now}] {result}"
    # Esta función reemplazará a la función original
    return compute_result

# Agregamos el decorador a nuestra función
# y ahora la función está decorada
@add_date
def hello():
    return "Hola mundo"

# Al llamar a `hello()` se obtendrá el resultado decorado
print(hello())