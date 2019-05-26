nome_arquivo = input("Digite o nome do arquivo (Ex - nome_arquivo.formato): ")

arquivo = open(nome_arquivo)

linhas = arquivo.read()

print(linhas)

# usando o readlines()

'''linhas = arquivo.readlines()

for linha in linhas:
    print(linha.strip())'''