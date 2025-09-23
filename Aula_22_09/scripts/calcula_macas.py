qnt_macas = int(input("Quantas maças foram compradas? "))
if qnt_macas >= 12:
    total = qnt_macas * 1.30
    print(f"Para {qnt_macas} há 1.30 cada fica {total}")
else:
    total = qnt_macas * 1.50
    print(f"Para {qnt_macas} há 1.50 cada fica {total}")
# total = quantidade * 1.30 if quantidade >= 12 else quantidade * 1.50
# print(f"Para {quantidade} maças o total fica R$ {total:.2f}"