"""
lista.remove("python")
print(lista)
lista.append("python")
print(lista)
lista.remove("python")
#lista.insert(1, "python")
lista[1]="python"
print(lista)
"""
"""
lista = [1, "python", 3.14, "python", 17]
indice = []
for item in range(len(lista)):
    if lista[item] == "python":
        indice.append(item)
print(f"O python está nas posiçôes {indice}")
"""

quantidade = int(input("Quantos itens você quer digitar? "))
indice = []
itens = []
for item in range(1, quantidade+1):
    itens.append(input(f"Digite um valor para a {item}°: "))
if "python" in itens:
    for i in range(len(itens)):
        if itens[i] == "python":
            indice.append(i)
    print(f"O python está nas posiçôes {indice}")
else:
    print(f"Você não digitou python {itens}")

