"""
Questão 01:
Uma biblioteca muito utilizada em Python, quando o assunto é processamento de sinais, é a biblioteca SciPy: https://scipy.org/. 
Iremos utilizar esta biblioteca para realizar a convolução 2D utilizando duas diferentes abordagens para tratamento dos pixels 
de bordas de uma imagem. Comente o código abaixo identificando a abordagem utilizada para cada uma das duas operações de 
filtragem. Explique em poucas palavras as abordagens utilizadas. (Sugestão: ver notas de aula sobre filtragem no domínio espacial.)
"""


import numpy as np
from scipy import ndimage

Image = np.array([[1, 2, 3, 4, 5], [0, 1, 3, 4, 0], [
                 1, 1, 3, 2, 0], [0, 0, 4, 5, 6], [1, 0, 7, 8, 0]])
mask = np.array([[1, 1, 1], [0, 0, 0], [1, 1, 1]])

Imgfilt = ndimage.convolve(Image, mask, mode='constant', cval=0.0)
Imgfilt2 = ndimage.convolve(Image, mask, mode='wrap')

print(Imgfilt)
print(Imgfilt2)
