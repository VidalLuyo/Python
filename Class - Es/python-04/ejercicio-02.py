#lEER el archivo


# read - Solo lecturas
# write - Escritura en el archivo o mejor dicho sobreescribir
# append - añadir informacion sin borrar el contenido que ya existe
# exclusive creation - crear un archivo nuevo y dara error si ya existe
# r+ - (read & write) permite leer y poder escribir el mismo archivo


with open("Prueba_01.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    
print(f"Contenido del archivo:\n {contenido}")