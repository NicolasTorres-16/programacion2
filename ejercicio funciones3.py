def  hallar_mayor_menor(a,b):
    if a > b:
        mayor= a
        menor = b
    else:
        mayor = b
        menor = a
    return mayor, menor
num1 = 4
num2 = 2
mayor, menor = hallar_mayor_menor(num1,num2)
print("mayor: ", mayor, "menor: " ,menor)
