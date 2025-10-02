inicio  = int(input("Digite o inicio da contagem: "))
fim = int(input("Digite o fim da contagem: "))
if fim > inicio:
    for numero in range(inicio, fim+1):
        print(numero)
elif fim < inicio:
    for numero in range(inicio, fim-1, -1):
        print(numero)