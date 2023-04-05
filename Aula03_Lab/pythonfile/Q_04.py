"""
Questão 04: Uma imagem equalizada possui uma função de distribuição acumulativa (do inglês: cumulative distribution function – cdf) 
aproximadamente linear, uma vez que a cdf é a soma acumulativa da ocorrência de todos os níveis de cinza: 𝑐𝑑𝑓(𝑖)=Σℎ(𝑗)/𝑁𝑗≤𝑖,
   onde ℎ(𝑖) indica o número de pixels com intensidade 𝑖 e 𝑁 o número total de pixels da imagem. Por exemplo, no cenário idea
   uma imagem equalizada possui exatamente a mesma quantidade de pixels para cada tom de cinza (intensidade
   Executar e explicar cada linha do código abaixo:
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

hist_I, bin_centers_I = exposure.histogram(I)  # histograma da imagem original

Ieq = exposure.equalize_hist(I)  # Equalizando a imagem I

# histograma da imagem equalizada
hist_Ieq, bin_centers_Ieq = exposure.histogram(Ieq)

# Calculando a função de distribuição acumulativa de I
cdf_I, bins_I = exposure.cumulative_distribution(I)

# Calculando a função de distribuição acumulativa de Ieq
cdf_Ieq, bins_Ieq = exposure.cumulative_distribution(Ieq)

li = hist_I.shape  # li recebe o tamanho do array "hist".

leq = hist_Ieq.shape  # l_qe recebe o tamanho do array "hist_eq".

xi = range(li[0])  # número de bins para visualizar o histograma da imagem I
# número de bins para visualizar o histograma da imagem Ieq
xeq = range(leq[0])

plt.figure(figsize=[20, 10])  # Definindo o tamanho da imagem

plt.subplot(2, 3, 1)  # Criando um subgrupo de imagens com base na figura
plt.imshow(I, cmap='gray')  # Exibindo a imagem original em tons de cinza

plt.subplot(2, 3, 2)  # Criando um subgrupo de imagens com base na figura
# Plotando um gráfico de linhas usando os valores de bins_I no eixo horizontal e hist_I no eixo vertical.
plt.bar(bins_I, hist_I)

plt.subplot(2, 3, 3)  # Criando um subgrupo de imagens com base na figura
plt.title('CDF para a imagem I')  # Definido um titulo para imagem
# Plotando o histograma da função de distribuição acumulativa de I
plt.plot(bins_I, cdf_I, 'r')

plt.subplot(2, 3, 4)  # Criando um subgrupo de imagens com base na figura
plt.imshow(Ieq, cmap='gray')

plt.subplot(2, 3, 5)  # Criando um subgrupo de imagens com base na figura
# Plotando um gráfico de linhas usando os valores de xeq no eixo horizontal e hist_Ieq no eixo vertical.
plt.bar(xeq, hist_Ieq)

plt.subplot(2, 3, 6)  # Criando um subgrupo de imagens com base na figura
plt.title('CDF para a imagem Ieq')  # Definido um titulo para imagem
plt.plot(bins_Ieq*255, cdf_Ieq, 'r')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
