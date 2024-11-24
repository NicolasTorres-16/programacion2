print("Unidades disponibles: metro, kilometro, centimetro, milla, yarda, pie, pulgada")

conversiones = {
    "metro": 1,
    "kilometro": 1000,
    "centimetro": 0.01,
    "milla": 1609.34,
    "yarda": 0.9144,
    "pie": 0.3048,
    "pulgada": 0.0254
}

unidad_origen = input("Ingrese la unidad de origen: ")
unidad_destino = input("Ingrese la unidad de destino: ")

if unidad_origen not in conversiones or unidad_destino not in conversiones:
    print("Una o ambas unidades no son válidas.")
else:
    valor = float(input(f"Ingrese el valor en {unidad_origen}: "))
    metros = valor * conversiones[unidad_origen]
    resultado = metros / conversiones[unidad_destino]
    print(f"{valor} {unidad_origen}(s) equivalen a {resultado:.4f} {unidad_destino}(s).")


