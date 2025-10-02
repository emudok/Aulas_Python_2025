nomes = []
alturas = []
for numero in range(5):
    nomes.append(input(f"Digite o {numero+1}° nome: "))
    alturas.append(float(input(f"Digite a {numero}° altura: ").replace(",", ".")))
pessoas = list(zip(nomes, alturas))
pessoas_ordenadas = sorted(pessoas)
for nome, altura in pessoas_ordenadas:
    print(f"Nome: {nome} Altura: {altura:.2f} m")
    
