def calcular_voltaje(corriente, resistencia):
    return corriente * resistencia

def calcular_corriente(voltaje, resistencia):
    return voltaje / resistencia

def calcular_resistencia(voltaje, corriente):
    return voltaje / corriente

def seleccionar_calculo():
    print("Selecciona lo que deseas calcular:")
    print("1. Voltaje (V)")
    print("2. Corriente (I)")
    print("3. Resistencia (R)")
    opcion = input("Introduce el número de tu elección: ")
    return opcion

def main():
    opcion = seleccionar_calculo()

    if opcion == '1':  
        corriente = float(input("Introduce la corriente (I) en amperios: "))
        resistencia = float(input("Introduce la resistencia (R) en ohmios: "))
        voltaje = calcular_voltaje(corriente, resistencia)
        print(f"El voltaje es: {voltaje} V")
    
    elif opcion == '2':  
        voltaje = float(input("Introduce el voltaje (V) en voltios: "))
        resistencia = float(input("Introduce la resistencia (R) en ohmios: "))
        corriente = calcular_corriente(voltaje, resistencia)
        print(f"La corriente es: {corriente} A")
    
    elif opcion == '3':  
        voltaje = float(input("Introduce el voltaje (V) en voltios: "))
        corriente = float(input("Introduce la corriente (I) en amperios: "))
        resistencia = calcular_resistencia(voltaje, corriente)
        print(f"La resistencia es: {resistencia} ohmios")
    
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")


main()
