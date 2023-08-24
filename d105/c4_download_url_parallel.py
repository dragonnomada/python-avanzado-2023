# Librería Regex -> Identificar patrones regulares
import re

from c1_tareas_seriadas import download, write_content

def task(url):
    url = url.strip()
    filename = re.search("denue[\w\_\-]+_csv.zip", url).group(0)

    # TAREA 1 - DESCARGAR
    print("DESCARGANDO:", url)
    content = download(url)

    # TAREA 2 - ESCRIBIR
    print("GUARDANDO:", filename)
    write_content("output/" + filename, content)

from threading import Thread

with open("urls.txt", "r") as f: # f - nombre del archivo

    threads = [] # "n" hilos almacenados

    print("Registrando cada URL como un task (hilo) a descargar...")

    for url in f.readlines()[:5]: # line-by-line
        t = Thread(target=task, args=(url,)) # target + args (task + params)
        threads.append(t)

    print("Inicializando todas las descargas...")

    for t in threads:
        t.start()

    print("Se han inicializado todas las descargas")

    print("Esperando a que finalicen todas las descargas...")

    for t in threads:
        t.join() # RETIENE LA EJECUCIÓN HASTA QUE ESTE HILO ACABE

    print("Todas las descargas están completas")