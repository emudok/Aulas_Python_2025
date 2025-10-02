import random
import numpy as np
vetor = np.array(list(map(float, input("Digite números qualquer:").replace(",", ".").split())))
print(vetor)
cubo = vetor ** 3
print(f"{vetor} elevado ao cubo = {cubo}")
outro = []
for numero in range(len(vetor)):
    outro.append(random.randint(1, 100))
outro = np.array(outro)
soma = vetor + outro
print(f"{vetor} + {outro} = {soma}")
