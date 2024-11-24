peso = float(input("Ingrese su peso(kilogramos) "))
estatura = float(input("Ingrese su estatura(metros) "))
imc = round(peso / estatura**2, 2)
print(f"Tu índice de masa corporal (IMC) es: {imc}")
