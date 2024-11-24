numeros = []
contador = 0

while contador < 5:
    numero = int(input(f"Ingrese el número {contador + 1}: "))
    numeros.append(numero)
    contador += 1

suma_negativos = 0
suma_positivos = 0
cantidad_positivos = 0

for numero in numeros:
    if numero < 0:
        suma_negativos += numero
    elif numero > 0:
        suma_positivos += numero
        cantidad_positivos += 1

if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
else:
    promedio_positivos = 0

print(f"La sumatoria de los números negativos es: {suma_negativos}")
print(f"El promedio de los números positivos es: {promedio_positivos:.2f}")
