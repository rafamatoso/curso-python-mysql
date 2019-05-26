import aleatorio as a
import media as m

lista = a.geraListaInteiro(10)
#print(lista)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

lista.sort()

print("Minha lista: ")
print(lista)

print("Média dos valores da Lista: ",media)
print("Mediana dos valores da Lista: ",mediana)
print("Moda dos valores da Lista: ",moda) 