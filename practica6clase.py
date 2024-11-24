lado1 = float(input("ingrese el lado 1 del triangulo"))
lado2 = float(input("ingrese el lado 2 del triangulo"))
lado3 = float(input("ingrese el lado 3 del triangulo"))

if (lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1):
    print("los datos ingresados pertenecen a un triangulo")
    if (lado1==lado2==lado3):
        print("triangulo equilatero")
    elif(lado1!=lado2!=lado3):
        print("triangulo escaleno")
    else:
        print("triangulo isoceles")
else:
    print("los datos no son de un triangulo")

        

        
        
        
        
    
    
