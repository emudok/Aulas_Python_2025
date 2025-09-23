produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade de itens: "))
preco = float(input("Digite o valor do produto em R$: ").replace(",", "."))
total = quantidade * preco
print(f"O produto {produto} e valor total {total:.2f}")