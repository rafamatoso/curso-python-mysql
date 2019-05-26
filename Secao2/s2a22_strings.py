a = "Rafael"
b = "Matoso"

concatenar = a + " " + b + "\n"

print(concatenar)

tamanho = len(concatenar) # conta a qtd de caracteres, inclusive espaço em branco

print(tamanho)

print(concatenar[0:6]) # uma string é um array de caracteres, então podemos usar as propriedades do array

print(concatenar.lower()) # string é um objeto, pode usar métodos da classe

print(concatenar.strip()) # strip remove caracteres especiais no início e fim da string

print(concatenar.split("a"))