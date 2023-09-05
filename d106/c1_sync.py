for id in [98, 123, 97, 34]:
    import requests
    url = "https://randomuser.me/api?seed={}".format(id)
    response = requests.get(url)
    data = response.json()
    results = data["results"]
    user = results[0]
    name = user["name"]["first"] + " " + user["name"]["last"]
    print(f"Proceso: {id}", name)