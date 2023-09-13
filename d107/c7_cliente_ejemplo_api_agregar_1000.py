import requests

def add_product(name, description, price, units):
    endpoint = "http://127.0.0.1:5000/api/products"
    response = requests.put(endpoint, data={
        "name": name,
        "description": description,
        "price": price,
        "units": units,
    })
    return response.status_code

from concurrent.futures import ThreadPoolExecutor

executor1 = ThreadPoolExecutor(max_workers=4)

futures = [ executor1.submit(add_product, f"Producto {i}", "Sin descripción", 10 * i, 2 * i) \
                    for i in range(1_000) ]

from concurrent.futures import wait

wait(futures)

outputs = [ future.result() for future in futures ]

print(outputs)