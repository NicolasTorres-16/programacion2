class Calculadora:
    def __init__(self):
        self.valor1=int(input("Ingrese el primer valor: "))
        self.valor2=int(input("Ingrese el segundo valor: "))
    def suma(self):
        suma=self.valor1+self.valor2
        print("El resultado de la suma de los valores es: ",suma)
        self.menu()
    def resta(self):
        resta=self.valor1-self.valor2
        print("El resultado de la resta de los valores es: ",resta)
    def multiplicacion(self):
        pro=self.valor1*self.valor2
        print("El resultado de la multiplicación de los valores es: ",pro)
    def division(self):
        div=self.valor1/self.valor2
        print("El resultado de la división de los valores es: ",div)
    def imprimir(self):
        print("Los valores son: ")
        print("Valor 1: ",self.valor1)
        print("Valor 2: ",self.valor2)
    def menu(self):
        opcion = input("ingrese 1:suma, 2: resta, 3: producto, 4:division, 5:mostrar ")
        if opcion == "1":
            self.suma()
        elif opcion =="2":
            self.resta()
        elif opcion =="3":
            self.multiplicacion()
        elif opcion =="4":
            self.division()
        elif opcion =="5":
            self.imprimir()
        elif opcion =="6":
            exit()
        else:
            print("error de ingreso")
            self.menu()

while True:
    calcular=Calculadora()
