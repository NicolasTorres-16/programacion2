letra = input("Introduce una letra: ")

if len(letra) != 1:
    print("Error: Debes ingresar solo un carácter.")
else:
    if letra.lower() in "aeiou":
        print("Es una vocal.")
    else:
        print("No es una vocal.")
