""" 
Questão 03:
Faça o download das imagens Laboratorio_4_1.tif e Laboratorio_5_2.png. Digite o código
abaixo e interprete os resultados. Qual a imagem com maior quantidade de informação de baixas
frequências? Justifique.
"""
# Imports
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft2, fftshift
from skimage.io import imread

Ia = imread('./img/Laboratorio_4_1.tif', as_gray=True)
Ib = imread('./img/Laboratorio_5_2.png', as_gray=True)
Fa = fft2(Ia)

# Desloca o componente de frequência zero para o centro do espectro
Fa = fftshift(Fa)
Fb = fft2(Ib)
Fb = fftshift(Fb)
Fa_abs = np.abs(Fa)
f_ganho = np.log10(Fa_abs)
Fa_abs = 255*f_ganho/np.max(f_ganho)
Fb_abs = np.abs(Fb)
f_ganho = np.log10(Fb_abs)
Fb_abs = 255*f_ganho/np.max(f_ganho)

# Mostrando a imagem a e b originais e sus deslocamentos de frequência
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 6))
ax = axes.ravel()
ax[0].imshow(Ia, cmap='gray')
ax[0].set_title('Ia - Original')
ax[1].imshow(Fa_abs, cmap='gray')
ax[1].set_title('Ia - Deslocamento de frequência')
ax[2].imshow(Ib, cmap='gray')
ax[2].set_title('Ib - Original')
ax[3].imshow(Fb_abs, cmap='gray')
ax[3].set_title('Ib - Deslocamento de frequência')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
