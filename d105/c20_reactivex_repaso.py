from reactivex import create, operators

users_ids = [1, 34, 56, 98, 123, 97]

# === Parte 1 - Stream de usuarios ===

# Observable nos permite observar un siguiente valor
# Scheduler nos permite acceder al hilo programado para el stream
def users_stream(observable, scheduler):
    import requests
    for id in users_ids:
        response = requests.get("https://randomuser.me/api?seed={}".format(id))
        data = response.json()
        results = data["results"]
        user = results[0]
        fullname = user["name"]["first"] + " " + user["name"]["last"]
        email = user["email"]
        username = user["login"]["username"]
        password = user["login"]["password"]

        observable.on_next({
            "fullname": fullname,
            "email": email,
            "username": username,
            "password": password
        })
    observable.on_completed()

users_source = create(users_stream)

# # users_source.subscribe(lambda user: print(user))

# emails_source = users_source.pipe(
#     operators.map(lambda user: user["email"])
# )

# emails_source.subscribe(lambda email: print(email))

# === Parte 2 - Stream de imágenes ===

def user_pictures_stream(observer, scheduler):
    import requests
    for id in users_ids:
        url = "https://i.pravatar.cc/400?u={}".format(id)
        response = requests.get(url)
        picture = response.content
        # with open("....png", "wb") as f:
        #    f.write(picture)
        observer.on_next(picture)
    observer.on_completed()

user_pictures_source = create(user_pictures_stream)

# user_pictures_source.subscribe(lambda picture: print(len(picture)))

# === Parte 3 - Fusionar los flujos de datos e imágenes ===

users_zipped_source = users_source.pipe(
    operators.zip(user_pictures_source)
)

# user_zipped_source.subscribe(lambda z: print("User: {} | Picture: {} bytes".format(z[0], len(z[1]))))

# Ejemplo avanzado
email_pictures_source = users_zipped_source.pipe(
    operators.map(lambda z: (z[0]["email"], len(z[1]))),
    operators.filter(lambda w: w[1] >= 25000)
)

email_pictures_source.subscribe(lambda w: print(w))