minha_lista = ["abacaxi", "melancia", "maçã"]
minha_lista2 = [1, 2, 3, 4, 5]
minha_lista3 = ["abacaxi", 2, 9.89, True]
minha_lista4 = [7, 8, 9, 2, 1, 6, 3, 4, 10, 1457]

# print(minha_lista[2])

#for i in minha_lista:
#    print(i)

tamanho = len(minha_lista)
print(tamanho)

# adicionar item numa lista
minha_lista.append("limão")
print(minha_lista)

# verifica se um determinado item pertence na lista
if "abacaxi" in minha_lista:
    print("abacaxi está na lista")

# remove elemento de uma lista
del minha_lista[2:]
print(minha_lista)
# del minha lista[:] # remove todos os elementos

