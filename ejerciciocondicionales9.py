numero_anterior = int(input("Ingrese un número entero: "))

while True:
    numero_actual = int(input("Ingrese otro número entero: "))
    if numero_actual < numero_anterior:
        print("Ese número es menor que el anterior. Programa terminado.")
        break
    numero_anterior = numero_actual
