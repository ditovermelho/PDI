""" 
Questão 06:
Modifique o código abaixo, inserindo a linha de código que implementa o filtro Butterworth
passa baixa. Comente a operação realizada e os resultados produzidos. Comente sobre a
influência do parâmetro F_corte.
"""
# Imports
import numpy as np
from d import euclidiana
from matplotlib import pyplot as plt
from scipy import ndimage
from scipy.fftpack import fft2, fftshift, ifft2
from skimage.io import imread

I = imread('./img/Laboratorio_4_1.tif', as_gray=True)
l, c = I.shape
noise = 15*np.random.normal(0, 1, (l, c))
In = I + noise
F = fft2(I)
# Desloca o componente de frequência zero para o centro do espectro
F = fftshift(F)
l, c = F.shape
H = np.ones((l, c), dtype=float)
F_corte = 70.0
centro = (l//2, c//2)

for i in range(l):
    for j in range(c):
        p = (i, j)
        D = euclidiana(centro, p)
        n = 1  # ordem do filtro
        H[i, j] = 1 / (1 + (D/F_corte)**(2*n))  # Butterworth passa baixa

F_new = F*H
I_filt = ifft2(F_new)
plt.figure(figsize=[10, 10])
plt.subplot(2, 2, 1)
plt.imshow(In, cmap='gray')
plt.subplot(2, 2, 2)
F_abs = np.abs(F)
f_ganho = np.log10(F_abs)
F_abs = 255*f_ganho/np.max(f_ganho)
plt.imshow(F_abs, cmap='gray')
plt.subplot(2, 2, 3)
plt.imshow(H, cmap='gray')
plt.subplot(2, 2, 4)
plt.imshow(np.abs(I_filt), cmap='gray')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
