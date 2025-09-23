valor_carro_fabrica = float(input("Digite o valor de fábrica do carro: ").replace(".", "").replace(",", "."))
valor_distribuidor = valor_carro_fabrica * 0.28
imposto = valor_carro_fabrica * 0.45
valor_final = valor_carro_fabrica + valor_distribuidor + imposto
print(f"Com 28% do distribuidor = R$ {valor_distribuidor:.2f}")
print(f" + 45% do imposto = R$ {imposto:.2f}")
print(f"O valor final para o consumidor é {valor_final:.2f}")