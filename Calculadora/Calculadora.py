from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

def solo_numeros(caracter):
    print(f"Caracter: {caracter}")
    try:
        a = float(caracter)
        return True
    except Exception as ex:
        if(caracter == ''):
            print("Vacio")
            pantalla.set("")
        

        return False

def tecla_presionada(evento):
    print("Tecla", evento.keysym)
    tecla = convertir_tecla(evento.keysym)
    print(tecla)
    if(tecla == '<-'):
        pass
    elif(tecla == 'Return'):
        calcular_operacion()
        entrada.focus()
        entrada.icursor(tk.END)
    elif(tecla == 'Escape'):
        pantalla.set("")
    elif validar_caracter(tecla) == False:
        return "break"
    
    

def convertir_tecla(tecla):
    if(tecla == "plus"):
        return "+"
    elif(tecla == 'minus'):
        return "-"
    elif(tecla == 'slash'):
        return "/"
    elif(tecla == 'asterisk'):
        return "*"
    elif(tecla == 'BackSpace'):
        return "<-"
    elif(tecla == 'period'):
        return "."
    else:
        return tecla

def calcular_raiz():
    numero = float(pantalla.get())
    pantalla.set(numero**(0.5))

def calcular_operacion():
    suma = pantalla.get().split('+')
    mult = pantalla.get().split('*')
    divi = pantalla.get().split('/')
    rest = pantalla.get().split('-')
    print(suma)
    print(mult)
    print(divi)
    print(rest)
    if(len(suma)== 2):
        pantalla.set(float(suma[0]) + float(suma[1]))
    elif(len(mult)== 2):
        pantalla.set(float(mult[0]) * float(mult[1]))
    elif(len(divi)== 2):
        pantalla.set(float(divi[0]) / float(divi[1]))
    elif(len(rest)== 2):
        pantalla.set(float(rest[0]) - float(rest[1]))

def validar_caracter(t):
    try:
        if t in botones_permitidos:
            operacion = False
            for i in pantalla.get():
                if i in operaciones:
                    operacion = True
            
            if pantalla.get()[-1] in operaciones and t in operaciones:
                return False
            elif "." in pantalla.get() and t == '.' and operacion == True and pantalla.get().count(".") == 1:
                return True
            elif "." in pantalla.get() and t == '.':
                return False
            elif "+" in pantalla.get() and t in operaciones:
                return False
            elif "-" in pantalla.get() and t in operaciones:
                return False
            elif "*" in pantalla.get() and t in operaciones:
                return False
            elif "/" in pantalla.get() and t in operaciones:
                return False
            else:
                return True
        else:
            return False
    except: return True

def click_boton(t):
    try:
        if validar_caracter(t):
            pantalla.set(pantalla.get() + t)
        elif(t == 'C'):
            pantalla.set("")
        elif(t == '<-'):
            pantalla.set(pantalla.get()[:-1])
        elif(t == '√'):
            calcular_raiz()
        elif(t == '='):
            calcular_operacion()

        entrada.focus()
        entrada.icursor(tk.END)
    except:
        pantalla.set(pantalla.get() + t)

raiz = Tk()
raiz.title("Calculadora")

pantalla = StringVar()


marcoPrincipal = ttk.Frame(raiz,padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0 , sticky=(N,W,E,S))

#vcmd = raiz.register(solo_numeros)
#entrada = ttk.Entry(marcoPrincipal, font=("Segoe UI", 18), justify='right', textvariable=pantalla, validate="key", validatecommand=(vcmd, "%P"))
entrada = ttk.Entry(marcoPrincipal, font=("Segoe UI", 18), justify='right', textvariable=pantalla)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

ancho = 6

operaciones = ('+','-','*','/')
botones_permitidos = ('1','2','3','4','5','6','7','8','9','0','BackSpace','Up','Right','Left','Down','.','+','-','*','/')
operaciones_permitidas = ('plus','minus','asterisk','slash','Return','percent')

botones = [
    ('C', 1, 0), ('√', 1, 1), ('%', 1, 2), ('<-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

for (texto, fila, columna) in botones:
    boton = ttk.Button(marcoPrincipal, text=texto, width= ancho,command=lambda t=texto: click_boton(t))
    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=2,pady=2)

entrada.bind("<Key>", tecla_presionada)

raiz.mainloop()