#Adivina el número (simple)

import random

def numero():
    num = random.randint(1,5)
    intentos = int(input("Adivina el numero el numero escondido: "))
    return intentos == num

print("Felicidad Acertaste el numero" if numero() else "Fallaste")