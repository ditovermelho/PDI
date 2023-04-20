""" 
Questão 02:
Faça o download da imagem Laboratorio_4_1.tif e salve na pasta onde se encontra o script aula4.py.  
Estando no Colab, fazer upload para o armazenamento da sessão. Realize a filtragem desta imagem 
utilizando o filtro da Média de Vizinhança 3x3, 5x5, 7x7, 9x9 e 25x25. Plote todas as imagens 
(original e suas versões filtradas).  Se o relatório não for enviado via Colab, inserir o 
código escrito no relatório. (Sugestão: declare as máscaras e utilize a função ndimage.convolve.  
Ver notas de aula.)

"""
# Imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from skimage import io

# Carregando a imagem
image = io.imread('./img/Laboratorio_4_1.tif')

# Definindo os tamanhos dos filtros
sizes = [3, 5, 7, 9, 25]

# Criando as máscaras dos filtros
masks = [np.ones((size, size), dtype=np.float32)/(size**2) for size in sizes]

# Aplicando as máscaras
Imgfilt = [ndimage.convolve(image, mask) for mask in masks]

# Plotando as imagens
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 6))
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original')
for i, Imgfilt in enumerate(Imgfilt):
    ax[i+1].imshow(Imgfilt, cmap='gray')
    ax[i+1].set_title(f'Filtro {sizes[i]}x{sizes[i]}')
plt.tight_layout()
plt.show()
