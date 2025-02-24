#ACTUALIZAR el archivo

# read - Solo lecturas
# write - Escritura en el archivo o mejor dicho sobreescribir
# append - añadir informacion sin borrar el contenido que ya existe
# exclusive creation - crear un archivo nuevo y dara error si ya existe
# r+ - (read & write) permite leer y poder escribir el mismo archivo


with open("Python_01.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Hola Vidal 1.\n")
    archivo.write("Hola Vidal 2.\n")
    archivo.write("Hola Vidal 3.\n")
    archivo.write("Hola Vidal 4.\n")
    archivo.write("Hola Vidal 5.\n")
    archivo.write("Hola Mundo\n")
    
print("ACTUALIZACION COMPLETA")