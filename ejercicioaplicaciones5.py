def sumar(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def multiplicar(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

numeros = [1, 2, 3, 4]
print("Suma:", sumar(numeros))
print("Multiplicación:", multiplicar(numeros))


