quantidade = int(input("Digite a quantidade de candidatos: "))
alto=0
nome_alto=""
for numero in range(1, quantidade + 1):
    nome = input("Digite nome do candidato: ")
    altura = float(input("Digite a altura do candidato: ").replace(",", "."))
    if altura>alto:
        nome_alto = nome
        alto = altura
print(f"O nome do candidato mais alto é {nome_alto}")