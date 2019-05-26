# Visualização de dados em Python

import matplotlib.pyplot as plt

'''x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = "Gráfico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y)
plt.show()'''

# Comparação entre gráficos Barras

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = "Gráfico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")
plt.legend() # imprime a legenda do gráfico

plt.show()