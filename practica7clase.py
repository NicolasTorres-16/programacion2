import csv
admin = {"admin": 1234}
profes = {}
estudiantes = {}
asignaturas = []

def Academico():
    print("academico")
    n_usuarios = int(input("marque 1.profes 2.estudiantes 3.asignaturas"))
    if n_usuarios ==1:
        usu =input("ingrese el nuevo usuario" )
        contra= int(input("ingrese la contraseña para el nuevo usuario "))
        profes[usu]=contra
        print("usuario almacenado ")
        academico()
    
def convivencia():
    print("convivencia")
    
def biblioteca():
    print("biblioteca")

def votaciones():
    print("votaciones")

def acceso():
    print("bienvenido al menu de acceso: 1.Administrativo 2. profe 3.estudiante")
    opcion = int(input())
    if opcion == 1:
        print("bienvenido admin")
        usu = input("ingrese su usuario: ")
        contra = int(input("ingrese su contraseña: "))
        if usu in admin and contra == admin[usu]:
            print("ok")
            modulo = int(input("a que modulo quiere ir: 1. academico, 2. convivencia, 3.biblioteca, 4.votaciones "))
            if modulo == 1:
                academico()
            elif modulo ==2:
                convivencia()
            elif modulo ==3:
                biblioteca()
            elif modulo ==4:
                votaciones()
            else:
                print("dato erroneo")
        else:
            print("dato erroneo")

                
            
            
