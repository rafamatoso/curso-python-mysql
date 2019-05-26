def soma(x, y): # Funções precisam ser definidas antes de serem chamadas
    return x + y

def multiplicacao(x, y):
    return x * y

s = soma(2, 3)
m = multiplicacao(2, 3)

print(multiplicacao(soma(s, m), multiplicacao(s, m)))

