# idade = int(input("Digite sua idade: ")) # No Python 3, todo o input de dados é considerado como string!
idade = 30

if idade <= 0:
    print("idade inválida")
elif idade < 18:
    print("menor de idade")
else:
    print("maior de idade")
