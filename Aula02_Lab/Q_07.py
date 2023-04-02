"""
# Questão 07: Execute e discuta o código abaixo. Compare com o exercício resolvido da página
29 do material “Aula EAD 1”.
"""
import numpy as np


def normaliza(I, espaco_cor):
    ''' I é uma imagem binária ou em tons de cinza; espaco_cor=[min,max] é uma lista onde min e max são o menor e 
    o maior valor para um pixel no espaço de cor da imagem, respectivamente. '''
    fmax = float(np.max(I))
    fmin = float(np.min(I))
    l, c = np.shape(I)
    for i in range(l):
        for j in range(c):
            I[i, j] = (espaco_cor[1]/(fmax - fmin))*(I[i, j]-fmin)
    return


A = np.array([[300, 320, 330], [45, 105, 170], [255, 350, 120]])
print('Imagem A:')
print(A)

normaliza(A, [0, 255])
print('Imagem A normalizada:')
print(A)
