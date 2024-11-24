class Persona():

    def __init__(self):
        self.nombre=input('ingrese su nombre ')
        self.edad=int(input('ingrese su edad '))
        self.ht=10
        
    def imprimir(self):
        print ('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años', self.ht, ' horas trabajadas')
        
class Sueldo(Persona):
    def __init__(self):
        super().__init__()#heredo atributos
        self.ht=float(input('horas trabajadas'))

    def pago(self):
        sueldot=self.ht*79000
        print(sueldot)
        

class Vida(Sueldo):
    def __init__(self):
        super().__init__()
        self.actividad=input('describa que actividad fisica realiza')

    def imprimir2(self):
        print(self.actividad)

        
class Persona1():
    def __init__(self):
        self.nombre=input('Ingrese su nombre: ')
        self.edad=int(input('Ingrese su edad: '))

    def imprimir(self):
        print ('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')
