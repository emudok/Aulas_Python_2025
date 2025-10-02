fatorial = 1
numero = int(input("Digite um numero: "))
contador = numero
while contador >= 1:
    fatorial = fatorial * contador
    contador -= 1
print(f"O fatorial de {numero}! = {fatorial}")

"""
for contador in range (numero,0,-1):
    fatorial = fatorial * contador
print(f"O fatorial de {numero}! = {fatorial}")
"""

"""
import math
print(f"O fatorial de {numero}! = {math.factorial(numero)}")")
"""