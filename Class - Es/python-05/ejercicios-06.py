original = input("Ingrese el nombre del archivo original: ")
copia = input("Ingresa el nombre del archivo copia: ")


try:
    with open(original, "r") as archivo_o:
        contenido = archivo_o.read()
        
    with open(copia, "w") as archivo_n:
        archivo_n.write(contenido.upper())
        
    print(f"Se creo la copia del archivo {original}")
    
except FileNotFoundError:
    print(f"El archivo {original} no exite")