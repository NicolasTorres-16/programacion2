import csv

usuarios_profesor = {"hector": 1234, "jeider": 4321}
estudiantes = ["laura", "daniel", "jhon", "juan", "nicolas"]
contraseñas = [1010, 1011, 1012, 1013, 1014]
asignaturas = ["calculo", "programacion", "dibujo", "circuitos"]
notas_estudiantes = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]

def autenticacion_profesor():
    usuario = input('Ingrese su usuario: ').lower()
    clave = int(input('Ingrese su contraseña: '))
    if (usuario in usuarios_profesor) and (usuarios_profesor[usuario] == clave):
        print('Usuario autenticado')
    else:
        print('Error de usuario y/o contraseña')
    
    menu()

def menu():
    print("""Bienvenido al programa de notas UIS Barbosa
            Marque: 1. Profesor
                    2. Estudiante""")
    opcion = int(input("opción\n"))
    if opcion == 1:
        print("Bienvenido profesor")
        autenticacion_profesor()
        
    elif opcion == 2:
        print("Bienvenido estudiante")
    else:
        print("Error de opción")

menu()
