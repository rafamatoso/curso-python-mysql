arquivo = open("helloworld.txt")

#linhas = arquivo.readlines();  # Lê as linhas e as separam por strings
#linha = arquivo.readline();    # Lê apenas a primeira limha do arquivo 
linhas = arquivo.read();        # Lê as linhas e gera uma única string

print(linhas);
#print(linha)