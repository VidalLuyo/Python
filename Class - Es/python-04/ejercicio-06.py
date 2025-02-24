import os

if os.path.exists("Prueba_contendio_vacio.txt"):
    os.remove("Prueba_contendio_vacio.txt")
    print("Archivo eliminado")
else:
    print("Error el archivo no existe")