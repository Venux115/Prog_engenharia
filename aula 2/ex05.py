print("Exercício 5 - Juros Compostos")

PV = float(input("Informe o valor inicial do investimento: "))
N  = float(input("Em quantos meses você vai investir? "))
I  = float(input("Qual é o valor da rentabilidade mensal? ")) / 100


FV = PV * (1+ I) ** N

print(f"O Valor final do investimento será {FV:.2f}")