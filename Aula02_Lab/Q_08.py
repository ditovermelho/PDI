# Questão 08

"""
Comandos de intalação de Bibliotecas: 

python -m pip install -U pip
python -m pip install -U scikit-image
python -m pip install -U matplotlib
"""

import matplotlib.pyplot as plt
from skimage import data
from skimage.color.colorconv import rgb2gray
from skimage.transform import resize

Imagem1 = data.astronaut()
Imagem1 = rgb2gray(Imagem1)
print('Dimensão Imagem1: ', Imagem1.shape)

Imagem2 = data.cat()
Imagem2 = rgb2gray(Imagem2)
print('Dimensão Imagem2: ', Imagem2.shape)

Imagem1_resized = resize(
    Imagem1, (Imagem2.shape[0], Imagem2.shape[1]), anti_aliasing=True)
print('Dimensão Imagem1 modificada: ', Imagem1_resized.shape)

plt.figure(figsize=(10, 20))

plt.subplot(1, 3, 1)
plt.imshow(Imagem1_resized, cmap='gray')
plt.title('Imagem1')

plt.subplot(1, 3, 2)
plt.imshow(Imagem2, cmap='gray')
plt.title('Imagem2')

plt.subplot(1, 3, 3)
plt.title('Imagem1 + Imagem2')
plt.imshow(Imagem1_resized + Imagem2, cmap='gray')

plt.tight_layout()
plt.show()
