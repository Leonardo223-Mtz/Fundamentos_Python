from tkinter import * 
from tkinter import ttk

raiz = Tk()
labeltexto = ttk.Label(raiz, text = "Etiqueta solo texto")
labeltexto.grid()

imagen = PhotoImage(file= "capibara.png")

labelimage = ttk.Label(raiz)
labelimage.grid()
labelimage['image'] = imagen

labelcombinada = ttk.Label(raiz, text = "Etiqueta combinada", compound="center")
labelcombinada.grid()
labelcombinada['image'] = imagen

raiz.mainloop()

