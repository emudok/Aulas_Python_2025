import numpy as np
nome_produtos = list(input("Digite o nome do produto: ").strip())
preco_produtos = np.array(list(map(float,input("Digite o preço dos produtos: ").replace(",", ".").split())))
produtos_atualizados = preco_produtos + (0.16 * preco_produtos)
for produto in produtos_atualizados:
    print(f"O valor dos produtos é {produto:.2f}")

