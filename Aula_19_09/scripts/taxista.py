nome = input("Digite o nome do taxista: ")
odometroinicial = int(input("Digite o valor do odômetro inicial: "))
odometrofinal = int(input("Digite o valor do odômetro final: "))
litros = int(input("Digite quanto foi gasto em L: "))
preco = float(input("Digite o valor do combustivel preco em R$: ").replace(",", "."))
ganho = float(input("Digite o valor do pago em R$: ").replace(",", "."))
km = odometroinicial - odometrofinal
media = (odometrofinal - odometroinicial) / litros
print(f"A média de consumo km/litro é {media:.2f}")
lucroliq = ganho -(preco * litros)
print(f"Para o taxista {nome} o lucro líquido é R$ {lucroliq:.2f}")

