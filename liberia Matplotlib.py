import matplotlib.pyplot as Grafica

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico de líneas
Grafica.plot(x, y, marker='o', linestyle='-', color='g')

# Etiquetas y título
Grafica.xlabel('Eje X')
Grafica.ylabel('Eje Y')
Grafica.title('Gráfico de Líneas')

# Mostrar el gráfico
Grafica.show()


#grafico de barras

# Datos
x = ['A', 'B', 'C', 'D', 'E']
y = [5, 7, 3, 8, 6]

# Crear el gráfico de barras
Grafica.bar(x, y, color='orange')

# Etiquetas y título
Grafica.xlabel('Categorías')
Grafica.ylabel('Valores')
Grafica.title('Gráfico de Barras')

# Mostrar el gráfico
Grafica.show()

#histograma

# Datos
datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Crear el histograma
Grafica.hist(datos, bins=5, color='green', edgecolor='black')

# Etiquetas y título
Grafica.xlabel('Valor')
Grafica.ylabel('Frecuencia')
Grafica.title('Histograma')

# Mostrar el gráfico
Grafica.show()

#grafico de dispersion

# Datos
x = [1, 2, 3, 4, 5]
y = [1, 4, 6, 8, 10]

# Crear el gráfico de dispersión
Grafica.scatter(x, y, color='red')

# Etiquetas y título
Grafica.xlabel('Eje X')
Grafica.ylabel('Eje Y')
Grafica.title('Gráfico de Dispersión')

# Mostrar el gráfico
Grafica.show()

#grafico de pastel

# Datos
etiquetas = ['A', 'B', 'C', 'D']
valores = [15, 30, 45, 10]

# Crear el gráfico de pastel
Grafica.pie(valores, labels=etiquetas, autopct='%1.1f%%')

# Título
Grafica.title('Gráfico de Pastel')

# Mostrar el gráfico
Grafica.show()
