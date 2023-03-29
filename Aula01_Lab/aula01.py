"""
# Questão 01
# coding = utf-8

# Questão 02
A = [[1, 1, 2, 1, 3], [1, 1, 2, 3, 1], [2, 2, 3, 2, 2], [1, 3, 2, 1, 1]]

print(A, type(A), '\n')

# Questão 03

import numpy as np

M =  np.array(A)

print(M, type(M), '\n')

# Questão 04

MM =  np.matrix(A)

print(MM, type(MM), '\n')

# A variavel M e do tipo array ou vetor. Um vetor e uma matriz de uma dimenção ou linha.
# A variavel MM e do tipo matriz. O termo matriz e normalmete usado quando a matriz tem mais de uma dimenção,
# tendo no minimo linhas e colunas.

# Questão 05

from matplotlib import pyplot as plt

plt.figure()
plt.imshow(M, cmap='gray')
plt.show()

# Questão 06

from matplotlib import pyplot as plt

imagem_aleatoria = np.random.random([500,500])

plt.figure()
plt.imshow(imagem_aleatoria, cmap='gray')
plt.colorbar()
plt.show()

# Ao executar o código temos um imagem estatica em preto, branco e cinza
# que lembra muito uma tv de tubo com interferência eletromagnetica

# Questão 07

from skimage import data

plt.figure()
moedas = data.coins()
print('Shape:', moedas.shape)
print('Tipo:', type(moedas))
print('Tipo de dados:', moedas.dtype)
plt.imshow(moedas, cmap='gray')
plt.show()

# Ao executar o código temos os resultados para moedas:
# Shape de (303, 384)
# Tipo array
# Tipo de dados uint8
# Que resultam em uma imagem de uma coleção de moedas em preto e branco.

# Questão 08

plt.figure()
astronauta = data.astronaut()
print('Shape:', astronauta.shape)
print('Tipo:', type(astronauta))
print('Tipo de dados:', astronauta.dtype)
plt.imshow(astronauta, cmap='gray')
plt.show()

# Ao executar o código temos os resultados para astronauta:
# Shape de (512, 512, 3)
# Tipo array
# Tipo de dados uint8
# Que resultam em uma imagem de uma Astronauta colorida.

# Questão 09

astronauta = data.astronaut()
plt.figure()
plt.subplot(1,3,1)
plt.imshow(astronauta[:,:,0],cmap='gray')
plt.subplot(1,3,2)
plt.imshow(astronauta[:,:,1],cmap='gray')
plt.subplot(1,3,3)
plt.imshow(astronauta[:,:,2],cmap='gray')
plt.show()

# Ao executar o código temos os resultados para astronauta:
# Três imagens de uma Astronauta em preto e branco,
# Sendo a primeira tendo a sua tonalide mas voltada para o branco,
# A segunda tem sua tonalidade mas voltada para o cinza,
# E a terceira possui sua tonalidade mas voltada para o preto.

"""
import numpy as np
from matplotlib import pyplot as plt
# from skimage import data

imagem = []
lista = []

lista += range(1, 41)

for _ in range(1, 41):
    imagem.append(lista)

imagem = np.matrix(imagem)
plt.figure()
print('Shape:', imagem.shape)
print('Tipo:', type(imagem))
print('Tipo de dados:', imagem.dtype)
plt.imshow(imagem, cmap='gray')
plt.show()

#
