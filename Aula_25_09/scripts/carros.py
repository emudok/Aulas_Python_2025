carros = {}
for numero in range(3):
    carros[numero] = {
        "modelo": input(f"Digite o modelo do {numero+1} carro: "),
        "placa": input(f"Digite o placa do {numero+1} carro: "),
        "ano": int(input(f"Digite o ano de fabricação {numero+1} do carro: ")),
        "cor": input(f"Digite o cor do {numero+1} carro: ")
    }
opcao = int(input("Digite 1-excluir, 2-atualizar:"))
if opcao == 1:
    while True:
        modelo = input("Digite o modelo do carro que deseja excluir: ")
        teste = False
        for numero in carros:
            if carros[numero]["modelo"] == modelo:
                del carros[numero]
                teste = True
                break
        if teste:
            break
elif opcao == 2:
    while True:
        modelo = input("Digite o modleo do carro que deseja atualizar: ")
        teste = False
        for numero in carros:
            if carros[numero]["modelo"] == modelo:
                carros[numero]["modelo"] = input("Digite o modelo do carro: ")
                carros[numero]["placa"] = input("Digite o placa do carro: ")
                carros[numero]["ano"] = int(input("Digite o ano do carro: "))
                carros[numero]["cor"] = input("Digite o cor do carro: ")
                teste = True
                break
        if teste:
            break
print(carros)

