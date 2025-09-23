nome = input("Insira seu nome: ")
altura = float(input("Insira sua altura: ").replace(",", "."))
sexo = input("Insira seu sexo (M/F): ").upper()
peso = -1
if sexo == "M":
    peso = (72.7 * altura)- 58
elif sexo == "F":
    peso = (62.1 * altura) - 44.7
else:
    print(f"Favor escolher entre M ou F: {sexo}")
if peso >= 0.0:
    print(f"Caro {nome} seu peso ideal é {peso:.2f} Kg")
