import numpy as np
temperaturas_lista = list(input("Digite as temperaturas com espaço: ").replace(',', '.').split())
temperaturas_lista = list(map(float, temperaturas_lista))
temperaturas = np.array(temperaturas_lista)
#temperaturas = np.array([22.5,23.0,24.0,19.3,22.0])

media = np.mean(temperaturas)
mediana = np.median(temperaturas)
devio_padrao = np.std(temperaturas)
max_temperatura = np.max(temperaturas)
min_temperatura = np.min(temperaturas)

print(f"media temperatura: {media:.0f}°C")
print(f"mediana temperatura: {mediana:.0f}°C")
print(f"devio padrao: {devio_padrao:.0f}")
print(f"max_temperatura: {max_temperatura:.0f}°C")
print(f"min_temperatura: {min_temperatura:.0f}°C")