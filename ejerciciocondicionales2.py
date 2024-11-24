import math

a = float(input("Introduce el coeficiente a (grado 2): "))
b = float(input("Introduce el coeficiente b (grado 1): "))
c = float(input("Introduce el coeficiente c (constante): "))

discriminante = b**2 - 4*a*c


if discriminante > 0:
    
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print(f"Soluciones de la ecuación de segundo grado: {a}x² + {b}x + {c} = 0")
    print("Tiene dos raíces reales.")
    print(f"La primera raíz es x1 = {x1}")
    print(f"La segunda raíz es x2 = {x2}")
elif discriminante < 0:
    
    preal = -b / (2 * a)
    pimag = math.sqrt(-discriminante) / (2 * a)
    print(f"Soluciones de la ecuación de segundo grado: {a}x² + {b}x + {c} = 0")
    print("Tiene dos raíces complejas.")
    print(f"La primera raíz es x1 = {preal} + i{pimag}")
    print(f"La segunda raíz es x2 = {preal} - i{pimag}")
else:
    x1 = -b / (2 * a)
    print(f"Soluciones de la ecuación de segundo grado: {a}x² + {b}x + {c} = 0")
    print("Tiene dos raíces iguales.")
    print(f"x1 = x2 = {x1}")

