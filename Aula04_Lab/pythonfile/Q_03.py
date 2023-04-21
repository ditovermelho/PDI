"""
Questão 03:
Carregue a mesma imagem do exercício anterior e apresente sua versão filtrada com o Filtro da Mediana. 
Utilize uma janela de dimensão 5x5. 
(Sugestão: utilize a função: ndimage.median_filter(I, size=5, mode='constant', cval=0.0))
"""

# Imports
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import io

# Carregando a imagem
image = io.imread('./img/Laboratorio_4_1.tif', as_gray=True)

# Aplicando o filto da medianda
Imgfilt = ndimage.median_filter(image, size=5, cval=0.0)

# Mostrando a imagem original e sua versão filtrada
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original')
ax[1].imshow(Imgfilt, cmap='gray')
ax[1].set_title('Filtro da mediana')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
