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
from skimage import data
from skimage.filters import threshold_otsu, threshold_sauvola

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

I = data.camera()  # I recebe a imagem camera do pacote data.

limiar = 128  # criando e atribuindo valor de 128 a limar

# criando e atribuindo valor de threshold_otsu(I) a limiar_otsu
limiar_otsu = threshold_otsu(I)

# criando e atribuindo valor de threshold_sauvola(I) a limiar_sauvola
limiar_sauvola = threshold_sauvola(I)

I_binaria = I > limiar  # Calculando a versão binarizada de I

# Calculando a versão binarizada de I ultilizando Otsu
I_binarizada_otsu = I > limiar_otsu

# Calculando a versão binarizada de I ultilizando Sauvola
I_binarizada_sauvola = I > limiar_sauvola

plt.figure(figsize=[20, 10])  # Definindo o tamanho da imagem

plt.subplot(2, 3, 1)  # Criando um subgrupo de imagens com base na figura
plt.imshow(I, cmap='gray')  # Exibindo a imagem original em tons de cinza
plt.title('Imagem em tons de cinza.')  # Definido um titulo para imagem

plt.subplot(2, 3, 2)  # Criando um subgrupo de imagens com base na figura
# Exibindo a imagem Binarizada com limiar fixo em tons de cinza
plt.imshow(I_binaria, cmap='gray')
# Definido um titulo para imagem
plt.title('Binarização com limiar fixo.')

plt.subplot(2, 3, 4)  # Criando um subgrupo de imagens com base na figura
# Exibindo a imagem Binarizada com algoritmo de Otsu em tons de cinza
plt.imshow(I_binarizada_otsu, cmap='gray')
# Definido um titulo para imagem
plt.title('Imagem Binarizada com algoritmo de Otsu.')

plt.subplot(2, 3, 5)  # Criando um subgrupo de imagens com base na figura
# Exibindo a imagem Binarizada com algoritmo de Sauvola em tons de cinza
plt.imshow(I_binarizada_sauvola, cmap='gray')
# Definido um titulo para imagem
plt.title('Imagem Binarizada com algoritmo de Sauvola.')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.

# Imprimindo os valores de limiar
print("Limiar com valor fixo:", limiar)
print("Limiar de Otsu:", limiar_otsu)
print("Limiar de Sauvola:", limiar_sauvola)
print("Dimensão do array que armazena o limiar de Sauvola:", limiar_sauvola.shape)
