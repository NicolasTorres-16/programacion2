eje=[1,2,3,4]
try:
    a=int(input('ingrese un numero'))
    b=int(input('ingrese un numero'))
    print('El cociente es: ', a/b)
    print(eje[a])

except (ValueError, TypeError, IndexError):
    print('Error en el ingreso de un numero')
    print('El error fue: ', sys.exc_info()[0])

except ZeroDivisionError:
    print('Tiene una división indeterminada')
    print('Error de ingreso del divisor')
