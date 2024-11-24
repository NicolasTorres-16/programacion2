l = [0]
entrada = int(input("ingrese un numero positivo"))
pos = 0 
while entrada>=l[pos]:
    l.append(entrada)
    pos += 1
    entrada = int(input("ingrese un numero positivo"))
while entrada < l[pos] and entrada >= 0:
    print("Número no mayor que el anterior. Tienes una última oportunidad.")
    entrada = int(input("Ingrese un número positivo: "))

   
