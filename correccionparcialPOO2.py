import csv
from datetime import datetime

class Producto:
    def __init__(self, nombre_nict, precio_nict, cantidad_t):
        self.nombre = nombre_nict
        self.precio = precio_nict
        self.cantidad = cantidad_t

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad en stock: {self.cantidad}")

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            print(f"Venta realizada: {cantidad_vendida} unidades de {self.nombre}")
        else:
            print("Stock insuficiente para la venta")

    def actualizar_inventario(self, cantidad_agregada):
        self.cantidad += cantidad_agregada
        print(f"Inventario actualizado: {self.cantidad} unidades de {self.nombre}")

class Electronico(Producto):
    def __init__(self, nombre_nict, precio_nict, cantidad_t, garantia):
        super().__init__(nombre_nict, precio_nict, cantidad_t)
        self.garantia = garantia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Garantía: {self.garantia}")

class Alimento(Producto):
    def __init__(self, nombre_nict, precio_nict, cantidad_t, fecha_vencimiento):
        super().__init__(nombre_nict, precio_nict, cantidad_t)
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Fecha de vencimiento: {self.fecha_vencimiento}")

    def esta_vencido(self):
        hoy_nt = datetime.now().date()
        fecha_venc = datetime.strptime(self.fecha_vencimiento, "%Y-%m-%d").date()
        return hoy_nt > fecha_venc

def exportar_inventario_a_csv(productos, archivo_csv):
    with open(archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Precio", "Cantidad", "Tipo", "Garantía/Fecha de Vencimiento"])
        for producto in productos:
            if isinstance(producto, Electronico):
                writer.writerow([producto.nombre, producto.precio, producto.cantidad, "Electrónico", producto.garantia])
            elif isinstance(producto, Alimento):
                writer.writerow([producto.nombre, producto.precio, producto.cantidad, "Alimento", producto.fecha_vencimiento])

def agregar_producto():
    tipo = input("Ingrese el tipo de producto (1 para Electrónico, 2 para Alimento): ")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad en stock: "))

    if tipo == "1":
        garantia = input("Garantía del producto: ")
        producto = Electronico(nombre, precio, cantidad, garantia)
    elif tipo == "2":
        fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
        producto = Alimento(nombre, precio, cantidad, fecha_vencimiento)
    else:
        print("Tipo no válido.")
        return None

    return producto

def mostrar_inventario(productos):
    if not productos:
        print("No hay productos en el inventario.")
    for producto in productos:
        producto.mostrar_info()
        print()

def realizar_venta(productos):
    nombre = input("Ingrese el nombre del producto a vender: ")
    for producto in productos:
        if producto.nombre == nombre:
            cantidad = int(input("Cantidad a vender: "))
            producto.vender(cantidad)
            return
    print("Producto no encontrado.")

def actualizar_inventario(productos):
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for producto in productos:
        if producto.nombre == nombre:
            cantidad = int(input("Cantidad a agregar al inventario: "))
            producto.actualizar_inventario(cantidad)
            return
    print("Producto no encontrado.")

def menu():
    productos = []
    while True:
        print("\nSistema de Inventario")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Realizar venta")
        print("4. Actualizar inventario")
        print("5. Exportar inventario a CSV")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = agregar_producto()
            if producto:
                productos.append(producto)
                print("Producto agregado.")
        elif opcion == "2":
            mostrar_inventario(productos)
        elif opcion == "3":
            realizar_venta(productos)
        elif opcion == "4":
            actualizar_inventario(productos)
        elif opcion == "5":
            archivo_csv = input("Ingrese el nombre del archivo CSV (con extensión .csv): ")
            exportar_inventario_a_csv(productos, archivo_csv)
            print("Inventario exportado a CSV.")
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")
menu()
