from tkinter import * 
from tkinter import ttk

raiz = Tk()

estado = StringVar()

comboEstados = ttk.Combobox(raiz, textvariable=estado)
comboEstados.grid()
comboEstados['values'] = ("Jalisco","Nayarit","Colima","Michoacan")

raiz.mainloop()

