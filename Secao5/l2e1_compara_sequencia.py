import re

s1 = input("Digite a primeira sequência: ")
s2 = input("Digite a segunda sequência: ")

'''if s1 == s2:
    print("Sequências iguais")
else:
    print("Sequências diferentes")'''

# Fazer busca usando expressão regular

busca = re.match(s1,s2)

if busca:
    print("Sequências Idênticas")
    print(busca.group())
else:
    print("Sequências Diferentes")