""" 
Dilatação: Execute e comente o código abaixo, assim como os resultados produzidos. O que significam as matrizes criadas?
"""

import numpy as np
from matplotlib import pyplot as plt
from skimage.morphology import binary_dilation, binary_erosion

A = np.zeros((4, 4), dtype='int')
A[1, 1] = 1
A[1, 2] = 1
A[2, 1] = 1
A[2, 2] = 1

elem_estrut = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
Ad = binary_dilation(A, footprint=elem_estrut)
# OBS: A dependência selem foi removida da lista de argumentos da binary_dilation na sua atualização 1.0.
# A dependência atual é o footprint, e possível executar o comando apenas passando o parâmetro desejado.

plt.figure(1)
plt.subplot(1, 3, 1)
plt.imshow(A, cmap='gray')
plt.subplot(1, 3, 2)
plt.imshow(elem_estrut, cmap='gray')
plt.subplot(1, 3, 3)
plt.imshow(Ad, cmap='gray')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
