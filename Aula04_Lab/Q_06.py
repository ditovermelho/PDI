"""
Questão 06:
Execute o código abaixo, comente linha por linha, e os resultados de forma geral.
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage.io import imread

I = imread('Laboratorio_4_1.tif', as_gray=True)
l, c = I.shape
noise = 15*np.random.normal(0, 1, (l, c))

In = I + noise

Infilt = ndimage.gaussian_filter(In, sigma=1)
Infilt1 = ndimage.median_filter(I, size=5, mode='constant', cval=0.0)

mask = 1.0/9 * np.ones((3, 3), dtype='int')
Infilt2 = ndimage.convolve(In, mask, mode='constant', cval=0.0)
mask2 = 1.0/25 * np.ones((5, 5), dtype='int')
Infilt3 = ndimage.convolve(In, mask2, mode='constant', cval=0.0)

plt.figure(figsize=[15, 10])
plt.subplot(2, 3, 1)
plt.title('Original')
plt.imshow(I, cmap='gray')
plt.subplot(2, 3, 2)
plt.title('Ruidosa')
plt.imshow(In, cmap='gray')
plt.subplot(2, 3, 3)
plt.title('Gaussiano')
plt.imshow(Infilt, cmap='gray')
plt.subplot(2, 3, 4)
plt.title('Mediana 3x3')
plt.imshow(Infilt1, cmap='gray')
plt.subplot(2, 3, 5)
plt.title('Media 3x3')
plt.imshow(Infilt2, cmap='gray')
plt.subplot(2, 3, 6)
plt.title('Media 5x5')
plt.imshow(Infilt3, cmap='gray')
plt.show()
