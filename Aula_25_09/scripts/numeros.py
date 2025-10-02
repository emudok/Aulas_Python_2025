import array
numeros = array.array('i')
#numeros = []
for numero in range(5):
    numeros.append(int(input(f"Digite o {numero+1} numero: ")))
print(f"O maior é {max(numeros)} e o menor é {min(numeros)}")
