# Visualização de dados em Python

import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

# Construindo legendas nos gráficos

# Título
plt.title("Meu primeiro gráfico com Python")

# Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo y")

plt.plot(x, y)
plt.show()