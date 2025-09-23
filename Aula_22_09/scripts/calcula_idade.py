from datetime import datetime

dia_nasci_str = input("Informe o dia de nascimento dd/mm/aaaa: ")
data_nasci =datetime.strptime(dia_nasci_str, "%d/%m/%Y")
hoje = datetime.today()
idade_dias = hoje - data_nasci
idade = hoje.year - data_nasci.year

if (hoje.month, hoje.day) < (data_nasci.month,data_nasci.day):
    idade = idade - 1

segundos = idade_dias.total_seconds()
horas = int(segundos // 3600)
minutos = int((segundos % 3600)//60)

print(f"Você tem {idade} anos de idade")
print(f"Foram {idade_dias.days} dias")
print(f"{horas} horas e {minutos} minutos")

