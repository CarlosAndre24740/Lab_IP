import math
import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        numero1 = float(entrada_numero1.get())
        numero2 = float(entrada_numero2.get())
        if not (math.isfinite(numero1) and math.isfinite(numero2)):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error de entrada", "Debes ingresar valores numéricos válidos.")
        return

    match opcion.get():
        case "+":
            resultado = numero1 + numero2
        case "-":
            resultado = numero1 - numero2
        case "*":
            resultado = numero1 * numero2
        case "/":
            if numero2 == 0:
                messagebox.showerror("Error matemático", "No se puede dividir entre cero.")
                return
            resultado = numero1 / numero2
        case _:
            messagebox.showwarning("Operación no seleccionada", "Selecciona una operación.")
            return

    variable_resultado.set(f"{resultado:g}")


def limpiar():
    entrada_numero1.delete(0, tk.END)
    entrada_numero2.delete(0, tk.END)
    variable_resultado.set("")
    opcion.set("")
    entrada_numero1.focus()


def salir():
    if messagebox.askyesno("Salir", "¿Deseas cerrar la calculadora?"):
        ventana.destroy()


ventana = tk.Tk()
ventana.title("Calculadora Básica - ChagoUaz")
ventana.geometry("500x560")
ventana.resizable(False, False)

tk.Label(ventana, text="CALCULADORA BÁSICA", font=("Arial", 22, "bold")).pack(pady=(20, 5))
tk.Label(ventana, text="Introducción a la Programación", font=("Arial", 11)).pack(pady=(0, 20))

grupo_datos = tk.LabelFrame(ventana, text=" DATOS DE ENTRADA ", font=("Arial", 11, "bold"), padx=20, pady=15)
grupo_datos.pack(padx=30, fill="x")

tk.Label(grupo_datos, text="Primer número:", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entrada_numero1 = tk.Entry(grupo_datos, width=20, font=("Arial", 12), justify="center")
entrada_numero1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(grupo_datos, text="Segundo número:", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
entrada_numero2 = tk.Entry(grupo_datos, width=20, font=("Arial", 12), justify="center")
entrada_numero2.grid(row=1, column=1, padx=10, pady=10)

opcion = tk.StringVar(value="")

grupo_operaciones = tk.LabelFrame(ventana, text=" OPERACIÓN ", font=("Arial", 11, "bold"), padx=20, pady=15)
grupo_operaciones.pack(padx=30, pady=15, fill="x")

tk.Radiobutton(grupo_operaciones, text="Suma (+)", variable=opcion, value="+", font=("Arial", 11)).grid(row=0, column=0, padx=25, pady=8, sticky="w")
tk.Radiobutton(grupo_operaciones, text="Resta (-)", variable=opcion, value="-", font=("Arial", 11)).grid(row=0, column=1, padx=25, pady=8, sticky="w")
tk.Radiobutton(grupo_operaciones, text="Multiplicación (*)", variable=opcion, value="*", font=("Arial", 11)).grid(row=1, column=0, padx=25, pady=8, sticky="w")
tk.Radiobutton(grupo_operaciones, text="División (/)", variable=opcion, value="/", font=("Arial", 11)).grid(row=1, column=1, padx=25, pady=8, sticky="w")

variable_resultado = tk.StringVar()

grupo_resultado = tk.LabelFrame(ventana, text=" RESULTADO ", font=("Arial", 11, "bold"), padx=20, pady=15)
grupo_resultado.pack(padx=30, fill="x")

tk.Label(grupo_resultado, text="Resultado:", font=("Arial", 11)).grid(row=0, column=0, padx=10)
tk.Entry(grupo_resultado, textvariable=variable_resultado, width=22, font=("Arial", 14, "bold"),
         justify="center", state="readonly").grid(row=0, column=1, padx=10)

grupo_botones = tk.Frame(ventana)
grupo_botones.pack(pady=20)

tk.Button(grupo_botones, text="CALCULAR", width=12, command=calcular).grid(row=0, column=0, padx=5)
tk.Button(grupo_botones, text="LIMPIAR", width=12, command=limpiar).grid(row=0, column=1, padx=5)
tk.Button(grupo_botones, text="SALIR", width=12, command=salir).grid(row=0, column=2, padx=5)

tk.Label(ventana, text="ChagoUaz • Introducción a la Programación", font=("Arial", 9)).pack(pady=5)

entrada_numero1.focus()
ventana.mainloop()
