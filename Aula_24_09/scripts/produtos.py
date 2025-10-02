produto = int(input("Digite a quantidade do produto: "))
nome_pesado = "" # "" vazio
peso_pesado = 0
nome_leve = ""
peso_leve =10000000000000
nome_caro = ""
preco_caro = 0
nome_barato = ""
preco_barato = 1000000000000
for numero in range (1, produto + 1):
    nome = input(f"Digite o nome{produto}° do produto: ")
    peso = float(input(f"Digite o peso do {produto}° produto: ").replace(',', '.'))
    preco = float(input(f"Digite o preço do {produto}° produto R$: ").replace(',', '.'))
    if peso > peso_pesado:
        peso_pesado = peso
        nome_pesado = nome
    # peso_pesado = peso if peso>peso_pesado else peso_pesado
    # nome_pesado = nome if peso>peso_pesado else nome_pesado
    if peso<peso_leve:
        peso_leve = peso
        nome_leve = nome
    if preco > preco_caro:
        preco_caro = preco
        nome_caro = nome
    if preco < preco_barato:
        preco_barato = preco
        nome_barato = nome
print(f"O nome do produto mais caro é {nome_caro} com valor {preco_caro}")
print(f"O nome do produto mais barato é {nome_barato} com valor {preco_barato}")
print(f"O nome do produto pesado é {nome_pesado} com {peso_pesado} Kg")
print(f"O nome do produto leve é {nome_leve} com {peso_leve} Kg")
