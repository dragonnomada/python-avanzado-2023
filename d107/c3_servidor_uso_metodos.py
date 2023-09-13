#
# Métodos Web
# -------------------------------
# Los métodos son estereotipos de cómo debería recibirse la petición web
# Esto permite que podemos diseñar un mismo servicio que se comporte 
# bajo distintos métodos
# Por ejemplo, en la ruta GET /hello nos duevuelve "hola mundo"
# Por ejemplo, en la ruta POST /hello nos duevuelve "hola mundo secreto"
#
# Los métodos web sirven para dividir recursos y formar un ecosistema semántico
# en la nomenclatura de nuestras API (endpoints) de tal forma
# que prodremos crear un apego hacía lo que es un API RESTful
#
# Los métodos principales son:
# GET - Se usa para indicar que el recurso es público y todo queda "sobre" la URL
# POST - Se usa para indicar que el recurso está protegido y viajan cosas "bajo" la URL
# PUT - Similar a POST pero para indicar que se crean nuevos recursos en el servidor
# PATCH - Similar a POST (no muy usado) indica actualizaciones parciales o streaming
# DELETE - Similar a POST pero para indicar la eliminación de recursos en el servidor
#

#
# Ejemplo de un api hello que se comporta diferente con base en el método web

from flask import Flask
from flask import request # request - Es el objeto que tiene TODA la información 
                          #           acerca de la petición, por ejemplo,
                          #           los queries (args)
                          #           el formulario asociado
                          #           datos json, headers, url,
                          #           path, params, etc.

app = Flask(__name__)

@app.route("/api/hello", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def hello():
    # 1. Resolver bajo qué método se accedió a esta ruta

    if request.method == "GET":
        return "Hello GET"
    elif request.method == "POST":
        return "Hello POST"
    elif request.method == "PUT":
        return "Hello PUT"
    else:
        return f"Hello method={request.method}"
    
app.run()

# curl 127.0.0.1:5000/api/hello
# curl -X GET 127.0.0.1:5000/api/hello
# curl -X POST 127.0.0.1:5000/api/hello