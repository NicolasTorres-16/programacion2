while True:
    print("Seleccione un candidato para votar:")
    print("1. Candidato A")
    print("2. Candidato B")
    print("3. Candidato C")
    print("4. Voto en blanco")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        print("Usted ha votado por el candidato A.")
        break
    elif opcion == "2":
        print("Usted ha votado por el candidato B.")
        break
    elif opcion == "3":
        print("Usted ha votado por el candidato C.")
        break
    elif opcion == "4":
        print("Usted ha votado en blanco.")
        break
    else:
        print("Opción errónea. Intente nuevamente.")
