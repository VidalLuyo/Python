nombre_archivo = "Python_01.txt"

#Crear y escribir en el archivo

texto = input("Introduce una linea de texto: ")
caracter = input("Introduce un caracter para contarlo: ")

with open(nombre_archivo, "a", encoding="utf-8") as archivo:
    archivo.write(texto)

#Leer los primeros 10 caracteres y el conteo
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read(100)
    conteo = contenido.count(caracter)

print(f"Los primeros 10 caracteres son : {contenido}")
print(f"El caracter aparece un total de : {conteo}")