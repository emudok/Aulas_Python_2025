import numpy as np
coeficientes1 = list(input("Digite os primeiros coeficientes: ").split())
coeficientes1= np.array(list(map(float, coeficientes1)))
coeficientes2 = list(input("Digite os segundos coeficientes: ").split())
coeficientes2 = np.array(list(map(float, coeficientes2)))

termos_ind = list(input("Digite os termos independentes: ").split())
termos_ind = np.array(list(map(int, termos_ind)))

coeficientes = np.array([coeficientes1,coeficientes2])
solucao = np.linalg.solve(coeficientes, termos_ind)
print(f"x = {solucao[0]:.0f} e y = {solucao[1]:.0f}")