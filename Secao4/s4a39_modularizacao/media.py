# media, mediana, moda

# modo fácil
#from statistics import *

'''mean(lista)
median(lista)
mode(lista)'''

# modo com funções

def media(lista):
    media = sum(lista)/float(len(lista))
    return media

def mediana(lista):
    #mediana = median(lista)
    lista_ordenada = sorted(lista)
    t = len(lista_ordenada)

    if t % 2 == 0:
        mediana = (lista_ordenada[int((t/2)-1)] + lista_ordenada[int(t/2)])/2
    elif t % 2 == 1:
        mediana = lista_ordenada[int((t/2))]

    return mediana

def moda(lista):
    #moda = mode(lista)
    lista_dic = {}

    for l in lista:
        if l not in lista_dic:
            lista_dic[l] = 1
        else:
            lista_dic[l] += 1

    maior_repeticao = max(lista_dic.values())

    for i in lista_dic:
        if lista_dic[i] == maior_repeticao:
            moda = i

    return moda