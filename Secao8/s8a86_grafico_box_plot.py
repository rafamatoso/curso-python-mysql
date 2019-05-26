# Box-plot: diagrama de caixa (dispersão de dados)
import matplotlib.pyplot as plt
import random

vetor = []

for i in range(100):
    n_aleatorio = random.randint(0,50)
    vetor.append(n_aleatorio)

# print(vetor)
plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()