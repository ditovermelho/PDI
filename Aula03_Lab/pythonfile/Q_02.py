"""
Questão 02: Repita o Exercício anterior, porém agora utilizando o negativo da imagem Laboratorio_3_1.jpg.
"""

import os  # pacote de integração com o sistema operacional

# Importe de pacotes
from matplotlib import pyplot as plt
from skimage import exposure, util
from skimage.io import imread

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Carregando I com uma matriz NumPy gerada com base na imagem Laboratorio_3_1.
I = imread('./img/Laboratorio_3_1.jpg', as_gray=True)

# Negativando a imagem
I_neg = util.invert(I)

# Gerando o Histograma com base em I. A função histogram ira calcular o número de pixels de cada intervalo de intensidade
# (bin) da imagem. Comando e normalmente usado para analisar a  distribuição de intensidade de uma imagem.
hist, bin_centers = exposure.histogram(I_neg, normalize=False)
l = hist.shape  # l recebe o tamanho do array "hist".
x = range(l[0])  # número de bins para visualizar o histograma da imagem I.

# Para identificar o tom de cinza com maior frequência
gray_value = bin_centers[hist.argmax()]

# Para identificar a frequência da tonalidade de cinza mais comum
frequency = hist.max()

# Imprimir o resultado
print(
    f"A tonalidade de cinza com a maior frequência é {gray_value}, e ela apareceu é {frequency} vezes.")

plt.figure()  # Criando uma nova figura com plotagem vazia
plt.title('Imagem em tons de cinza.')  # Definido um titulo para imagem
# Exibindo uma imagem 2D "I" utilizando uma paleta de cores cinza.
plt.imshow(I_neg, cmap='gray')

plt.figure(figsize=[20, 5])  # Criando uma nova figura com dimensões (20, 5).
plt.subplot(1, 3, 1)  # Criando um subgrupo de imagens com base na figura
plt.title('Histograma em um plote comum')  # Definido um titulo para imagem
# Plotando um gráfico de linhas usando os valores de x no eixo horizontal e hist no eixo vertical.
plt.plot(x, hist)

plt.subplot(1, 3, 2)  # Criando um subgrupo de imagens com base na figura
plt.title('Histograma em gráfico de barras')  # Definido um titulo para imagem
# Plotando um gráfico de linhas usando os valores de x no eixo horizontal e hist no eixo vertical.
plt.bar(x, hist)

plt.subplot(1, 3, 3)  # Criando um subgrupo de imagens com base na figura
# Definido um titulo para imagem
plt.title('Histograma em gráfico do tipo stem')
# Plotando um gráfico de linhas usando os valores de x no eixo horizontal e hist no eixo vertical.
plt.stem(x, hist)
plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
