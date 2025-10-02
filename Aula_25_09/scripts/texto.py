texto = input("Digite um texto ou uma palavra: ").strip()
letra = input("Digite uma letra: ").strip()
contagem = texto.count(letra)
print(f"Aparece {contagem} vezes")
