def carrito (**descripcion):
    print("Los datos de mi carro")
    for clave, valor in descripcion.items():
        print(f"{clave}: {valor}")

carrito(marca = "toyota", año = 2021)