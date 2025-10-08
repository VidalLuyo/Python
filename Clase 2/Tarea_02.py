#Ejercicio 5
# Escribir un programa que determine si un número ingresado
# por el usuario es positivo, negativo o cero.

numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
