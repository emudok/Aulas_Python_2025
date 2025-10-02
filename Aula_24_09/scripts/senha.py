senha = int(input(f"Digite a senha: "))
contador = 1
while senha != 12345:
    senha = int(input(f"Senha incorreta! Tente novamente: "))
    contador+=1
print(f"Senha correta! ")
print(f"Seja bem-vindo, foram {contador} tentativas")

