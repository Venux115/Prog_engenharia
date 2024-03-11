print("Exercicio 3 - Divisão")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if not (num1 == 0 or num2 == 0):
    divisao = num1 / num2;
    print(f"O resultado da divisão é {divisao}")
else:
    print("Impossivel efetuar divisão por zero")