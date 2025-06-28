from tkinter import * 
from tkinter import ttk

raiz = Tk()
raiz.title("Inicio de Sesión")


marcoPrincipal = ttk.Frame(raiz,padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0 , sticky=(N,W,E,S))
marcoPrincipal.columnconfigure(0,weight=1)
marcoPrincipal.rowconfigure(0,weight=1)

ttk.Label(marcoPrincipal, text="Usuario: ").grid(column=1,row=1,sticky=(E))
txtUsuario = ttk.Entry(marcoPrincipal, width=30).grid(column=2,row=1,sticky=(W))

ttk.Label(marcoPrincipal, text="Password: ").grid(column=1,row=2,sticky=(E))
txtUsuario = ttk.Entry(marcoPrincipal, show = "*", width=30 ).grid(column=2,row=2,sticky=(W))

ttk.Button(marcoPrincipal, text="Ingresar").grid(column=2,row=3,sticky=E)

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=10,pady=10)


raiz.mainloop()