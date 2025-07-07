from tkinter import * 
from tkinter import ttk

raiz = Tk()
boton = ttk.Button(raiz, text = "Botón solo texto")
boton.grid()

imagen = PhotoImage(file= "capibara.png")

botonimage = ttk.Button(raiz)
botonimage.grid()
botonimage['image'] = imagen

botoncombinada = ttk.Button(raiz, text = "Botón combinado", compound="bottom")
botoncombinada.grid()
botoncombinada['image'] = imagen

chebtn =  ttk.Checkbutton(raiz, text = "Opción 1")
chebtn.grid()

raiz.mainloop()

