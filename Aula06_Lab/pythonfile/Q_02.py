""" 
Faça o download das imagens Laboratorio_6_1.tif e realize a operação de dilatação pelo elemento estruturante representado por B:
𝐵=[0 1 0 1 1 1 0 1 0 ].
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carregar a imagem
image = cv2.imread('./img/Laboratorio_6_1.tif', cv2.IMREAD_GRAYSCALE)

# Definir o elemento estruturante B
B = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)

# Realizar a dilatação
dilated_image = cv2.dilate(image, B, iterations=1)

# Plotar as imagens
plt.figure(figsize=(10, 10))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')

plt.subplot(1, 2, 2)
plt.imshow(dilated_image, cmap='gray')
plt.title('Imagem Dilatada')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
