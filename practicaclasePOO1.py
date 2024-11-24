class Alumno:
    def _init_(self):
        self.nombre=input("ingrese su nombre")
        self.nota= int(input("ingrese su nota"))
 
    def imprimir(self):
         
         print("Nombre: ",self.nombre) 
         print("Nota: ",self.nota) 
 
    def resultado(self):
        if self.nota < 5:
             print("El alumno ha suspendido") 
        else:
            print("El alumno ha aprobado") 
 
##alumno1=Alumno() 
##alumno2=Alumno() 
##alumno1.inicializar("ivan",8) 
##alumno2.inicializar("juan",4) 
##alumno1.imprimir() 
##alumno1.resultado() 
##alumno2.imprimir() 
##alumno2.resultado() 
