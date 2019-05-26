num1 = float(input("Digite o primeiro número: "))
op = input("Digite o operador: ")
num2 = float(input("Digite o segundo número: "))

if op == "+":
    result = num1 + num2

elif op == "-":
    result = num1 - num2

elif op == "*":
    result = num1 * num2

elif op == "/":
    result = num1 / num2

elif op == "**":
    result = num1 ** num2

elif op == "%":
    result = num1 % num2

else:
    print("Erro: sem operador ou operador desconhecido")

print("Resultado = %.2f" %result)