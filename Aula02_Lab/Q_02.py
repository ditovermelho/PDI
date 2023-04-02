"""
# Questão 02: Utilize a função ones da biblioteca numpy para plotar uma imagem binária de dimensão
20x20 com todos os valores de pixels iguais a um. Escureça apenas os
pixels na vizinhança diagonal do pixel na posição (x,y) = (8,15). Plote a imagem
original (para isso, passe os parâmetros vmin=0, vmax=1 para a função plt.imshow)
e a modificada na mesma figura.
"""

import matplotlib.pyplot as plt
import numpy as np

# Criação da matriz de 20x20 com todos os elementos igauis a um
II = np.ones((20, 20), dtype='int')

# Deteminação dos pixels da 4-vizinhaça do ponto (8, 15)
x, y, valor = 8, 15, 0
II[x-1, y-1] = valor
II[x-1, y+1] = valor
II[x+1, y-1] = valor
II[x+1, y+1] = valor

# Gerando a imagem original e uma modificação na mesa
plt.subplot(1, 2, 1)
plt.imshow(np.ones((20, 20)), cmap='gray', vmin=0, vmax=1)
plt.title('Imagem original')

plt.subplot(1, 2, 2)
plt.imshow(II, cmap='gray', vmin=0, vmax=1)
plt.title('Imagem modificada')

plt.tight_layout()
plt.show()
