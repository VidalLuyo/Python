#el usuario debe escribir 3 datos enteros y que realize la operacion que se multiplique y se divide el numero 
# 1 y el numero 2 debe multiplicarse y el resultado de ellos 2 devera dividirse
def numero():
     num1 = int(input("ingresa primer numero:"))
     num2 = int(input("ingresa segundo numero:"))
     num3= int(input("ingresa tercer numero:"))
     return num1 * num2 / num3

print(f"el resultado final es: {numero()}")
