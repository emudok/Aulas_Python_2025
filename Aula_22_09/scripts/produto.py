produto = int(input("Digite o código do produto: "))
match produto:
    case 1:
        print("Seu produto é da região Sul")
    case 2:
        print("Seu produto é da região Norte")
    case 3:
        print("Seu produto é da região Leste")
    case 4:
        print("Seu produto é da região Oeste")
    case produto if 5 <= produto <= 6:
        print("Seu produto é da região Nordeste")
    case produto if 7 <= produto <=9:
        print("Seu produto é da região Sudeste")
    case 10:
        print("Seu produto é da região Centro-Oeste")
    case 11:
        print("Seu produto é da região Noroeste")
    case _:
        print("Seu produto é Importado")
