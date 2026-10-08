import tkinter as tk
from tkinter import messagebox


# ==========================================
# CONVERSIÓN DE PALABRAS A NÚMEROS
# ==========================================

numeros = {
    "cero": 0,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10,
    "once": 11,
    "doce": 12,
    "trece": 13,
    "catorce": 14,
    "quince": 15,
    "dieciseis": 16,
    "dieciséis": 16,
    "diecisiete": 17,
    "dieciocho": 18,
    "diecinueve": 19,
    "veinte": 20,
    "veintiuno": 21,
    "veintidos": 22,
    "veintidós": 22,
    "veintitres": 23,
    "veintitrés": 23,
    "veinticuatro": 24,
    "veinticinco": 25,
    "veintiseis": 26,
    "veintiséis": 26,
    "veintisiete": 27,
    "veintiocho": 28,
    "veintinueve": 29,
    "treinta": 30,
    "cuarenta": 40,
    "cincuenta": 50,
    "sesenta": 60,
    "setenta": 70,
    "ochenta": 80,
    "noventa": 90,
    "cien": 100
}


def convertir_numero(texto):
    texto = texto.lower().strip()

    # Si escribe directamente un número
    try:
        return int(texto)
    except ValueError:
        pass

    # Si escribe el número con letras
    if texto in numeros:
        return numeros[texto]

    # Números como "treinta y dos"
    partes = texto.split()

    if "y" in partes:
        try:
            posicion = partes.index("y")

            primera = numeros[partes[0]]
            segunda = numeros[partes[posicion + 1]]

            return primera + segunda

        except (ValueError, KeyError):
            pass

    raise ValueError


# ==========================================
# CALCULAR
# ==========================================

def calcular():

    try:

        tabla_inicial = convertir_numero(
            entrada_tabla_inicial.get()
        )

        tabla_final = convertir_numero(
            entrada_tabla_final.get()
        )

        multiplicacion_inicial = convertir_numero(
            entrada_mult_inicial.get()
        )

        multiplicacion_final = convertir_numero(
            entrada_mult_final.get()
        )

        if tabla_inicial > tabla_final:
            messagebox.showerror(
                "Error",
                "La tabla inicial no puede ser mayor que la tabla final."
            )
            return

        if multiplicacion_inicial > multiplicacion_final:
            messagebox.showerror(
                "Error",
                "La multiplicación inicial no puede ser mayor que la final."
            )
            return

        resultado.config(state="normal")
        resultado.delete("1.0", tk.END)

        for tabla in range(tabla_inicial, tabla_final + 1):

            resultado.insert(
                tk.END,
                f"\nTABLA DEL {tabla}\n"
            )

            resultado.insert(
                tk.END,
                "────────────────────────\n"
            )

            for numero in range(
                multiplicacion_inicial,
                multiplicacion_final + 1
            ):

                resultado.insert(
                    tk.END,
                    f"{tabla} × {numero} = {tabla * numero}\n"
                )

        resultado.config(state="disabled")

    except ValueError:

        messagebox.showerror(
            "Error",
            "Escribe un número válido o su nombre.\n\n"
            "Ejemplos: 2, dos, diez, veinte, treinta y dos."
        )


# ==========================================
# LIMPIAR
# ==========================================

def limpiar():

    entrada_tabla_inicial.delete(0, tk.END)
    entrada_tabla_final.delete(0, tk.END)
    entrada_mult_inicial.delete(0, tk.END)
    entrada_mult_final.delete(0, tk.END)

    resultado.config(state="normal")
    resultado.delete("1.0", tk.END)
    resultado.config(state="disabled")

    entrada_tabla_inicial.focus()


# ==========================================
# SALIR
# ==========================================

def salir():
    ventana.destroy()


# ==========================================
# VENTANA
# ==========================================

ventana = tk.Tk()

ventana.title("Generador de Tablas")
ventana.geometry("700x750")
ventana.resizable(False, False)
ventana.configure(bg="#0f172a")


# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    ventana,
    text="TABLAS DE MULTIPLICAR",
    font=("Segoe UI", 25, "bold"),
    bg="#0f172a",
    fg="white"
)

titulo.pack(pady=(25, 5))


subtitulo = tk.Label(
    ventana,
    text="Escribe números o sus nombres",
    font=("Segoe UI", 11),
    bg="#0f172a",
    fg="#94a3b8"
)

subtitulo.pack(pady=(0, 20))


# ==========================================
# PANEL
# ==========================================

panel = tk.Frame(
    ventana,
    bg="#1e293b"
)

panel.pack(
    padx=35,
    fill="x"
)


# ==========================================
# CREAR CAMPOS
# ==========================================

def crear_campo(texto, fila, columna):

    etiqueta = tk.Label(
        panel,
        text=texto,
        font=("Segoe UI", 11, "bold"),
        bg="#1e293b",
        fg="white"
    )

    etiqueta.grid(
        row=fila,
        column=columna,
        padx=15,
        pady=(18, 5)
    )

    entrada = tk.Entry(
        panel,
        font=("Segoe UI", 14),
        justify="center",
        bg="#0f172a",
        fg="white",
        insertbackground="white",
        relief="flat",
        width=15
    )

    entrada.grid(
        row=fila + 1,
        column=columna,
        padx=15,
        pady=(0, 18),
        ipady=7
    )

    return entrada


entrada_tabla_inicial = crear_campo(
    "Tabla inicial",
    0,
    0
)

entrada_tabla_final = crear_campo(
    "Tabla final",
    0,
    1
)

entrada_mult_inicial = crear_campo(
    "Multiplicación inicial",
    2,
    0
)

entrada_mult_final = crear_campo(
    "Multiplicación final",
    2,
    1
)


# ==========================================
# BOTONES
# ==========================================

panel_botones = tk.Frame(
    ventana,
    bg="#0f172a"
)

panel_botones.pack(pady=20)


boton_calcular = tk.Button(
    panel_botones,
    text="CALCULAR",
    command=calcular,
    font=("Segoe UI", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=14,
    height=2
)

boton_calcular.grid(
    row=0,
    column=0,
    padx=7
)


boton_limpiar = tk.Button(
    panel_botones,
    text="LIMPIAR",
    command=limpiar,
    font=("Segoe UI", 11, "bold"),
    bg="#475569",
    fg="white",
    activebackground="#334155",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=14,
    height=2
)

boton_limpiar.grid(
    row=0,
    column=1,
    padx=7
)


boton_salir = tk.Button(
    panel_botones,
    text="SALIR",
    command=salir,
    font=("Segoe UI", 11, "bold"),
    bg="#dc2626",
    fg="white",
    activebackground="#b91c1c",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=14,
    height=2
)

boton_salir.grid(
    row=0,
    column=2,
    padx=7
)


# ==========================================
# RESULTADOS
# ==========================================

etiqueta_resultado = tk.Label(
    ventana,
    text="RESULTADOS",
    font=("Segoe UI", 14, "bold"),
    bg="#0f172a",
    fg="white"
)

etiqueta_resultado.pack(pady=(5, 10))


marco_resultado = tk.Frame(
    ventana,
    bg="#1e293b"
)

marco_resultado.pack(
    padx=35,
    fill="both",
    expand=True
)


resultado = tk.Text(
    marco_resultado,
    font=("Consolas", 13),
    bg="#020617",
    fg="#e2e8f0",
    insertbackground="white",
    relief="flat"
)

resultado.pack(
    padx=15,
    pady=15,
    fill="both",
    expand=True
)

resultado.config(state="disabled")


# ==========================================
# ATAJOS
# ==========================================

ventana.bind(
    "<Return>",
    lambda event: calcular()
)

ventana.bind(
    "<Escape>",
    lambda event: salir()
)


entrada_tabla_inicial.focus()


# ==========================================
# EJECUTAR
# ==========================================

ventana.mainloop()