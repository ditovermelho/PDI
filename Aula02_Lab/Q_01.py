# Questão 01
"""
Comandos de intalação de Bibliotecas: 

python -m pip install -U pip
python -m pip install -U matplotlib
pip install numpy
"""

import numpy as np
import matplotlib.pyplot as plt

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
plt.show()
