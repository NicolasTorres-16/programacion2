import math  
radio = float(input("Ingrese el valor del radio del círculo: "))
área = math.pi * radio**2
perímetro = 2 * math.pi * radio

print(f"El área del círculo es: {área:.2f}")
print(f"El perímetro del círculo es: {perímetro:.2f}")
