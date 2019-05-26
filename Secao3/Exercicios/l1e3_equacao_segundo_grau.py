from math import sqrt

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = (b**2)-4*a*c

if delta > 0:
    x1 = (-b + sqrt(delta))/2*a 
    x2 = (-b - sqrt(delta))/2*a 
    print("x' = ", x1)
    print("x'' = ", x2)
elif delta == 0:
    x1 = (-b + sqrt(delta))/2*a
    print("x' = x'' = ", x1)
else:
    print("Não existe raízes reais")
