from tkinter import *

class Calculadora(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.crear_botones()

    def suma(self):
        num1 = self.entrada1.get()
        num2 = self.entrada2.get()
        resultado = float(num1) + float(num2)
        self.entrada_resultado.delete(0, 'end')
        self.entrada_resultado.insert(0, resultado)

    def resta(self):
        num1 = self.entrada1.get()
        num2 = self.entrada2.get()
        resultado = float(num1) - float(num2)
        self.entrada_resultado.delete(0, 'end')
        self.entrada_resultado.insert(0, resultado)

    def multiplicacion(self):
        num1 = self.entrada1.get()
        num2 = self.entrada2.get()
        resultado = float(num1) * float(num2)
        self.entrada_resultado.delete(0, 'end')
        self.entrada_resultado.insert(0, resultado)

    def division(self):
        num1 = self.entrada1.get()
        num2 = self.entrada2.get()
        resultado = float(num1) / float(num2)
        self.entrada_resultado.delete(0, 'end')
        self.entrada_resultado.insert(0, resultado)

    def crear_botones(self):
        self.etiqueta1 = Label(self, text='Número 1')
        self.etiqueta1.config(fg='green', font=('Arial', 16))
        self.entrada1 = Entry(self)
        self.etiqueta2 = Label(self, text='Número 2')
        self.etiqueta2.config(fg='purple', font=('Arial', 16))
        self.entrada2 = Entry(self)
        self.boton_suma = Button(self, text='Suma', command=self.suma)
        self.boton_resta = Button(self, text='Resta', command=self.resta)
        self.boton_multiplicacion = Button(self, text='Multiplicación', command=self.multiplicacion)
        self.boton_division = Button(self, text='División', command=self.division)
        self.etiqueta_resultado = Label(self, text='Resultado')
        self.etiqueta_resultado.config(fg='pink', font=('Arial', 16))
        self.entrada_resultado = Entry(self)
        self.etiqueta1.place(x=10, y=10, width=100, height=30)
        self.entrada1.place(x=120, y=10, width=100, height=30)
        self.etiqueta2.place(x=10, y=50, width=100, height=30)
        self.entrada2.place(x=120, y=50, width=100, height=30)
        self.boton_suma.place(x=230, y=10, width=100, height=20)
        self.boton_resta.place(x=230, y=40, width=100, height=20)
        self.boton_multiplicacion.place(x=230, y=70, width=100, height=20)
        self.boton_division.place(x=230, y=100, width=100, height=20)
        self.etiqueta_resultado.place(x=10, y=120, width=100, height=30)
        self.entrada_resultado.place(x=120, y=120, width=100, height=30)

ventana = Tk()
ventana.wm_title('Calculadora')
ventana.geometry('400x200')
app = Calculadora(ventana)
app.mainloop()
