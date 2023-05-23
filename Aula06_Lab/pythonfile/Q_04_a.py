""" 
Algumas operações importantes são geradas a partir de combinações das operações básicas de Erosão e Dilatação, 
como é o caso das operações de Abertura e Fechamento. Utilize a imagem Laboratório_6_3.tif e execute o que se 
pede nas alternativas abaixo.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
# from skimage.io import imread
from skimage.morphology import (binary_closing, binary_dilation,
                                binary_erosion, binary_opening, diamond, disk,
                                rectangle)

# I = imread('./img/Laboratorio_6_3.tif', as_grey=True)
I = cv2.imread('./img/Laboratorio_6_3.tif', cv2.IMREAD_GRAYSCALE)

elem_estrut_1 = disk(1)
elem_estrut_2 = rectangle(2, 4)
# OBS: A dependência selem foi removida da lista de argumentos da binary_dilation na sua atualização 1.0.
# A dependência atual é o footprint, e possível executar o comando apenas passando o parâmetro desejado.
Id_1 = binary_opening(I, footprint=elem_estrut_1)
Id_2 = binary_opening(I, footprint=elem_estrut_2)

# Plotar as imagens
plt.figure(1)
plt.subplot(1, 3, 1)
plt.imshow(I, cmap='gray')
plt.subplot(1, 3, 2)
plt.imshow(Id_1, cmap='gray')
plt.subplot(1, 3, 3)
plt.imshow(Id_2, cmap='gray')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
