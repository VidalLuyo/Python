#



def suma(**detalles):
    total = sum(detalles.values())
    print(f"El total es : {total}")

suma(pan = 2, pera = 1.5)