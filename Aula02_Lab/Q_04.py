
"""
# Questão 04: Utilize a mesma imagem utilizada no Exercício 1 e ilumine apenas os pixels tais que
a distância Euclidiana entre eles e o pixel p com coordenadas (10,10) seja menor ou
igual a quatro. Plote a imagem resultante.
"""


import d
import matplotlib.pyplot as plt
import numpy as np

# Criação da matriz de 20x20 com todos os elementos igauis a zero
I = np.zeros((20, 20), dtype='int')

# Definindo a função euclidiana


# Deteminação dos pixels com distância Euclidiana menor ou igual a 4
tamanho, x, y, valor = 20, 10, 10, 1
for i in range(tamanho):
    for j in range(tamanho):
        p = (x, y)
        q = (i, j)

        if d.euclidiana(p, q) <= 4:
            I[i, j] = valor

# Plotar a imagem modificada
plt.imshow(I, cmap='gray', vmin=0, vmax=1)
plt.title('Imagem modificada')
plt.tight_layout()
plt.show()
