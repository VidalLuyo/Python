def num(n):
    return n * 2

numeros = [1, 2, 3, 4]
resultado = map(num, numeros)

print(list(resultado))