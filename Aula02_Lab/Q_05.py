
"""
# Questão 05: Repita o exercício anterior utilizando uma imagem binária 1000x1000, o ponto p com
coordenadas (500,500), e ilumine os pixels q tais que De(p, q)≤60. Plote a imagem
resultante e comente as principais diferenças em relação à imagem gerada no Exercício
4.
"""


import d
import matplotlib.pyplot as plt
import numpy as np

# Valores
tamanho, x, y, valor = 1000, 500, 500, 1
# Criação da matriz de 20x20 com todos os elementos igauis a zero
I = np.zeros((tamanho, tamanho), dtype='int')

# Definindo a função euclidiana

# Deteminação dos pixels com distância Euclidiana menor ou igual a 4
for i in range(tamanho):
    for j in range(tamanho):
        p = (x, y)
        q = (i, j)

        if d.euclidiana(p, q) <= 60:
            I[i, j] = valor

# Plotar a imagem modificada
plt.imshow(I, cmap='gray', vmin=0, vmax=1)
plt.title('Imagem modificada')
plt.tight_layout()
plt.show()
