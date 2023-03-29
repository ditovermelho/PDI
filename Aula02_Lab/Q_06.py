# Questão 06
"""
Comandos de intalação de Bibliotecas: 

python -m pip install -U pip
python -m pip install -U matplotlib
pip install numpy
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# Definindo a função chebyshev


def d_chebyshev(p, q):
    return max(abs(p[0] - q[0]), abs(p[1] - q[1]))


# Valores
tamanho, x, y, valor, comparador = 1000, 500, 500, 1, 60

# Criação da matriz de 20x20 com todos os elementos igauis a zero
I = np.zeros((tamanho, tamanho), dtype='int')

# Deteminação dos pixels com distância Euclidiana menor ou igual a 4
for i in range(tamanho):
    for j in range(tamanho):
        p = (x, y)
        q = (i, j)

        if d_chebyshev(p, q) <= comparador:
            I[i, j] = valor

# Plotar a imagem modificada
plt.imshow(I, cmap='gray', vmin=0, vmax=1)
plt.title('Imagem modificada')
plt.show()
