"""
2x + 3y = 8
5x + y = 7
"""

import numpy as np
a = np.array([[2,3], [5,1]])
b = np.array([8,7])
solucao = np.linalg.solve(a, b)
print(f"X= {solucao[0]:.0f}, y= {solucao[1]:.0f}") #int arrendonda para baixo,.0f para cima