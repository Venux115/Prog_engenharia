quantidadeLivros = int(input("Digite a quantidades de livros a serem comprados: "))

livro = 24.95
desconto = 0.35
livro = livro * (1 - desconto)
transporte = 0.75 * (quantidadeLivros - 1) + 3

valorFinal = (livro * quantidadeLivros) + transporte

print(f"O valor nescessario para a compra de {quantidadeLivros} livros são R${valorFinal:.2f}")


16,2175

14,25