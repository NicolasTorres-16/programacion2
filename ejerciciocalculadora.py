##class Calculadora():
##    def __init__(self, num1, num2):
##        self._num1=num1
##        self._num2=num2
##
##    def suma(self):
##        resultado=self._num1 + self._num2
##        print(f»El resultado de la suma es: {self._num1} + {self._num2}={resultado}»)
##
##    def resta(self):
##        resultado=self._num1 – self._num2
##        print(f»El resultado de la resta es: {self._num1} – {self._num2}={resultado}»)
##
##    def division(self):
##        resultado=self._num1 // self._num2
##        print(f»El resultado de la divisón es: {self._num1} // {self._num2}= {resultado}»)
##
##    def multiplicacion(self):
##        resultado=self._num1 * self._num2
##        print(f»El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}»)
##
##operacion=Calculadora(10, 5)
##operacion.suma()
##
##operacion=Calculadora(20, 5)
##operacion.resta()
##
##operacion=Calculadora(15, 3)
##operacion.division()
##
##operacion=Calculadora(8, 4)
##operacion.multiplicacion()




class Calculadora:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def suma(self):
        resultado = self._num1 + self._num2
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    def resta(self):
        resultado = self._num1 - self._num2
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

    def division(self):
        if self._num2 != 0:
            resultado = self._num1 / self._num2
            print(f"El resultado de la división es: {self._num1} / {self._num2} = {resultado}")
        else:
            print("Error: División por cero no permitida.")

    def multiplicacion(self):
        resultado = self._num1 * self._num2
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

operacion = Calculadora(10, 5)
operacion.suma()

operacion = Calculadora(20, 5)
operacion.resta()

operacion = Calculadora(15, 3)
operacion.division()

operacion = Calculadora(8, 4)
operacion.multiplicacion()
