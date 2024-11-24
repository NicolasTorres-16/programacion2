def relacion(a,b):
    if a > b:
        return True
    elif a < b:
        return False
    else:
        return "empate"
num1 = float(input("ingrese el primer numero "))
num2 = float(input("ingrese el segundo numero "))
resultado = relacion(num1, num2)
print(f"La relación entre {num1} y {num2} es: {resultado} ")










