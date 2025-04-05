# Paso 1 y 2: Crear archivo y pedir tres frases
archivo = "datos.txt"

linea1 = input("Ingrese la primera línea: ")
linea2 = input("Ingrese la segunda línea: ")
linea3 = input("Ingrese la tercera línea: ")

with open(archivo, "w") as f:
    f.write(linea1 + "\n")
    f.write(linea2 + "\n")
    f.write(linea3 + "\n")

# Paso 3: Leer el contenido del archivo y mostrarlo
with open(archivo, "r") as f:
    contenido = f.readlines()

print("\nContenido del archivo:")
for linea in contenido:
    print(linea.strip())

# Paso 4: Contar la cantidad de palabras en el archivo
total_palabras = sum(len(linea.split()) for linea in contenido)
print(f"\nEl archivo contiene {total_palabras} palabras en total.")
