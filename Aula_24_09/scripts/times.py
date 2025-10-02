time1 = input("Digite seu time: ")
time2 = input("Digite seu time: ")
vitorias_1 = 0
vitorias_2 = 0
empate = 0
opcao = "sim"
while opcao == "sim":
    gols1 = int(input(f"Digite o número de gols do {time1}: "))
    gols2 = int(input(f"Digite o número de gols do {time2}: "))
    if gols1 > gols2:
        vitorias_1+=1
        print(f"O {time1} venceu!")
    elif gols2 > gols1:
        vitorias_2+=1
        print(f"O {time2} venceu!")
    else:
        empate+=1
        print(f"Foi empate do {time1} com {time2} !")
    opcao = input("Deseja outra partida? digite sim ou não").lower()
if vitorias_1 > vitorias_2:
    print(f"O {time1} é o campeão com {vitorias_1} vitorias!")
elif vitorias_2 > vitorias_1:
    print(f"O {time2} é o campeão com {vitorias_2} vitorias!")
else:
    print(f"O time {time1} com {vitorias_1} vitorias empatou com o {time2} com {vitorias_2} vitorias!")

