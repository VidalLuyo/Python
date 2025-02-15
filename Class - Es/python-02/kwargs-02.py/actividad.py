def registrar_es():
    nombre = input("Ingresame tu nombre: ")
    edad = input("Ingresame tu edad: ")

    estudiante(Nombre = nombre, Edad = edad)

def estudiante(**datos):
    print("Infomacion del estudiante: ")
    for variable, dato in datos.items():
        print(f"{variable}: {dato} ")


registrar_es()