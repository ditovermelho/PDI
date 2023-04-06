""" 
Questão 06: Execute o código abaixo e responda a seguinte questão: que tipo de transformação está sendo 
realizada na imagem carregada? Qual a principal característica dessa operação?
"""

import os  # pacote de integração com o sistema operacional.

# Importe de pacotes.
import numpy as np
from matplotlib import pyplot as plt
from skimage import data, exposure
from skimage.color.colorconv import rgb2gray

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

img = data.eagle()  # Imagem recebe a imagem eagle do pacote data.

# c = o resultado de 255 dividido pelo log do maior valor da imagem mais um.
c = 255/(np.log(1 + np.max(img)))

# Imagem transformada recebe o resultado de log do pixel de imagem mais um vezes c.
img_transformed = c * np.log(1 + img)

# Criando um novo array com base na imagem transformada do tipo uint8.
img_transformed = np.array(img_transformed, dtype=np.uint8)

# Gerando o Histograma com base em imagem. A função histogram ira calcular o número de pixels
# de cada intervalo de intensidade (bin) da imagem.
hist_img, bin_centers_img = exposure.histogram(img)

# número de bins para visualizar o histograma da imagem.
hist_axes_img = range(hist_img.shape[0])

# Gerando o Histograma com base em imagem transformada. A função histogram ira calcular o número de pixels
# de cada intervalo de intensidade (bin) da imagem transformada.
hist_img_transformed, bin_centers_img_transformed = exposure.histogram(
    img_transformed)

# número de bins para visualizar o histograma da imagem transformada.
hist_axes_img_transformed = range(hist_img_transformed.shape[0])

# Definindo o tamanho da imagem
plt.figure(figsize=[15, 10])

plt.subplot(2, 2, 1)  # Criando um subgrupo de imagens com base na figura
plt.title('Imagem original')  # Definido um titulo para imagem
plt.imshow(img, cmap='gray')  # Exibindo a imagem original em tons de cinza

plt.subplot(2, 2, 2)  # Criando um subgrupo de imagens com base na figura
plt.title('Histograma da imagem original')  # Definido um titulo para imagem
# Plotando um gráfico de barras usando os valores de hist_axes_img no eixo horizontal e hist_img no eixo vertical.
plt.bar(hist_axes_img, hist_img)

plt.subplot(2, 2, 3)  # Criando um subgrupo de imagens com base na figura
plt.title('Imagem transformada')  # Definido um titulo para imagem
# Exibindo a imagem transformada em tons de cinza
plt.imshow(img_transformed, cmap='gray')

plt.subplot(2, 2, 4)  # Criando um subgrupo de imagens com base na figura
# Definido um titulo para imagem
plt.title('Histograma da imagem transformada')
# Plotando um gráfico de barras usando os valores de hist_axes_img_transformed no eixo horizontal e
# hist_img_transformed no eixo vertical.
plt.bar(hist_axes_img_transformed, hist_img_transformed)

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
