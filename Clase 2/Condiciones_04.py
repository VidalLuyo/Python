# Ejercicio 03: 
# Escribir un programa que determine si un estudiante aprobó o reprobó.
# Si la nota es mayor o igual a 7, debe imprimir "Aprobado".
# Si es menor, debe imprimir "Reprobado"

nota = float(input("Ingrese la nota del estudiante: "))

if nota >= 7:
    print("Aprobó")
else:
    print("Reprobó")