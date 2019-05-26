import random

def geraListaInteiro(tam):
    lista = []
    for i in range(tam):
        i = random.randint(0, tam)
        lista.append(i)
    return lista

