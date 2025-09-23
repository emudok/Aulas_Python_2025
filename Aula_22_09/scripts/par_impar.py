numero = int(input("Digite um número: "))
"""
if numero % 2 == 0:
    print(f"{numero} é Par!")
else:
    print(f"{numero} é Ímpar!")
"""
resultado = "é Par!" if numero % 2 == 0 else "é Ímpar!"
print(f"{numero} {resultado}")