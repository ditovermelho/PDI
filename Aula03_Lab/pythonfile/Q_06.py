""" 
Questão 06: Execute o código abaixo e responda a seguinte questão: que tipo de transformação está sendo 
realizada na imagem carregada? Qual a principal característica dessa operação?
"""

import numpy as np
from skimage.color.colorconv import rgb2gray

img = data.eagle()
c = 255/(np.log(1 + np.max(img)))
img_transformed = c * np.log(1 + img)
img_transformed = np.array(img_transformed, dtype=np.uint8)
hist_img, bin_centers_img = exposure.histogram(img)
hist_axes_img = range(hist_img.shape[0])
hist_img_transformed, bin_centers_img_transformed = exposure.histogram(
    img_transformed)
hist_axes_img_transformed = range(hist_img_transformed.shape[0])
plt.figure(figsize=[15, 10])
plt.subplot(2, 2, 1)
plt.title('Imagem original')
plt.imshow(img, cmap='gray')
plt.subplot(2, 2, 2)
plt.title('Histograma da imagem original')
plt.bar(hist_axes_img, hist_img)
plt.subplot(2, 2, 3)
plt.title('Imagem transformada')
plt.imshow(img_transformed, cmap='gray')
plt.subplot(2, 2, 4)
plt.title('Histograma da imagem transformada')
plt.bar(hist_axes_img_transformed, hist_img_transformed)
plt.show()
