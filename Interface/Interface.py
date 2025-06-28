from tkinter import * 
from tkinter import ttk
import tkinter as tk
import csv
from tkinter import messagebox



def actualizar_tabla():

    for item in treeview.get_children():
        treeview.delete(item)

    with open('bd.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            treeview.insert('', tk.END, values=row)

    treeview.pack(expand=True, fill='both')


def validaciones():
    if(nombre.get() == ""):
        messagebox.showerror(message="Falta información: Nombre", title="Error")
        return
    elif(paterno.get() == ""):
        messagebox.showerror(message="Falta información: Apellido Paterno", title="Error")
        return
    elif(materno.get() == ""):
        messagebox.showerror(message="Falta información: Apellido Materno", title="Error")
        return
    elif(correo.get() == ""):
        messagebox.showerror(message="Falta información: Correo", title="Error")
        return
    elif(movil.get() == ""):
        messagebox.showerror(message="Falta información: Movil", title="Error")
        return
    elif(estado.get() == ""):
        messagebox.showerror(message="Falta información: Estado", title="Error")
        return
    elif(status.get() == ""):
        messagebox.showerror(message="Seleccione una ocupación", title="Error")
        return
    elif(leer.get() == False and musica.get() == False and videojuegos.get() == False):
        messagebox.showerror(message="Seleccione por lo menos una aficion", title="Error")
        return

    guardar()
    



def guardar():
    print("Guardado", status.get(),estado.get())
    print(nombre.get(),paterno.get(),materno.get(),correo.get(),movil.get())
    print(leer.get(),musica.get(),videojuegos.get())
    _leer = "NO"
    _musica = "NO"
    _videos = "NO"

    if(leer.get() == True):
        _leer = "SI"
    
    if(musica.get() == True):
        _musica = "SI"

    if(videojuegos.get() == True):
        _videos = "SI"
    
    with open('./bd.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre.get(), paterno.get(),materno.get(),correo.get(),movil.get(),_leer,
                         _musica,_videos,status.get(),estado.get()])
        
    messagebox.showinfo(message="Información guardada exitosamente", title="Éxito")

    cancelar()
  

def cancelar():
    nombre.set("")
    status.set("")
    estado.set("")
    paterno.set("")
    materno.set("")
    correo.set("")
    movil.set("")
    leer.set(False)
    musica.set(False)
    videojuegos.set(False)

raiz = Tk()
raiz.title("Registros")


status = StringVar()
estado = StringVar()
nombre = StringVar()
paterno = StringVar()
materno = StringVar()
correo = StringVar()
movil = StringVar()
leer = BooleanVar()
musica = BooleanVar()
videojuegos = BooleanVar()

notebook = ttk.Notebook()

marcoPrincipal = ttk.Frame(raiz,padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0 , sticky=(N,W,E,S))

marcoPrincipal2 = ttk.Frame(raiz,padding="3 3 12 12")
marcoPrincipal2.grid(column=0, row=0 , sticky=(N,W,E,S))

marco1 = ttk.Frame(marcoPrincipal,padding="10 10 12 12", relief="raised", width= 200)
marco1.grid(column=0, row=0 , sticky=(N,W))

ttk.Label(marco1, text="Nombre: ",width=9).grid(column=1,row=1,sticky=(E),padx=10,pady=5)
txtUsuario = ttk.Entry(marco1, width=30, textvariable=nombre).grid(column=2,row=1,sticky=(W),padx=10,pady=5)

ttk.Label(marco1, text="A Paterno: ",width=9).grid(column=1,row=2,sticky=(E),padx=10,pady=5)
txtUsuario = ttk.Entry(marco1, width=30, textvariable=paterno).grid(column=2,row=2,sticky=(W),padx=10,pady=5)

ttk.Label(marco1, text="A Materno: ",width=9).grid(column=1,row=3,sticky=(E),padx=10,pady=5)
txtUsuario = ttk.Entry(marco1, width=30, textvariable=materno).grid(column=2,row=3,sticky=(W),padx=10,pady=5)

ttk.Label(marco1, text="Correo: ",width=9).grid(column=1,row=4,sticky=(E),padx=10,pady=5)
txtUsuario = ttk.Entry(marco1, width=30, textvariable=correo).grid(column=2,row=4,sticky=(W),padx=10,pady=5)

ttk.Label(marco1, text="Móvil: ",width=9).grid(column=1,row=5,sticky=(E),padx=10,pady=5)
txtUsuario = ttk.Entry(marco1, width=30, textvariable=movil).grid(column=2,row=5,sticky=(W),padx=10,pady=5)

marco2 = ttk.Frame(marcoPrincipal,padding="3 3 12 12",relief="raised")
marco2.grid(column=0, row=1 , sticky=(W,S))

ttk.Label(marco2, text="Aficiones: ").grid(column=0,row=0,sticky=(W))
ttk.Checkbutton(marco2, text="Leer",width=11, variable=leer).grid(column=0,row=1,sticky=(E))
ttk.Checkbutton(marco2, text="Música",width=11,variable=musica).grid(column=1,row=1,sticky=(E))
ttk.Checkbutton(marco2, text="Videojuegos",width=11,variable=videojuegos).grid(column=2,row=1,sticky=(E))

marco3 = ttk.Frame(marcoPrincipal,padding="3 3 12 12")
marco3.grid(column=0, row=2, sticky=(S,W))

ttk.Button(marco3, text="Guardar", command=validaciones, width= 15).grid(column=0,row=0,sticky=W)
ttk.Label(marco3, text="            ").grid(column=1,row=0,sticky=(E))
ttk.Button(marco3, text="Cancelar", command=cancelar, width= 15).grid(column=2,row=0,sticky=E)

marco4 = ttk.Frame(marcoPrincipal,padding="3 60 12 12")
marco4.grid(column=1, row=0, sticky=(N,S,E,W))

ttk.Radiobutton(marco4, text="Estudiante", variable=status, value = 'Estudiante').grid(column=1,row=0,sticky=(N,S,E,W))
ttk.Radiobutton(marco4, text="Empleado", variable=status, value = 'Empleado').grid(column=1,row=1,sticky=(N,S,E,W))
ttk.Radiobutton(marco4, text="Desempleado", variable=status, value = 'Desempleado').grid(column=1,row=2,sticky=(S,E,W))

marco5 = ttk.Frame(marcoPrincipal,padding="3 30 12 12")
marco5.grid(column=1, row=1, sticky=(N,S,E,W))
comboEstados = ttk.Combobox(marco5, textvariable=estado)
comboEstados.grid(column=0, row=0)
comboEstados['values'] = ("Aguascalientes","Baja California","Baja California Sur","Campeche","Chiapas","Chihuahua","Ciudad de México",
                          "Coahuila","Colima","Durango","Estado de México","Guanajuato","Guerrero","Hidalgo","Jalisco","Michoacán","Morelos",
                          "Nayarit","Nuevo León","Oaxaca","Puebla", "Querétaro","San Luis Potosí","Sinaloa","Sonora","Tabasco","Tamaulipas",
                          "Tlaxcala","Veracruz","Yucatán","Zacatecas")

for child in marco2.winfo_children():
    child.grid_configure(padx=10,pady=10)

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=15,pady=15)


marco6 = ttk.Frame(marcoPrincipal2,padding="3 3 3 3")
marco6.grid(column=0, row=0, sticky=(N,S,E,W))

columnas = ('Nombre', 'A. Paterno', 'A. Materno','Correo','Móvil','Leer','Música','Videojuegos','Ocupación','Estado')
treeview = ttk.Treeview(marco6, columns=columnas, show='headings',height=20)
for col in columnas:
    treeview.heading(col, text=col)
    treeview.column(col, width=70)

ttk.Label(marcoPrincipal2, text="            ").grid(column=0,row=1,sticky=(E))
ttk.Button(marcoPrincipal2, text="Leer Datos", command=actualizar_tabla).grid(column=0,row=2,sticky=(S,E))
actualizar_tabla()

notebook.add(marcoPrincipal, text="Guardar Registros", padding=5)
notebook.add(marcoPrincipal2, text="Consultar Registros", padding=5)
notebook.pack()

raiz.mainloop()