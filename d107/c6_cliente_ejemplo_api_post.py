import requests

def update_product_name_by_id(id, name):
    endpoint = f"http://127.0.0.1:5000/api/product/{id}"
    response = requests.post(endpoint, data={
        "name": name
    })
    return response.status_code

def update_product_price_by_id(id, price):
    endpoint = f"http://127.0.0.1:5000/api/product/{id}"
    response = requests.post(endpoint, data={
        "price": price
    })
    return response.status_code

s1 = update_product_name_by_id(826380571, "Coca Cola hackeda >: )")
s2 = update_product_price_by_id(461785922, 0.01)

print(s1)
print(s2)