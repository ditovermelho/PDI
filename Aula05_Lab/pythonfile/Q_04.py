""" 
Questão 04:
Execute o código abaixo e interprete os resultados. Informe o tipo de processamento
executado sobre a imagem. Qual a frequência de corte utilizada?
"""

# Imports
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft2, fftshift, ifft2
from skimage.io import imread

I = imread('./img/Laboratorio_4_1.tif', as_gray=True)
F = fft2(I)
F = fftshift(F)
l, c = F.shape
H = np.zeros((l, c), dtype=int)
F_corte = 30
centro = (l//2, c//2)


def d_euclidiana(p, q):
    x, y = p
    s, t = q
    d = np.sqrt((x-s)**2 + (y-t)**2)
    return d


for i in range(l):
    for j in range(c):
        p = (i, j)
        D = d_euclidiana(centro, p)
        if D <= F_corte:
            H[i, j] = 1

F_new = F*H
I_filt = ifft2(F_new)

plt.figure(figsize=[10, 10])
plt.subplot(2, 2, 1)
plt.imshow(I, cmap='gray')
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
