import csv
    
with open('archivo_salida.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Encabezado1', 'Encabezado2'])    
    writer.writerow(['Dato1', 'Dato2'    ])        