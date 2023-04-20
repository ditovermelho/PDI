"""
Questão 03:
Carregue a mesma imagem do exercício anterior e apresente sua versão filtrada com o Filtro da Mediana. 
Utilize uma janela de dimensão 5x5. 
(Sugestão: utilize a função: ndimage.median_filter(I, size=5, mode='constant', cval=0.0))
"""

# Imports
import numpy as np
from scipy import ndimage
from skimage import io

# Carregando a imagem
image = io.imread('./img/Laboratorio_4_1.tif')

# Aplicando o filto da medianda
Imgfilt = ndimage.median_filter(image, size=5, cval=0.0)

# Mostrando a imagem original e sua versão filtrada
io.imshow_collection([image, Imgfilt])
io.show()
