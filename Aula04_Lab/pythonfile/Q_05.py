"""
Questão 5:
Além do operador Laplaciano, existem outros operadores para detecção de bordas, tais como os operadores 
de Sobel e Prewitt. Tais operadores são clássicos, sendo um dos primeiros operadores propostos. No 
entanto, outros operadores menos conhecidos podem gerar bons resultados.  Utilize a imagem 
Laboratorio_4_2.jpg e plote suas versões filtradas utilizando os operadores: Sobel, Prewitt e Scharr. 
"""
# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Lê a imagem
img = cv2.imread('./img/Laboratorio_4_2.jpg', cv2.IMREAD_GRAYSCALE)

# Aplica o operador Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(np.power(sobelx, 2) + np.power(sobely, 2))

# Aplica o operador Prewitt
prewittx = cv2.filter2D(
    img, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
prewitty = cv2.filter2D(
    img, -1, np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]))
prewitt = np.sqrt(prewittx**2 + prewitty**2)

# Aplica o operador Scharr
scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharr = np.sqrt(scharrx**2 + scharry**2)

# Plota as imagens filtradas
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 6))
ax = axes.ravel()
ax[0].imshow(img, cmap='gray')
ax[0].set_title('Original')
ax[1].imshow(sobel, cmap='gray')
ax[1].set_title('Filtro Sobel')
ax[2].imshow(prewitt, cmap='gray')
ax[2].set_title('Filtro Prewitt')
ax[3].imshow(scharr, cmap='gray')
ax[3].set_title('Filtro Scharr')

"""
cv2.imshow('Original', img)
cv2.imshow('Sobel', sobel.astype(np.uint8))
cv2.imshow('Prewitt', prewitt.astype(np.uint8))
cv2.imshow('Scharr', scharr.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas
