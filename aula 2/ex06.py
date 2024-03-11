print("Exercício 6 - Juros Compostos 2")

FV = float(input("Informe o valor final que deseja arrecadar: "))
N  = float(input("Digite o número de meses que pretende investir:"))
I  = float(input("Digite a rentabilidade do investimento: ")) / 100


PV = FV / (1 + I) ** N

print(f"O valor inicial para esse investimento deve ser {PV:.2f}")