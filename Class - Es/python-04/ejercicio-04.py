# os.listdir

# read - Solo lecturas
# write - Escritura en el archivo o mejor dicho sobreescribir
# append - añadir informacion sin borrar el contenido que ya existe
# exclusive creation - crear un archivo nuevo y dara error si ya existe
# r+ - (read & write) permite leer y poder escribir el mismo archivo


import os

archivo_actual = input("Introduce el nombre del archivo que deseas cambiar: ")
archivo_nuevo_nombre = input("Introduce el nombre nuevo del archivo: ")


# Verificamos si el archivo existe

if archivo_actual in os.listdir():
    os.rename(archivo_actual, archivo_nuevo_nombre)
    print("El archivo se renombre exitosamente.")
else:
    print("Error: el archivo no existe.")
