pessoas = {}
quantidade = int(input("Digite o quantidade de pessoas: "))
for c in range(quantidade):
    nome = input(f"Digite o nome da {c+1}° pessoa: ")
    pessoas[nome] = {
        "cidade": input(f"Digite o cidade do(a) {nome}: "),
        "bairro": input(f"Digite o bairro do(a) {nome}: "),
        "altura": float(input(f"Digite o altura do(a) {nome}: ").replace(",", ".")),
    }
#print(pessoas)
for nome, pessoa in pessoas.items():
    print(f"{nome}:")
    for chave, valor in pessoa.items():
        print(f"{chave} = {valor}")

