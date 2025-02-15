def carrito (**descripcion):
    print("Los datos de mi carro")
    for clave, valor in descripcion.items():
        print(f"Mi {clave} es: {valor}")

carrito(marca = "toyota", año = 2021)