cadena = input("Ingrese una cadena: ")
indice = 0
contador_mayusculas = 0

while indice < len(cadena):
    caracter = cadena[indice]
    if "A" <= caracter <= "Z":
        contador_mayusculas += 1
    indice += 1

print("La cadena ingresada tiene", contador_mayusculas, "letras mayúsculas.")
