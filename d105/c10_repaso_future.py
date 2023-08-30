from concurrent.futures import Future

# 1. Establecer un objeto cuyo resultado es a futuro
future_person = Future()

# ...

# 2. Diseñar una función que espere cuándo el resultado
#    futuro esté ajustado
# 9. Se ejecuta finalmente la función con el future listo
def wait_person(future_person):
    # 10. Recuperamos el valor ajustado a futuro
    person = future_person.result()

    # 11. Procesamos los datos a futuro como se deba
    print(person)

# ...

# 3. Registramos la función que procesará
#    el valor a futuro cuándo esté listo
future_person.add_done_callback(wait_person)
# 8. El valor a futuro ya está ajustado
#    por lo que se llama a la función registrada

# ...

# 4. Diseñamos una función que recupere información
#    en tiempo diferido (dependiente de la respuesta de un servidor)
def fetch_person():
    import requests
    
    # 5. Hacemos la petición que durará un tiempo prolongado
    response = requests.get("https://randomuser.me/api")

    import json

    data = json.loads(response.text)

    results = data["results"]

    user = results[0]

    name = user["name"]["first"] + " " + user["name"]["last"]
    gender = user["gender"]
    email = user["email"]
    picture = user["picture"]["medium"]

    # 6. Construimos un resultado
    person = {
        "name": name,
        "gender": gender,
        "email": email,
        "picture": picture
    }

    # 7. Establecemos el valor a futuro
    future_person.set_result(person)

# ... En espera de ejecutar (4.)

# Ahora ya podemos ejecutar `fetch_person`
# y procesar los resultados
fetch_person()