"""
Questão 06:
Execute o código abaixo, comente linha por linha, e os resultados de forma geral.
"""
# Imports
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage.io import imread

# I recebe a imagem Laboratorio_4_1.tif
I = imread('./img/Laboratorio_4_1.tif', as_gray=True)
# l e c recebem as dimensões de I
l, c = I.shape
# Aumentando a amplitude do ruido
noise = 15*np.random.normal(0, 1, (l, c))

# In resebe a Imagem original mas o ruido
In = I + noise

# Infilt recebe resultado da aplicação do filtro gaussian em In, com 1 de sigma
Infilt = ndimage.gaussian_filter(In, sigma=1)
# Infilt recebe o resultado da aplicação do filtro mediana em I, com tamanho 5x5, com bordas 0.0
Infilt1 = ndimage.median_filter(I, size=5, mode='constant', cval=0.0)

# Definindo uma mask bidimensional de dimensões 3x3 com valor de 1.0/9 de tipo inteiro
mask = 1.0/9 * np.ones((3, 3), dtype='int')
# Infilt2 recebe o resultado da aplicação do filtro convolve em In com a mask, com bordas 0.0
Infilt2 = ndimage.convolve(In, mask, mode='constant', cval=0.0)
# Definindo uma mask2 bidimensional de dimensões 25x25 com valor de 1.0/25 de tipo inteiro
mask2 = 1.0/25 * np.ones((5, 5), dtype='int')
# Infilt3 recebe o resultado da aplicação do filtro convolve em In com a mask2, com bordas 0.0
Infilt3 = ndimage.convolve(In, mask2, mode='constant', cval=0.0)

# PLotando as imagens
plt.figure(figsize=[15, 10])  # Definindo o tamanho da figura
plt.subplot(2, 3, 1)  # Criando um subgrupo de imagens com base na figura
plt.title('Original')  # Defini um titulo para a figura
plt.imshow(I, cmap='gray')   # Exibindo a imagem original em tons de cinza
plt.subplot(2, 3, 2)  # Criando um subgrupo de imagens com base na figura
plt.title('Ruidosa')  # Defini um titulo para a figura
plt.imshow(In, cmap='gray')  # Exibindo a imagem ruidosa em tons de cinza
plt.subplot(2, 3, 3)  # Criando um subgrupo de imagens com base na figura
plt.title('Gaussiano')  # Defini um titulo para a figura
plt.imshow(Infilt, cmap='gray')  # Exibindo a imagem gaussiano em tons de cinza
plt.subplot(2, 3, 4)  # Criando um subgrupo de imagens com base na figura
plt.title('Mediana 3x3')  # Defini um titulo para a figura
plt.imshow(Infilt1, cmap='gray')  # Exibindo a imagem mediana em tons de cinza
plt.subplot(2, 3, 5)  # Criando um subgrupo de imagens com base na figura
plt.title('Media 3x3')  # Defini um titulo para a figura
# Exibindo a imagem media 3x3 em tons de cinza
plt.imshow(Infilt2, cmap='gray')
plt.subplot(2, 3, 6)  # Criando um subgrupo de imagens com base na figura
plt.title('Media 5x5')  # Defini um titulo para a figura
# Exibindo a imagem media 5x5 em tons de cinza
plt.imshow(Infilt3, cmap='gray')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas
