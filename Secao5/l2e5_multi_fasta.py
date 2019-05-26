arquivo = open("seq_fasta.txt")

linhas = arquivo.readlines()

multifasta = {}

for linha in linhas:
    if linhas[0] == ">":
        seq_atual = linha.strip()
        multifasta[seq_atual] = ""
    else:
        multifasta[seq_atual] = multifasta[seq_atual]+linha.strip()

print(multifasta)