import math

while True:
    print("\n--- Menú de Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Comparar si un número es par o impar")
    print("6. Calcular porcentaje")
    print("7. Funciones trigonométricas (seno, coseno, tangente)")
    print("8. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La suma es: {num1 + num2}")
    
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La resta es: {num1 - num2}")
    
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La multiplicación es: {num1 * num2}")
    
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
            print(f"La división es: {num1 / num2}")
        else:
            print("Error: No se puede dividir entre cero.")
    
    elif opcion == "5":
        num = int(input("Ingrese un número para saber si es par o impar: "))
        if num % 2 == 0:
            print(f"{num} es un número par.")
        else:
            print(f"{num} es un número impar.")
    
    elif opcion == "6":
        total = float(input("Ingrese el total: "))
        porcentaje = float(input("Ingrese el porcentaje: "))
        print(f"{porcentaje}% de {total} es: {total * (porcentaje / 100)}")
    
    elif opcion == "7":
        angulo = float(input("Ingrese el ángulo en grados: "))
        angulo_rad = math.radians(angulo)  
        print(f"Seno de {angulo}°: {math.sin(angulo_rad)}")
        print(f"Coseno de {angulo}°: {math.cos(angulo_rad)}")
        print(f"Tangente de {angulo}°: {math.tan(angulo_rad)}")
    
    elif opcion == "8":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida, por favor intente de nuevo.")
