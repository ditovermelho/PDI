"""
Questão 05: A operação de binarização de uma imagem consiste determinar um limiar abaixo do qual 
os pixels são transformados em zero. Conhecendo o limiar, esta operação se resume a uma simples 
operação lógica pixel a pixel. Por exemplo, para uma dada imagem I em tons de cinza, uma binarização 
pode ser feita da seguinte forma: I_binária = I > limiar. Nesta operação, o processo mais relevante 
consiste na determinação do limiar, e pode influenciar diretamente o resultado obtido. Sendo assim 
execute os seguintes passos:

a) Carregue a imagem I da biblioteca skimage:
    from skimage import data
    I = data.camera() 
    
b) Calcule sua versão binarizada assumindo:
    limiar = 128 
    
c) Calcule sua versão binarizada utilizando o algoritmo de Otsu:
    from skimage.filters import threshold_otsu, threshold_sauvola
    limiar2 = threshold_otsu(I)
    
d) Calcule sua versão binarizada utilizando o algoritmo de Savoula: 
    limiar3 = threshold_sauvola(I)
    
e) Plote a imagem original e suas versões binarizadas na mesma figura. Insira os títulos adequadamente. 

f) Imprima os valores de cada limiar calculado e a dimensão do array que armazena o limiar Sauvola. 

g) Comente os resultados. Se o objetivo for retirar o fundo (background) da imagem, qual método seria mais 
adequado? E se o objetivo for detectar bordas?
"""

import os  # pacote de integração com o sistema operacional.

# Importe de pacotes.
from matplotlib import pyplot as plt
from skimage import data, exposure
from skimage.filters import threshold_otsu, threshold_sauvola

I = data.camera()  # I recebe a imagem camera do pacote data.

limiar = 128

I_binária = I > limiar
