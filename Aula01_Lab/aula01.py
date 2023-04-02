"""
# Questão 01: Iniciar python utilizando a IDE escolhida, ou o Google Colab. No caso de utilizar uma
IDE, crie uma pasta e comece um novo Project. Abra um novo python file e nomeie
como “aula1”. Caso esteja utilizando o Colab, crie um Novo Notebook, renomeie
para “Aula 1 – PI”. Crie uma célula de código para cada exercício. Digite na primeira
linha:
# coding = utf-8

O caractere # marca o inicio de comentário. Qualquer texto depois do # será ignorado
até o fim da linha, com exceção dos comentários funcionais. utf-8 abrange a maioria dos idiomas existentes. 
No caso do Colab, não é necessário
iniciar com alteração da codificação, pois os notebooks do Colab permitem combinar
código executável e rich text em um só documento, além de imagens, HTML,
LaTeX e muito mais. Quando você cria seus próprios notebooks do Colab, eles são
armazenados na sua conta do Google Drive.

# Questão 02: Em Python, as principais estruturas de dados nativas são: Tuplas, Listas, Dicionários
e Conjuntos. Para trabalhar com matrizes é necessário criar uma lista de listas (onde
cada lista contém uma linha da matriz) ou utilizar pacotes de programação científica
como o Numpy. Numpy é um pacote que inclui a Classe array, a Classe matrix e
várias funções auxiliares utilizadas para manipular estas estruturas de dados. Crie
a matriz A, de tamanho 4x5, cujos valores são: A

Para isso, utilize a estrutura de dados do tipo list. Por exemplo, o comando:

declara uma lista, onde seus elementos correspondem à primeira linha da Matriz.
Declare as demais linhas da matriz em novas listas. Por fim, crie uma lista A que
contém as listas anteriores. Imprima os resultados e o tipo da variável A utilizando
o comando

A = [[1, 1, 2, 1, 3], [1, 1, 2, 3, 1], [2, 2, 3, 2, 2], [1, 3, 2, 1, 1]]

print(A, type(A), '\n')

# Questão 03: Utilize a biblioteca numpy para converter A em uma estrutura do tipo array. Para
isso, insira o comando import numpy as np no topo do script. Em seguida, realize
a conversão da seguinte forma. Imprima a variável M e o seu tipo.

import numpy as np

M =  np.array(A)

print(M, type(M), '\n')

# Questão 04: Utilize a biblioteca numpy para converter A em uma estrutura do tipo matrix. Utilize
o comando. Imprima a variável MM e o seu tipo. Comente (na forma de comentário no código)
sobre as diferenças entre as variáveis M e MM.

MM =  np.matrix(A)

print(MM, type(MM), '\n')

# A variável M e do tipo array ou vetor. Um vetor e uma matriz de uma dimensão ou linha.
# A variável MM e do tipo matriz. O termo matriz e normalmente usado quando a matriz tem mais de uma dimensão,
# tendo no mínimo linhas e colunas.

# Questão 05: A principal biblioteca para gerar gráficos em python se chama Matplotlib. Sua documentação
completa, assim como exemplos de uso pode ser encontrada no site
<https://matplotlib.org/2.1.0/index.html>. Da biblioteca Matplotlib importe apenas
a função pyplot inserindo o seguinte comando no topo do script. Em seguida crie uma imagem em tons de cinza 
utilizando a matriz (a partir de agora, quando nos referirmos a uma matriz mxn, estamos nos referindo a um array 
mxn em python) da seguinte forma:

from matplotlib import pyplot as plt

plt.figure()
plt.imshow(M, cmap='gray')
plt.show()

# Questão 06: Utilize o comando. para gerar uma imagem a partir de uma matriz de números aleatórios do tipo float
no intervalo [0,1). Insira o comando. Antes do comando plt.show() e comente o resultado gerado.

from matplotlib import pyplot as plt

imagem_aleatoria = np.random.random([500,500])

plt.figure()
plt.imshow(imagem_aleatoria, cmap='gray')
plt.colorbar()
plt.show()

# Ao executar o código temos um imagem estatica em preto, branco e cinza
# que lembra muito uma tv de tubo com interferência eletromagnetica

# Questão 07: Sckit image exemplos – É possível trabalhar com Processamento de Imagem em
Python utilizando um dos três pacotes que segue: OpenCV, PIL e Scikit-image. O
primeiro é, talvez, a biblioteca mais conhecida e completa para PI, desenvolvida
em linguagem C, podendo ser instalada e importada para trabalhar em Python. A
segunda e a terceira são bibliotecas desenvolvidas especificamente para a linguagem
Python, sendo a terceira mais recente e ainda em desenvolvimento. No pacote
scikit-image existe uma base de dados de imagens, que podem ser importadas para
visualização e teste de técnicas de PI. Digite o comando from skimage import data
no início do script (ou célula), e em seguida o código abaixo. Comente os resultados

from skimage import data

plt.figure()
moedas = data.coins()
print('Shape:', moedas.shape)
print('Tipo:', type(moedas))
print('Tipo de dados:', moedas.dtype)
plt.imshow(moedas, cmap='gray')
plt.show()

# Ao executar o código temos os resultados para moedas:
# Shape de (303, 384)
# Tipo array
# Tipo de dados uint8
# Que resultam em uma imagem de uma coleção de moedas em preto e branco.

# Questão 08: Repita o exemplo anterior, porém substituindo o comando moedas = data.coins()
por astronauta = data.astronaut(). Faça as mudanças necessárias para executar o
código. Comente os resultados.

plt.figure()
astronauta = data.astronaut()
print('Shape:', astronauta.shape)
print('Tipo:', type(astronauta))
print('Tipo de dados:', astronauta.dtype)
plt.imshow(astronauta, cmap='gray')
plt.show()

# Ao executar o código temos os resultados para astronauta:
# Shape de (512, 512, 3)
# Tipo array
# Tipo de dados uint8
# Que resultam em uma imagem de uma Astronauta colorida.

# Questão 09: Execute o código abaixo e comente os resultados.

astronauta = data.astronaut()
plt.figure()
plt.subplot(1,3,1)
plt.imshow(astronauta[:,:,0],cmap='gray')
plt.subplot(1,3,2)
plt.imshow(astronauta[:,:,1],cmap='gray')
plt.subplot(1,3,3)
plt.imshow(astronauta[:,:,2],cmap='gray')
plt.show()

# Ao executar o código temos os resultados para astronauta:
# Três imagens de uma Astronauta em preto e branco,
# Sendo a primeira tendo a sua tonalide mas voltada para o branco,
# A segunda tem sua tonalidade mas voltada para o cinza,
# E a terceira possui sua tonalidade mas voltada para o preto.

# Questão 10: Escrever um código que gere a imagem como a matriz abaixo e plote uma imagem
em tons de cinza. Sugestão: utilize a função range (inicial, final, incremento).
matriz de 40 por 40, com elementos que vão do 1 ao 40 em cada linha.

"""
import numpy as np
from matplotlib import pyplot as plt

# from skimage import data

imagem = []
lista = []

lista += range(1, 41)

for _ in range(1, 41):
    imagem.append(lista)

imagem = np.matrix(imagem)
plt.figure()
print('Shape:', imagem.shape)
print('Tipo:', type(imagem))
print('Tipo de dados:', imagem.dtype)
plt.imshow(imagem, cmap='gray')
plt.show()

#
