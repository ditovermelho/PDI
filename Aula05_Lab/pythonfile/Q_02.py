""" 
Questão 02:
Analise o conteúdo de frequência do sinal

Plote os gráficos do sinal do domínio do tempo e da frequência e responda as seguintes
perguntas justificando: Quais as frequências presentes no sinal? É possível identificar a
frequência em que maior parte da energia do sinal está presente?
"""
import matplotlib.pyplot as plt
import numpy as np

# Definindo o sinal
x = np.linspace(0, 1, num=1000)
y = np.sin(20*np.pi*x) + 0.3*np.sin(200*np.pi*x)

# Calculando a Transformada de Fourier
fft_y = np.fft.fft(y)
freq = np.fft.fftfreq(len(y), d=x[1]-x[0])

# Calculando a densidade espectral de potência
psd_y = np.abs(fft_y)**2 / len(y)

# Plotando o gráfico do sinal no domínio da frequência
# Mostrando a imagem a e b originais e sus deslocamentos de frequência
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
ax = axes.ravel()
ax[0].plot(freq, np.abs(fft_y))
ax[0].set_xlabel('Frequência')
ax[0].set_ylabel('Magnitude')
ax[0].set_title('Sinal no domínio da frequência')
# Plotando o gráfico da PSD do sinal
ax[1].plot(freq, psd_y)
ax[1].set_xlabel('Frequência')
ax[1].set_ylabel('Densidade espectral de potência')
ax[1].set_title('PSD do sinal')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
