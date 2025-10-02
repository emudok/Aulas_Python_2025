def set_numero_1():
    while True:
        try:
            numero_1 = int(input("Digite um número: "))
            return numero_1
        except ValueError:
            print("Isto não é um número!")

def set_numero_2():
    while True:
        try:
            numero_2 = int(input("Digite outro número: "))
            return numero_2
        except ValueError:
            print("Isto não é número!")

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        return "Não há divisão por zero!"
    else:
        return a/b

while True:
    print("-"*63)
    print("1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir, 5 - Sair")
    while True:
        try:
            opcao = int(input("Digite a opção: "))
            break
        except ValueError:
            print("As opções são de 1 a 5!")
    if opcao == 1:
        print(f"soma = {somar(set_numero_1(), set_numero_2())}")
        input("Pressione <enter> para continuar...")
    elif opcao == 2:
        print(f"subtração = {subtrair(set_numero_1(), set_numero_2())}")
        input("Pressione <enter> para continuar...")
    elif opcao == 3:
        print(f"multiplicação = {multiplicar(set_numero_1(), set_numero_2())}")
        input("Pressione <enter> para continuar...")
    elif opcao == 4:
        print(f"divisão = {dividir(set_numero_1(), set_numero_2())}")
        input("Pressione <enter> para continuar...")
    elif opcao == 5:
        break
    else:
        print("Opção invalida!")


