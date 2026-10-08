import tkinter as tk

def saludar():
    texto.config(text="porque es necesario para el futuro del pais")

ventana = tk.Tk()
ventana.title("mi programa numero 1")
ventana.geometry("1000x800")
ventana.configure(bg="#371e3b")

texto = tk.Label(
    ventana,
    text="porque el pais necesita ingenieros en software",
    font=("Arial", 20, "bold"),
    bg="#2a1e3b",
    fg="red"
)

texto.pack(pady=50)

boton = tk.Button(
    ventana,
    text="presiona el boton bro",
    font=("Arial", 18),
    command=saludar
)

boton.pack()

ventana.mainloop()
