def presentacion(nombre, pais):
    return f"Hola me llamo {nombre} y estoy en el pais de {pais}"

nombre = input("Ingresa tu nombre: ")
pais = input("Ingresa tu pais: ")

print(presentacion(nombre, pais))

print()

def suma1 (num1, num2):
    return num1 + num2

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))

print(f"La suma de los dos numeros es: {suma1 (num1, num2)}")
print(f"La deficion de los datos numericos con el numero {num1 + num2}")