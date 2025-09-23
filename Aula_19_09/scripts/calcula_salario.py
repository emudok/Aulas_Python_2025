nome = input("Digite o nome do funcionário: ")
horast = int(input("Digite a quantidade de horas trabalhadas: "))
valorh = float(input("Digite o valor em R$ da hora: ").replace(",", "."))
salariobru = horast * valorh
print(f"Para o(a) {nome} o salário bruto é R$ {salariobru:.2f} ")
