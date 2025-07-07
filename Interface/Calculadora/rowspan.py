'''rom sympy import sympify, N, sqrt


expresion_str = "(2*3) / (8+7) + sqrt(9)"
expresion = sympify(expresion_str)

# Evaluar simbólicamente
print("Expresión simbólica:", expresion)

# Evaluar numéricamente (decimal)
resultado_decimal = N(expresion)
print("Resultado decimal:", resultado_decimal)'''

'''import tkinter as tk

def abrir_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Ventana Secundaria")
    etiqueta = tk.Label(nueva_ventana, text="Esta es una nueva ventana")
    etiqueta.pack()

root = tk.Tk()
root.title("Ventana Principal")

boton = tk.Button(root, text="Abrir Nueva Ventana", command=abrir_ventana)
boton.pack()

root.mainloop()'''

import tkinter as tk
from tkinter import ttk

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("300x200")

        self.etiqueta_resultado = ttk.Label(self, text="Resultado: ")
        self.etiqueta_resultado.pack(pady=10)

        self.boton_abrir = ttk.Button(self, text="Abrir Ventana Secundaria", command=self.abrir_ventana_secundaria)
        self.boton_abrir.pack(pady=10)

    def abrir_ventana_secundaria(self):
        self.ventana_secundaria = VentanaSecundaria(self, self.actualizar_resultado)
        self.ventana_secundaria.grab_set() # Evita que se pueda interactuar con la ventana principal

    def actualizar_resultado(self, resultado):
        self.etiqueta_resultado.config(text=f"Resultado: {resultado}")
        self.ventana_secundaria.destroy()


class VentanaSecundaria(tk.Toplevel):
    def __init__(self, ventana_principal, callback):
        super().__init__(ventana_principal)
        self.ventana_principal = ventana_principal
        self.callback = callback
        self.title("Ventana Secundaria")
        self.geometry("250x150")

        self.etiqueta_entrada = ttk.Label(self, text="Introduce un valor:")
        self.etiqueta_entrada.pack(pady=5)

        self.entrada = ttk.Entry(self)
        self.entrada.pack(pady=5)

        self.boton_enviar = ttk.Button(self, text="Enviar", command=self.enviar_datos)
        self.boton_enviar.pack(pady=10)

    def enviar_datos(self):
        valor = self.entrada.get()
        self.callback(valor)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
