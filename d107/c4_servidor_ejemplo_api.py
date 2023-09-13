from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

products_temp = []

def load_products():
    global products_temp
    try:
        import json
        with open("data/products.json", "r") as file:
            products = json.load(file)
            products_temp = products
            return products
    except:
        return []
    
def save_products(products):
    import json
    with open("data/products.json", "w") as file:
        json.dump(products, file)
        return products

def product_find_by_id(id):
    for product in products_temp:
        if product["id"] == int(id):
            return product

@app.route("/api/product/<id>", methods=["GET", "POST", "PUT"])
def api_product_by_id(id):
    try:
        if request.method == "GET":
            print("Recuperando el producto:", id)

            product = product_find_by_id(id)

            if not product == None:
                return product
            else:    
                response = make_response("El producto no existe")
                response.status_code = 400 # Bad Request

            return response
        elif request.method == "POST":
            load_products()

            product = product_find_by_id(id)

            if not request.form == None:
                name = request.form.get("name")
                if not name == None:
                    # TODO: Verficar que el nuevo nombre sea válido
                    product["name"] = name

                price = request.form.get("price")
                if not price == None:
                    # TODO: Verficar que el nuevo nombre sea válido
                    product["price"] = float(price)

            save_products(products_temp)

            return product
    except Exception as e:
        response = make_response(str(e))
        response.status_code = 500 # Internal Server Error
        return response


@app.route("/api/products", methods=["GET", "POST", "PUT"])
def api_products():
    if request.method == "GET":
        return load_products()
    elif request.method == "PUT":
        # Recuperamos del formulario los datos del producto
        try:
            name = request.form.get("name")
            description = request.form.get("description")
            price = float(request.form.get("price"))
            units = float(request.form.get("units"))

            if name == None or name == "" or name.strip() == "":
                raise Exception("El nombre pude ser vacío")
            
            if price < 0.01:
                raise Exception("El precio no pude ser inferior a 1 centavo")
            
            if units < 0:
                raise Exception("Las unidades no pueden ser negativas")
            
            products = load_products()

            import random

            products.append({
                "id": random.randint(1, 1_000_000_000),
                "name": name,
                "description": description,
                "price": price,
                "units": units,
            })

            try:
                save_products(products)
            except Exception as e:
                print("Error al guardar los productos:", e)
                response = make_response("Error al guardar los productos")
                response.status_code = 500 # Internal Server Error
                return response
            
            return "ok"
        except Exception as e:
            response = make_response(str(e))
            response.status_code = 400 # Bad Request
            return response

app.run()