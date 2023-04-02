"""
# Questão 01: Utilize a função zeros da biblioteca numpy para plotar uma imagem binária de dimensão
20x20 com todos os valores de pixels iguais a zero. Para isso, utilize o
comando:
I = np.zeros((20,20), dtype=’int’)
Ilumine apenas os pixels na 4-vizinhança do pixel na posição (x,y) = (10,10). Plote a
imagem original e a modificada na mesma figura utilizando a função plt.subplot(1,2,1).
"""

import matplotlib.pyplot as plt
import numpy as np

# Criação da matriz de 20x20 com todos os elementos igauis a zero
I = np.zeros((20, 20), dtype='int')

# Deteminação dos pixels da 4-vizinhaça do ponto (10, 10)
x, y, valor = 10, 10, 1
I[x-1, y] = valor
I[x+1, y] = valor
I[x, y-1] = valor
I[x, y+1] = valor

# Gerando a imagem original e uma modificação na mesa
plt.subplot(1, 2, 1)
plt.imshow(np.zeros((20, 20)), cmap='gray')
plt.title('Imagem original')

plt.subplot(1, 2, 2)
plt.imshow(I, cmap='gray')
plt.title('Imagem modificada')

plt.tight_layout()
plt.show()
