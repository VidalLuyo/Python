# Número aleatorio y doble
import random

def numero_doble():
    num = random.randint(1, 10)
    print(f"El numero aleatorio es: {num}")
    return num * 2

print(numero_doble())
