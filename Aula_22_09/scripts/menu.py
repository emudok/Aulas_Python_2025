menu = int(input(" \n 1-Coxinha 6,00 \n 2-Pastel 10,00 \n 3-Quibe 7,00 \n 4-Bolo Fubá 12,00 \n 5-Pudim de leite 11,50 \n Escolha:")) # \n pula de linha
quantidade = int(input("Digite a quantidade do produto: "))
match menu:
    case 1: total = 6.00 * quantidade
    case 2: total = 10.00 * quantidade
    case 3: total = 7.00 * quantidade
    case 4: total = 12.00 * quantidade
    case 5: total = 11.50 * quantidade
    case _: total = 0
if total > 0:
    print(f"Para a opção {menu} e {quantidade} unidades o produto fica R$ {total:.2f} ")
else:
    print(f"O tipo escolhido {menu} não é válido!")
