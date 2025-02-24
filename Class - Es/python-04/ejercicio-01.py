#Crear un archivo y escribir contenidos en el

# read - Solo lecturas
# write - Escritura en el archivo o mejor dicho sobreescribir
# append - añadir informacion sin borrar el contenido que ya existe
# exclusive creation - crear un archivo nuevo y dara error si ya existe
# r+ - (read & write) permite leer y poder escribir el mismo archivo


with open("Prueba_contendio.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, como estas.")
    
print("El archivo a sido creado.")