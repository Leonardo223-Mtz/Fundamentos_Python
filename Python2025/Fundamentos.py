#Archivo para operadores aritmeticos

def Suma(a,b):
    return a+b

def Resta(a,b):
    return a - b

def nuevoTema(tema):
    return f"\n---------- {tema} ----------\n"

def ejemplo(x):
    x += 1
    return x

if __name__ == "__main__":

    valor = 12
    valor1 = ejemplo(valor) 
    print(valor, valor1)
    

    print(nuevoTema("Operadores aritmeticos"))
    print("Operador suma, 5 + 6 = ",Suma(5,6))
    print("Operador resta, 5 - 6 = ",Resta(5,6))
    print("Operador Multiplicacion, 5 * 6 = ",5*6)
    print("Operador Division, 5 / 6 = ",5/6)
    print("Operador Division entera, 5 // 6 = ",5//6)
    print("Operador Módulo, 5 % 6 = ",5%6)
    print("Operador Exponente, 5 ** 6 = ",5**6)
    print("Operador +, +5 = ",+5)
    print("Operador -, -5 = ",-5)

    ''' Comentario de varias lineas
    Línea 2 
    Etc....'''

    print(nuevoTema("Operadores lógicos")) 
    print("Operador not")
    print("not True:", not True)
    print("not False:", not False)

    print("Operador and")
    print("True and True:", True and True)
    print("True and False:", True and False)
    print("False and True:", False and True)
    print("False and False:", False and False)

    print("Operador or")
    print("True or True:", True or True)
    print("True or False:", True or False)
    print("False or True:", False or True)
    print("False or False:", False or False)


    print(nuevoTema("Operadores de comparacion "))
    x = 8
    y = 8
    print(x == y)
    print(x != y)
    print(x > y)
    print(x < y)
    print(x >= y)
    print(x <= y)


    print(nuevoTema("Variables"))
    a,b,c = 1,4,"Bienvenido"
    print(a)
    print(b)
    print(c)

    print(nuevoTema("Enteros"))
    x = 569
    y = 54684
    z = 7894165465464620101846168797605654064684046846046846804646546
    b = 0b1111
    h = 0xFF
    #print(x*y*z)
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
    print(b,type(b))
    print(h,type(h))


    print(nuevoTema("Flotantes"))
    q = 985.63
    w = 1420.2
    print(q,type(q))
    print(w,type(w))


    print(nuevoTema("Complejos"))
    q = 3 + 2j
    w = -63j
    print(q,type(q))
    print(w,type(w))
    print(q + w)

    print(nuevoTema("Booleanos"))
    q = True
    w = False
    print(q,type(q))
    print(w,type(w))


    print(nuevoTema("Listas"))
    list = [2,5.6,"Cadena"]
    print(list)
    print(list[1])
    list.append("Leo")
    list[0] = "Hola"
    print(list)
    list.insert(1,"elemento1")
    print(list)
    print(list.index(5.6))
    print(list.index("Leo"))
    list.append([1,2,3,4,5])
    print(list)
    print(list[5][0])


    print(nuevoTema("Tuplas"))
    tupla = (23,67,"Tuplas")
    print(tupla)
    print(tupla[2])
    print(tupla.index(23))


    print(nuevoTema("Conjuntos"))
    conjunto = {23,67,12}
    print(conjunto)
    conjunto.add(44)    
    print(conjunto)

    print(nuevoTema("Diccionario"))
    diccionario = {"Nombre":"Leonardo",
                "Edad":33,
                "Estado": "Casado",
                "Telefono":"3317890987"}
    
    print(diccionario)
    print(diccionario["Edad"])


    print(nuevoTema("Cadena"))
    cadena1 = "Esto es una cadena"
    cadena2 = 'Esto es otra cadena'
    cadena_multilinea = '''Esto   es una 
    cadena multilinea   con tabuladores y 
    saltos de linea'''

    print(cadena1)
    print(cadena2)
    print(cadena_multilinea)

    print(cadena1[::2])
    print(cadena1[2])
    print(cadena1[:5])
    print(cadena1[2:])
    print(cadena1[5:-5])
   # print(cadena1[:-5])
    print(cadena1[::-1])
    print(cadena_multilinea[26])

    a = float(input("Valor de a: "))
    
    b = float(input("Valor de b: "))

    print(f"Solución:{-b/a}" if a != 0 else print("Soluciones infinitas") if b == 0 else print("No se puede dividir por cero"))





  
