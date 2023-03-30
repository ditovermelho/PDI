# Questão 04
"""
Comandos de instalação de Bibliotecas: 

python -m pip install -U pip
python -m pip install -U matplotlib
pip install numpy
"""

import math

import matplotlib.pyplot as plt
import numpy as np

import Q_03 as q3

# Criação da matriz de 20x20 com todos os elementos igauis a zero
I = np.zeros((20, 20), dtype='int')

# Definindo a função euclidiana


# Deteminação dos pixels com distância Euclidiana menor ou igual a 4
tamanho, x, y, valor = 20, 10, 10, 1
for i in range(tamanho):
    for j in range(tamanho):
        p = (x, y)
        q = (i, j)

        if q3.d_euclidiana(p, q) <= 4:
            I[i, j] = valor

# Plotar a imagem modificada
plt.imshow(I, cmap='gray', vmin=0, vmax=1)
plt.title('Imagem modificada')
plt.tight_layout()
plt.show()
