# Ejercicio 01: 
#Escribir un programa que verifique si un número ingresado por el usuario 
# es mayor, menor o igual a 10.
     
#input representa pedirle una consulta al usuario  
     
numero = int(input("Ingresa un número: "))

if numero > 10:
    print("El numero es mayor que 10")
elif numero < 10:
    print("El numero es menor que 10")
else:
    print("El numero es igual a 10")
