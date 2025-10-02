produtos = {}
quantidade = int(input("Digite quantos produtos você quer cadastrar: "))
total = 0
for i in range(quantidade):
    nome = input(f"Digite o nome do {i+1} produto: ")
    produtos[nome] = {
        "quantidade": int(input(f"Digite a quantidade do(a) {nome}: ")),
        "preco": float(input(f"Digite o preço do produto {nome}: ").replace(",", ".")),
    }
    produtos[nome]["total"]= produtos[nome]["preco"] * produtos[nome]["quantidade"]
    total += produtos[nome]["total"]

for nome, valor in produtos.items():
    print(f"{nome}:")
    for coluna, valor in valor.items():
        print(f"{coluna} = {valor}")
print(f"O valor total dos produtos é: {total:.2f}")
