cajero = input("ingrese una de las opciones: retiro, consulta, tra, recibos")
match cajero:
    case "retiro":
        plata = int(input("cuanto va a retirar"))
        print("retiro exitoso")
    case "consulta":
        print("su saldo es de: $150.000.000")
    case "tra":
        print ("tranferencia exitosa")
    case "recibos":
        print("agua, luz, internet")
    
