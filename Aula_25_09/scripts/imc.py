pessoas = {}
for numero in range(5):
    nome = input(f"Digite o nome da {numero+1} pessoa: ")
    pessoas[nome] = {
        "altura": float(input(f"Digite a altura da {numero+1} pessoa: ").replace(",", ".")),
        "peso": float(input(f"Digite o peso da {numero+1} pessoa: ").replace(",", "."))
    }
    pessoas[nome]["imc"] = (pessoas[nome]["peso"]/ (pessoas[nome]["altura"] * pessoas[nome]["altura"]))
for nomes, valores in pessoas.items():
    print(f"{nomes} tem {valores['peso']:.2f} Kg e {valores['altura']:.2f}m de altura e IMC={valores['imc']:.2f} kg/m²")


