"""
Questão 01:
Uma biblioteca muito utilizada em Python, quando o assunto é processamento de sinais, é a biblioteca SciPy: https://scipy.org/. 
Iremos utilizar esta biblioteca para realizar a convolução 2D utilizando duas diferentes abordagens para tratamento dos pixels 
de bordas de uma imagem. Comente o código abaixo identificando a abordagem utilizada para cada uma das duas operações de 
filtragem. Explique em poucas palavras as abordagens utilizadas. (Sugestão: ver notas de aula sobre filtragem no domínio espacial.)
"""

# Imports
import numpy as np
from scipy import ndimage

# Imagem recebe um array
Image = np.array([[1, 2, 3, 4, 5], [0, 1, 3, 4, 0], [
                 1, 1, 3, 2, 0], [0, 0, 4, 5, 6], [1, 0, 7, 8, 0]])
# mask recebe um array
mask = np.array([[1, 1, 1], [0, 0, 0], [1, 1, 1]])
"""
Imgfilt e imgflite recebem o resultado da convolução da imagem original onde:
Image: é a imagem a ser convolucionada com a máscara
mask: é a máscara que será usada para convolucionar a imagem
mode: especifica o modo de lidar com os pixels na borda da imagem. Pode ser 'constant', 'nearest', 'mirror' ou 'wrap'. O valor 
padrão é 'constant'.
cval: é o valor constante usado para preencher pixels na borda da imagem quando o modo é 'constant'
"""
Imgfilt = ndimage.convolve(Image, mask, mode='constant', cval=0.0)
Imgfilt2 = ndimage.convolve(Image, mask, mode='wrap')

# apresentando em terminal o resultado das operações de filtragem 
print(Imgfilt)
print(Imgfilt2)
