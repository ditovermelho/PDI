"""
Questão 01:
O algoritmo mais conhecido e utilizado para implementar a Discrete Fourier Transform (DFT),
devido à sua eficiência computacional, é o algoritmo Fast Fourier Transform (FFT). Como
mencionado anteriormente, uma biblioteca muito utilizada em Python, quando o assunto é
processamento de sinais, é a biblioteca SciPy: https://scipy.org/, que inclui uma série de
funções úteis para o desenvolvimento de sistemas de processamento de sinais em geral. Iremos
utilizar o módulo scipy.fftpack que fornece uma implementação da FFT. Para o cálculo da FFT
e a visualização adequada do eixo de frequências é preciso conhecer a frequência de amostragem
(𝐹𝑠) do sinal. Dessa forma, para um sinal real, o eixo de frequência compreende o intervalo
[0,𝐹𝑠2⁄]. Este fato é uma consequência do Teorema de Nyquist, que define a maior frequência
possível de ser visualizada pela decomposição em frequência.

Para fins de ilustração, considere a senóide da equação (1) como um sinal contínuo a ser
amostrado a uma taxa de 𝐹𝑠=200 Hz. O código abaixo realiza a discretização deste sinal,
calcula a FFT e visualiza seu conteúdo de frequência.

Execute o código a cima e observe o resultado. Note que para a identificação das frequências,
é preciso gerar um novo eixo, o eixo de frequência (xf). Note também a simetria do gráfico
gerado pela DFT: apenas metade do eixo de frequência traz informações úteis (caso em que o
sinal é real). Para cada bin de frequência 𝑘, a frequência associada pode ser calculada como
"""
# Imports
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft

Fs = 256
dt = 1  # intervalo de tempo em que se pretende vis ualizar o sinal do domínio do tempo
x = np.linspace(0, dt, dt*Fs)
y = np.sin(10*2.0*np.pi*x)
Nfft = dt*Fs  # Número de pontos da FFT (mesmo número de pontos do sinal)
yf = fft(y, Nfft)
xf = np.linspace(0, Fs/2, Nfft//2)
magnitude = np.abs(yf)
plt.figure(figsize=[20, 5])
plt.subplot(1, 3, 1)
plt.xlabel('tempo (t)')
plt.ylabel('y(t)')
plt.plot(x, y)
plt.subplot(1, 3, 2)
plt.title('Simetria do grafico da DFT: utilizase apenas metade do eixo de freq. para visualizacao(Fs/2)')
plt.xlabel('Frequencia (Hz)')
plt.ylabel('Magnitude')
plt.plot(magnitude)
plt.subplot(1, 3, 3)
plt.xlabel('Frequencia (Hz)')
plt.ylabel('Magnitude')
plt.plot(xf, magnitude[0:Nfft//2])

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
