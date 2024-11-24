def Separar(lista):
    pares = []
    impares = []
    lista.sort()
    for num in lista:
        if num % 2 == 0:
            pares.append(num)  
        else:
            impares.append(num) 
    
    return pares, impares
lista_numeros = [8, 3, 6, 1, 7, 4, 2, 5]
pares, impares = Separar(lista_numeros)

print("Números pares:", pares)
print("Números impares:", impares)<z
