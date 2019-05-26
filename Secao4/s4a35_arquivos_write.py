# w = open("file2.txt", "w")  # Escreve algo num arquivo (apaga o arquivo original)
w1 = open("file2.txt", "a") # Escreve algo num arquivo (Atualiza o conteúdo de um arquivo existente)

w1.write("Este é meu novo arquivo, sem apagar o conteúdo\n")

w1.close()

