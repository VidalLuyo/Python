def datos (a, b,*producto, **precio):
    print(f"a: {a}, b:{b}")
    print("Productos: ", producto)
    print("Precios: ", precio)

datos("Pan", "Leche", "Tamal", Pan = 2, Leche = 4, Tamal = 4.5)