#For - La suma de los 10 primeros numeros
suma = 0

for i in range(1,11):
    suma += i

print(f"La suma total es : {suma}")

#While - Pedir numeros al usuario hasta que ingrese 0

num = int(input("Ingresa un numero y si quieres salis ingresa el '0': "))

while num != 0:
    num = int(input("Ingresa otro numero o ingresa el '0' para salir: "))

print("Se termino el programa")
