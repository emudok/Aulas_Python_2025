autor1 = input("Informe o primeiro autor: ")
titulo1 = input("Informe o título: ")
num_pag1 = int(input("Digite o número de páginas:"))

autor2 = input("Informe o segundo autor: ")
titulo2 = input("Informe o título: ")
num_pag2 = int(input("Digite o número de páginas:"))

if num_pag1 > num_pag2:
    print(f"O livro de {autor1} de título {titulo1} é o maior!")
elif num_pag2 > num_pag1:
    print(f"O livro de {autor2} de título {titulo2} é o maior!")
else:
    print(f"O livro do {autor1} e {autor2} tem o mesmo número de páginas!")