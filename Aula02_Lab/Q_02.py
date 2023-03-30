# Questão 02
"""
Comandos de instalação de Bibliotecas: 

python -m pip install -U pip
python -m pip install -U matplotlib
pip install numpy
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
