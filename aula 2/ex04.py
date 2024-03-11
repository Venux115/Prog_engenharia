print("Exercicio 4 - Média arítimética")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if  media >= 6:
    print(f"Aluno aprovado! A média do aluno foi {media:.2f}")
else:
    print(f"Aluno reprovado! A média do aluno foi {media:.2f}")