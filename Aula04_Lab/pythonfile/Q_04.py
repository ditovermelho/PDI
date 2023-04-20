"""
Questão 04:
Faça o download da imagem Laboratorio_4_2.jpg, execute e comente o código abaixo. Responda as seguintes questões: 
Quais os dois filtros utilizados e quais suas principais características? Agora, experimente substituir Imgfilt 
por Imgfilt > 0.07 na função plt.imshow e comente o resultado. (Sugestão:  Ver notas de aula e identifique a 
máscara utilizada nos slides. Faça uma rápida pesquisa no google sobre o filtro laplaciano)
"""
# Imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from skimage import io

I = io.imread('./img/Laboratorio_4_2.jpg', as_gray=True)
Imgfilt = ndimage.laplace(I, mode='constant', cval=0.0)

mask = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
Imgfilt1 = ndimage.convolve(I, mask, mode='constant', cval=0.0)

plt.figure()
plt.imshow(I, cmap='gray')
plt.figure()
plt.imshow(Imgfilt, cmap='gray')
plt.figure()
plt.imshow(Imgfilt1, cmap='gray')
plt.show()
