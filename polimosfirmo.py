class Triangulo():
    def __int__(self):
        self.l1= float(input("ingrese el lado 1: "))
        self.l2= float(input("ingrese el lado 2: "))
        self.l3= float(input("ingrese el lado 3: "))


    def Peri(self):
        print("el perimetro de la figura es: ", self.l1+self.l2+self.l3)

    def Area(self):
        s=(self.l1+self.l2+self.l3)/2
        area=(s*(s-self.l1)*(s-self.l2)*(s-self.l3))**(0.5)
        print("el area de la figura es: ",area)

class Rectangulo():
    def __int__(self):
        self.l1= float(input("ingrese el lado 1: "))
        self.l2= float(input("ingrese el lado 2: "))


    def Peri(self):
        print("el perimetro de la figura es: ", self.l1*2+self.l2*2)

    def Area(self):
        area=(self.l1*self.l2)
        print("el area de la figura es: ",area)

class Circulo():
    def __int__(self):
        self.r= float(input("ingrese el radio 1: "))


    def Peri(self):
        Peri=2*math.pi*self.r
        print("el perimetro de la figura es: ", Peri)

    def Area(self):
        area=(self.l1*self.l2)
        print("el area de la figura es: ",area)


        


    
    
