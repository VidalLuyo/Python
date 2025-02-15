#Suma de dos números aleatorios
import random

def suma():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    return num1 + num2

print(suma())

