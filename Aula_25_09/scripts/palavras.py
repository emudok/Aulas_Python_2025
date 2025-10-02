quantidade = int(input("Digite a quantidade: "))
palavras = []
for numero in range(quantidade):
    palavras.append(input(f"Digite a {numero+1} palavra: "))
palavra=input(f"Digite outra palavra: ")
if palavra in palavras:
    print(f"{palavra} está entre as palavras digitadas.")
else:
    print(f"Palavra não foi digitada entre as palavras digitadas.")
