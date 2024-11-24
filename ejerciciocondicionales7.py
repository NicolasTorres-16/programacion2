nombres = []
n = int(input("¿Cuántos nombres de estudiantes deseas ingresar? "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    nombres.append(nombre)

print("Ahora puedes buscar si un nombre está en la lista.")
consulta = input("Introduce el nombre a buscar: ")

encontrado = False
for nombre in nombres:
    if nombre == consulta:
        encontrado = True
        
if encontrado:
    print(f"{consulta} está en la lista.")
else:
    print(f"{consulta} no está en la lista.")
