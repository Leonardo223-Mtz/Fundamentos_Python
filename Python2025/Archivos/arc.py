file = open("EjemploTexto.txt","w")
file.write("Este es la primera línea del archivo.")
file.close()

lista = ["Fresa", "Mango", "Papaya"]

with open("EjemploTexto.txt","a") as file:
    for e in lista:
        file.write(e + "\n")

print("Lista en el archivo")

lista2 = ["Honda", "Suzuki", "BMW"]

with open("EjemploTexto.txt","a") as file:
    file.writelines(lista2)

print("Lista con writelines\n\n")

print("Leer todo el archivo")
with open("EjemploTexto.txt","r") as file:
    print(file.read())


print("\n\nLeer dos lineas y 5 caracateres")
with open("EjemploTexto.txt","r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5))


print("\n\nAlmacenar el contenido en una lista y mostrar el ultimo elemmento")
with open("EjemploTexto.txt","r") as file:
   contenido = file.readlines()
   print(type(contenido))
   print(contenido[-1])


