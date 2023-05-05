""" 
Questão 05:
Realize uma filtragem passa alta ideal na imagem Laboratorio_4_2.jpg utilizando a
Transformada de Fourier. Plote a imagem original, o espectro de frequência, a função de
transferência H e a imagem processada. Utilize uma frequência de corte F_corte=40.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft2, fftshift, ifft2, ifftshift
from skimage import color, io

# Carrega a imagem
img = io.imread('./img/Laboratorio_4_2.jpg')

# Converte a imagem para escala de cinza, se necessário
if img.ndim == 3:
    img = color.rgb2gray(img)

# Calcula a Transformada de Fourier 2D da imagem
F = fft2(img)

# Desloca a frequência zero para o centro da imagem
F = fftshift(F)

# Calcula a função de transferência H
M, N = img.shape
X, Y = np.meshgrid(np.arange(N), np.arange(M))
D = np.sqrt((X - N/2)**2 + (Y - M/2)**2)
Fcorte = 40
H = np.where(D > Fcorte, 1, 0)

# Aplica a filtragem passa alta ideal na Transformada de Fourier
G = F * H

# Desloca a frequência zero para a posição original
G = ifftshift(G)

# Calcula a Transformada Inversa de Fourier 2D da imagem filtrada
g = ifft2(G)

# Normaliza a imagem filtrada
g = np.real(g)
g = (g - g.min()) / (g.max() - g.min()) * 255

# Plota a imagem original, o espectro de frequência, a função de transferência H e a imagem filtrada
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Imagem original')
axs[0, 1].imshow(np.log10(1 + np.abs(F)), cmap='gray')
axs[0, 1].set_title('Espectro de frequência')
axs[1, 0].imshow(H, cmap='gray')
axs[1, 0].set_title('Função de transferência H')
axs[1, 1].imshow(g, cmap='gray')
axs[1, 1].set_title('Imagem filtrada')
for ax in axs.flat:
    ax.axis('off')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
