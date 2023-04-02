"""
# Questão 06: Implemente uma função que calcula a distância de Chebyshev (Chessboard) e repita
o Exercício 5 utilizando esta nova função de distância. Chame esta função de
d_chebyshev (p, q).
"""


import d
import matplotlib.pyplot as plt
import numpy as np

# Valores
tamanho, x, y, valor, comparador = 1000, 500, 500, 1, 60

# Criação da matriz de 20x20 com todos os elementos igauis a zero
I = np.zeros((tamanho, tamanho), dtype='int')

# Deteminação dos pixels com distância Euclidiana menor ou igual a 4
for i in range(tamanho):
    for j in range(tamanho):
        p = (x, y)
        q = (i, j)

        if d.chebyshev(p, q) <= comparador:
            I[i, j] = valor

# Plotar a imagem modificada
plt.imshow(I, cmap='gray', vmin=0, vmax=1)
plt.title('Imagem modificada')
plt.tight_layout()
plt.show()
