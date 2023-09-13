#
# Servidores
# -----------------------------------
# El servidor es un programa que escucha un puerto específico de la máquina
# y atiende las solicitudes TCP mediante un protocolo que generalmente es HTTP
# HTTP -> Híper-texto (Hyper-Text Transfer Protocol)
# Los datos son en realidad paquetes en un híper-texto
# Una imagen es un híper-texto, un texto es un híper-texto, un archivo, etc.
# Podemos decir que el híper-texto es la unión entre `bytes` + meta-datos (mime-types)
#
# El servidor divide el puerto en rutas, y cada ruta atiende un recurso
# Cada ruta es conocida como un `endpoint`
#

# 1. Utilizar un framework capaz de escuchar y reservar el puerto
# python3 -m pip install flask
from flask import Flask

# 2. Generar un servidor al que registrarle rutas para proveer recursos
app = Flask(__name__) # __name__ representa el contexto de ejecución

# 3. Registrar las rutas en el servidor hacía los recursos
@app.route("/") # localhost:5000/
def home():
    return "Hola mundo"

# 4. Iniciar el servidor en un puerto específico
app.run() # app.run(port=5000)
          # app.run(port=5000, host="dragon.com")

#
# curl - es un programa de la terminal que nos permite
#        hacer peticiones web desde la línea de comandos
#
# curl [flags] url [options]
#