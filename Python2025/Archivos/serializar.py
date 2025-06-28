import pickle

info=[35,96,54,63.3]

with open("./Python2025/Archivos/ArchivoSerial","wb") as binFile:
    pickle.dump(info,binFile)

print("Archivo Binario creado")



with open("./Python2025/Archivos/ArchivoSerial","rb") as binFile:
    lista = pickle.load(binFile)
    print(lista)

print("Lista reconstruida")