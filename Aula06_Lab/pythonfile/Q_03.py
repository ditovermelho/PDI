""" 
Utilizando a imagem Laboratorio_6_2.png, realizar a operação de dilatação pelos seguintes elementos estruturantes: 
b) Elemento tipo disco com raio 1 
c) Elemento tipo disco com raio 4 
d) Elemento tipo diamante com raio 2 
e) Elemento tipo diamante com raio 5 
Adicione no relatório apenas os plots. Cada plote deve conter: Imagem original, elemento estruturante e imagem dilatada
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carregar a imagem original
imagem_original = cv2.imread('./img/Laboratorio_6_2.tif', cv2.IMREAD_GRAYSCALE)

# Elemento tipo disco com raio 1
elemento_1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
dilatada_1 = cv2.dilate(imagem_original, elemento_1)

# Elemento tipo disco com raio 4
elemento_2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
dilatada_2 = cv2.dilate(imagem_original, elemento_2)

# Elemento tipo diamante com raio 2
elemento_3 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
dilatada_3 = cv2.dilate(imagem_original, elemento_3)

# Elemento tipo diamante com raio 5
elemento_4 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilatada_4 = cv2.dilate(imagem_original, elemento_4)

# Plotar as imagens
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(10, 6))
ax = axes.ravel()
ax[0].plot(imagem_original, 'gray')
ax[0].set_title('Imagem Original')
ax[1].plot(elemento_1, 'gray')
ax[1].set_title('Elemento tipo disco (raio 1)')
ax[2].plot(dilatada_1, 'gray')
ax[2].set_title('Imagem Dilatada (raio 1)')
ax[3].plot(elemento_2, 'gray')
ax[3].set_title('Elemento tipo disco (raio 4)')
ax[4].plot(dilatada_2, 'gray')
ax[4].set_title('Imagem Dilatada (raio 4)')
ax[5].plot(elemento_3, 'gray')
ax[5].set_title('Elemento tipo diamante (raio 2)')
ax[6].plot(dilatada_3, 'gray')
ax[6].set_title('Imagem Dilatada (raio 2)')
ax[7].plot(elemento_4, 'gray')
ax[7].set_title('Elemento tipo diamante (raio 5)')
ax[8].plot(dilatada_4, 'gray')
ax[8].set_title('Imagem Dilatada (raio 5)')


plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
