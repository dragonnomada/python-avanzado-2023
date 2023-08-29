to_plot = []

# Función con 3-argumentos
def generar_imagen_aleatoria(id, ancho, alto):
    import numpy as np

    # Generar una matriz aleatoria de NxM
    im = np.random.uniform(0, 255, (alto, ancho)) # Alto consumo

    # with open(f"output/demo_{id}.png", "wb") as f:
    #     # TODO: Transformar el im.data en formato PNG
    #     f.write(im.data)
    
    # python3 -m pip install Pillow
    from PIL import Image
    im = Image.fromarray(im)
    im = im.convert('L')
    im.save(f"output/demo_{id}.png")

    # import matplotlib.pyplot as plt

    # # La gráfica de la imagen
    # plt.plot(im)
    # # Guardamos la imagen generada según su id
    # plt.savefig(f"output/demo_{id}.png")
    # # plt.show()

# SÍNCRONA (~27.167s) 20 * 1.3s ~= 27s

# generar_imagen_aleatoria(1, 4000, 4000)
# generar_imagen_aleatoria(2, 4000, 4000)
# generar_imagen_aleatoria(3, 4000, 4000)
# generar_imagen_aleatoria(4, 4000, 4000)

# for i in range(20):
#     generar_imagen_aleatoria(i + 101, 4000, 4000)

# ASÍNCRONA (~9.081s) [4 * 5] | 5 * 1.8s ~= 9s

from threading import Thread

# Almacenar la referencia a cada hilo
hilos = []

# Registrar de forma iterativa 20 hilos
for i in range(20):
    # Crear un hilo que al inicializarse (con el `hilo.start()`)
    # mande a llamar a la función `generar_imagen_aleatoria`
    # con los 3 argumentos variables (i, 4000, 4000)
    hilo_i = Thread(target=generar_imagen_aleatoria, args=(i, 4000, 4000))
    # Almacenamos el hilo creado
    hilos.append(hilo_i)

# Inicializamos la ejecución de cada hilo
for hilo in hilos:
    hilo.start() # Inicializa el hilo registrado y almacenado

# Opcionalmente podemos esperar a que todos los hilos hayan acabado
for hilo in hilos:
    hilo.join() # Preguntar si el hilo terminó y sino esperarlo

print("Se han generado todas las imágenes (los hilos finalizaron)")
