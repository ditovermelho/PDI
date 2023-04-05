"""
Questão 03: Carregue a imagem Laboratorio_3_2.bmp na variável I e em seguida utilize a 
função: Ieq = exposure.equalize_hist(I). Exiba ambas as imagens I e Ieq lado a lado com 
seus respectivos histogramas. Comente os resultados.
"""

import os  # pacote de integração com o sistema operacional

# Importe de pacotes
from matplotlib import pyplot as plt
from skimage import exposure
from skimage.io import imread

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Carregando I com uma matriz NumPy gerada com base na imagem Laboratorio_3_2.
I = imread('./img/Laboratorio_3_2.bmp', as_gray=True)

# Equalizando a imagem I
Ieq = exposure.equalize_hist(I)

# Gerando o Histograma com base em I. A função histogram ira calcular o número de pixels de cada intervalo de intensidade
# (bin) da imagem. Comando e normalmente usado para analisar a  distribuição de intensidade de uma imagem.
hist, bin_centers = exposure.histogram(I, normalize=False)
l = hist.shape  # l recebe o tamanho do array "hist".
x = range(l[0])  # número de bins para visualizar o histograma da imagem I.

# Gerando o Histograma com base em Iqe.
hist_eq, bin_centers_eq = exposure.histogram(Ieq, normalize=False)
l_eq = hist_eq.shape  # l_qe recebe o tamanho do array "hist_eq".
# número de bins para visualizar o histograma da imagem Ieq.
x_eq = range(l_eq[0])

# Para identificar o tom de cinza com maior frequência da imagem original
gray_value = bin_centers[hist.argmax()]

# Para identificar a frequência da tonalidade de cinza mais comum da imagem original
frequency = hist.max()

# Para identificar o tom de cinza com maior frequência da imagem Equalizando
gray_value_eq = bin_centers[hist_eq.argmax()]

# Para identificar a frequência da tonalidade de cinza mais comum da imagem Equalizando
frequency_eq = hist_eq.max()

# Imprimir o resultado
print(
    f"A tonalidade de cinza com a maior frequência da imagem original é {gray_value}, e ela apareceu é {frequency} vezes.")

print(
    f"A tonalidade de cinza com a maior frequência da imagem equalizada é {gray_value_eq}, e ela apareceu é {frequency_eq} vezes.")

# Definindo o tamanho da imagem
plt.figure(figsize=[20, 5])

plt.subplot(2, 3, 1)  # Criando um subgrupo de imagens com base na figura
plt.imshow(I, cmap='gray')  # Exibindo a imagem original em tons de cinza
plt.title('Imagem em tons de cinza.')  # Definido um titulo para imagem

plt.subplot(2, 3, 2)  # Criando um subgrupo de imagens com base na figura
# Plotando um gráfico de linhas usando os valores de x no eixo horizontal e hist no eixo vertical.
plt.bar(x, hist)
plt.title('Histograma em gráfico de barras.')  # Definido um titulo para imagem

plt.subplot(2, 3, 4)  # Criando um subgrupo de imagens com base na figura
plt.imshow(Ieq, cmap='gray')  # Definido um titulo para imagem equalizando
# Definido um titulo para imagem
plt.title('Imagem Equalizando em tons de cinza.')

plt.subplot(2, 3, 5)  # Criando um subgrupo de imagens com base na figura
# Plotando um gráfico de linhas usando os valores de x_eq no eixo horizontal e hist_eq no eixo vertical.
plt.bar(x_eq, hist_eq)
# Definido um titulo para imagem
plt.title('Histograma de Ieq em gráfico de barras.')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
