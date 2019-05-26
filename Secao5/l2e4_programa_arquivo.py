def lerArquivo(nome_arquivo):
    arquivo = open(nome_arquivo)
    linhas = arquivo.read()
    return linhas

menu = 0

try:
    while menu != 3:
        print()
        menu = int(input("Digite (1) para Ler Arquivo\nDigite (2) para Imprimir conteúdo\nDigite (3) para Encerrar Programa\n-> "))
        
        if menu == 1:
            linhas = lerArquivo("exercicio_e4.txt")

        elif menu == 2:
            if linhas != "":
                print("\n"+linhas)

            else:
                print("\nNão possui texto")

        elif menu == 3:
            print("\nPrograma Encerrado!")

        else:
            print("\nOpção inválida!")   
                
except EOFError:
    print("EOF Error")
