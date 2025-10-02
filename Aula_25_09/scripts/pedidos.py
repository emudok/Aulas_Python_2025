def retornar_preco(codigo):
    match codigo:
        case 1: return 7.00
        case 2: return 8.00
        case 3: return 10.00
        case 4: return 12.50

def calcular_total(quantidade, preco):
    return quantidade * preco

def quantidade():
    while True:
        try:
            quant = int(input("Digite a quantidade: "))
            if quant > 0:
                return quant
            else:
                print("Não vai comprar nada? ")
        except ValueError:
            print("Não é um número inteiro!")

total_f = 0
while True:
    print("-"*60)
    print("1-Coxinha, 2-Refrigerante, 3-Pastel, 4-Bolo, 5-Fechar pedido")
    while True:
        try:
            opcao = int(input("Escolha: "))
            break
        except ValueError:
            print("Isto não é um número inteiro!")

    if 1<=opcao<=4:
        total=calcular_total(quantidade(),retornar_preco(opcao))
        total_f+=total
    elif opcao==5:
        print(f"O total da compra foi de {total_f:.2f} reais!")
        break
    else:
        print("Opção inválida!")
