# python3 -m pip install tk
import tkinter as tk

# Es la ventana con los botones de minimizar, maximizar y cerrar
app = tk.Tk()

app.title("App Descargas")
app.geometry("600x400")
app.eval('tk::PlaceWindow . center')

# El panel interno de la venta
frame1 = tk.Frame(app, padx=10, pady=10)
frame1.grid()

entry1 = tk.Entry(frame1, takefocus=True)
entry1.grid(row=0, column=0)

label1 = tk.Label(frame1, text="Hola :D")
label1.grid(row=1, column=0)

def on_click1():
    print("Hola:", entry1.get())
    label1.config(text=f"Hola {entry1.get()}")

button1 = tk.Button(frame1, text="Pulsame", command=on_click1)
button1.grid(row=2, column=0)

frame1.pack()

app.mainloop()