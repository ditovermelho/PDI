"""
Questão 05:
O dataset digits: Para realizar o último experimento desta aula laboratorial,
utilizaremos o o dataset digits. Este dataset consiste de digitalizações de
dígitos manuscritos para reconhecimento. Cada elemento consiste em uma imagem
8x8 de um dígito. Todas as imagens foram pre-processadas de forma que todas
tenham resolução 8x8 e 16 níveis de cinza. Os vetores de características que
representam as imagens consistem nos próprios pixels das imagens, organizados
na forma de vetor. Execute o código abaixo e observe os resultados.
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits

digitos = load_digits()
print(digitos.data.shape)

imagem1 = digitos.data[0, :].reshape(8, 8)
imagem2 = digitos.data[42, :].reshape(8, 8)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(imagem1, cmap='gray')
plt.title('Imagem 1')

plt.subplot(1, 2, 2)
plt.imshow(imagem2, cmap='gray')
plt.title('Imagem 2')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.
