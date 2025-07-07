from tkinter import * 
from tkinter import ttk

def calcular(*args):
    try:
        valor = float(pies.get())
        metros.set((0.3048 * valor * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass

raiz = Tk()
raiz.title("Pies a metros")

marcoPrincipal = ttk.Frame(raiz,padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0 , sticky=(N,W,E,S))
marcoPrincipal.columnconfigure(0,weight=1)
marcoPrincipal.rowconfigure(0,weight=1)

pies = StringVar()
metros = StringVar()

txtPies = ttk.Entry(marcoPrincipal, width=7, textvariable=pies)
txtPies.grid(column=2, row=1,sticky=(W,E))

ttk.Label(marcoPrincipal, textvariable=metros).grid(column=2,row=2,sticky=(W,E))
ttk.Button(marcoPrincipal, text="Calcular", command=calcular).grid(column=3,row=3,sticky=W)

ttk.Label(marcoPrincipal, text="pies").grid(column=3,row=1,sticky=W)
ttk.Label(marcoPrincipal, text="es equivalente a:").grid(column=1,row=2,sticky=E)
ttk.Label(marcoPrincipal, text="metros").grid(column=3,row=2,sticky=W)

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5,pady=5)

txtPies.focus()
raiz.bind('<Return>',calcular)

raiz.mainloop()