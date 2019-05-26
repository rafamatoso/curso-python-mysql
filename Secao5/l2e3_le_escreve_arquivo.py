nome_arquivo = input("Digite o nome + formato do arquivo de destino: ")

w = open(nome_arquivo, "w+")

w.writelines() # writelines() é usado para criar um arquivo inexistente

cabecalho = input("Digite o cabeçalho do Arquivo: ")

seq = input("Digite a Sequência de Proteínas: ")

w.write(">"+cabecalho+"\n"+seq)

w.close()