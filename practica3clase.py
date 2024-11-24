import math 
print("""PERIMETROS Y AREAS DE FIGURAS GEOMETRICAS
            MARQUE: 1: Cuadrado
                    2: Triangulo
                    3: Circunferencia
                    4: Rombo""")
figura = input("ingrese la opcion")
if figura == "1":
    lado = float(input("ingrese el lado"))
    peri = lado*4
    area = lado*lado
    print("perimetro = ", peri, "Area = ", area)
elif figura == "2":
    lado1 = float(input("ingrese el lado 1 del triangulo"))
    lado2 = float(input("ingrese el lado 2 del triangulo"))
    lado3 = float(input("ingrese el lado 3 del triangulo"))
    if (lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1):
        peri = lado1+lado2+lado3
        semi = peri/2
        area = math.sqrt(semi*(semi-lado1)*(semi-lado2)*(semi-lado3))
        print(f"perimetro: (peri) Area:(area)")
elif figura == "3":
    radio = float(input("ingrese el radio de la circunferencia"))
    peri = math.pi*2*radio
    area = math.pi*radio**2
    print ("perimetro =", peri, "area =", area)
elif figura == "4":
    l = float(input("ingrese el lado del rombo"))
    d = float(input("ingrese el lado mayor"))
    a = float(input("ingrese el lado menor"))
    peri= l*4
    area = (d*a)/2
    print("perimetro=", peri, "area=", area)
else:
    print("NO CORRESPONDE A LAS OPCIONES")
    
                

    
    

                          
    
    
