numeros = []
cantidad = int(input("¿Cuántos números deseas ingresar? "))

for _ in range(cantidad):
    numero = int(input("Ingresa un número: "))
    numeros.append(numero)
    
numeros.sort()

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista original ordenada:", numeros)
print("Números pares:", pares)
print("Números impares:", impares)


