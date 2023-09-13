import requests

response = requests.get("http://127.0.0.1:5000/api/products")

print("=== RESPUESTA ===")
print("--- Status Code ---")
print(response.status_code)
print("--- Headers ---")
print(response.headers)
print("--- Content-Type ---")
print(response.headers["Content-Type"])
# print("--- Text ---") # in text
# print(response.text)
# print("--- Content ---") # in binary
# print(response.content)
print("--- Json ---") # in json
products = response.json()
print(products)

print()

print("=== PRODUCTOS ===")
for product in products:
    print("[{}] {} ${:.2f} ({} units)".format(product["id"], product["name"], \
          product["price"], product["units"]))