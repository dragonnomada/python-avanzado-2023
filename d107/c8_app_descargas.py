# python3 -m pip install tk
import tkinter as tk

# Lógica global

descargas_pentientes = [
    "https://example.com/fake.jpg"
]
descargas_iniciadas = []
descargas_finalizadas = []

on_downloads_pending_update = lambda url, downloads: print("Descargas pendientes actualizadas:", url, downloads)
on_downloads_started_update = lambda url, downloads: print("Descargas pendientes actualizadas:", url, downloads)
on_downloads_ended_update = lambda url, downloads: print("Descargas pendientes actualizadas:", url, downloads)

# TASK
def download_next():
    if len(descargas_iniciadas) == 0:
        # TODO: Cambiar por un alert en la ventana
        print("!!! No hay más cosas por descargar")
        return
    
    url = descargas_iniciadas.pop(0) # FIFO (First-In -> First-Out)

    # # Emitir un evento para actualizar las descargas pendientes en la interfaz
    # on_downloads_pending_update(url, descargas_pentientes)

    # descargas_iniciadas.append(url)

    on_downloads_started_update(url, descargas_iniciadas)

    print(f"Descargando: {url}")

    from time import sleep
    from random import randint

    sleep(randint(1, 6)) # Aleatorio de 1 a 6s

    # TODO: Descargar el archivo y guardarlo en local
    import requests
    
    response = requests.get(url)

    if not response.ok:
        print("Falló la descarga:", url)
        descargas_pentientes.append(url)
        on_downloads_pending_update(url, descargas_pentientes)
        return
    
    print("OK", url)
    
    import time

    filename = str(int(time.time())) + ".png"

    print(filename)

    with open(f"downloads/{filename}", "wb") as file:
        print("Guardando imagen:", filename, len(response.content))
        file.write(response.content)

    # index = descargas_iniciadas.index(url)
    # descargas_iniciadas.pop(index)

    on_downloads_started_update(url, descargas_iniciadas)

    descargas_finalizadas.append(url)

    on_downloads_ended_update(url, descargas_finalizadas)

# Es la ventana con los botones de minimizar, maximizar y cerrar
app = tk.Tk()

app.title("App Descargas")
app.geometry("600x400")
app.eval('tk::PlaceWindow . center')

# El panel interno de la venta
frame1 = tk.Frame(app, padx=10, pady=10)
frame1.grid()

frame2 = tk.Frame(frame1, padx=10, pady=10)
frame2.grid(row=4, column=0)

var1 = tk.StringVar()
var1.set("https://")

listvar1 = tk.StringVar()
listvar2 = tk.StringVar()
listvar3 = tk.StringVar()

entry1 = tk.Entry(frame1, textvariable=var1, takefocus=True)
entry1.grid(row=0, column=0)

label1 = tk.Label(frame1, text="Agrega una URL por descargar")
label1.grid(row=1, column=0)

label2 = tk.Label(frame2, text="Descargas pendientes:")
label2.grid(row=0, column=0)

label3 = tk.Label(frame2, text="Descargas iniciadas:")
label3.grid(row=0, column=1)

label3 = tk.Label(frame2, text="Descargas finalizadas:")
label3.grid(row=0, column=2)

def when_downloads_pending_update(url, downloads):
    listvar1.set("\n".join(downloads))
    label1.config(text=f"Se agregó la descarga de la url: {url}")

def when_downloads_started_update(url, downloads):
    listvar2.set("\n".join(downloads))
    label1.config(text=f"Se inició la descarga de la url: {url}")

def when_downloads_ended_update(url, downloads):
    listvar3.set("\n".join(downloads))
    label1.config(text=f"Se finalizó la descarga de la url: {url}")

on_downloads_pending_update = when_downloads_pending_update
on_downloads_started_update = when_downloads_started_update
on_downloads_ended_update = when_downloads_ended_update

def on_click1():
    url = var1.get()
    var1.set("https://")
    descargas_pentientes.append(url)
    label1.config(text=f"Se agregó: {url}")

    print(descargas_pentientes)

    listvar1.set("\n".join(descargas_pentientes))

button1 = tk.Button(frame1, text="Agregar descarga", command=on_click1)
button1.grid(row=2, column=0)

from concurrent.futures import ThreadPoolExecutor

executor1 = ThreadPoolExecutor(max_workers=2)

def on_click2():
    print("Descargando todos en un hilo...")
    while len(descargas_pentientes) > 0:
        url = descargas_pentientes.pop()
        descargas_iniciadas.append(url)

    on_downloads_pending_update(None, descargas_pentientes)
    on_downloads_started_update(None, descargas_iniciadas)

    # TASK IN THREAD-POOL
    for _ in range(len(descargas_iniciadas)):
        executor1.submit(download_next)

button1 = tk.Button(frame1, text="Descargar todos", command=on_click2)
button1.grid(row=3, column=0)

listbox1 = tk.Listbox(frame2, listvariable=listvar1)
listbox1.grid(row=1, column=0)

listbox2 = tk.Listbox(frame2, listvariable=listvar2)
listbox2.grid(row=1, column=1)

listbox3 = tk.Listbox(frame2, listvariable=listvar3)
listbox3.grid(row=1, column=2)

frame1.pack()

entry1.focus()

when_downloads_pending_update(None, descargas_pentientes)

app.mainloop()