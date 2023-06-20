"""
Questão 01:
A principal biblioteca para se trabalhar com machine learning, no sentido mais
tradicional, é a biblioteca scikit-learn. Existem bibliotecas dedicadas apenas
as técnicas mais recentes de IA, como Deep Learning, Tensor Flow, etc. Exemplos
são as bibliotecas Keras e Theano. Além de implementações de uma série de
classificadores e algoritmos de aprendizagem, também estão disponíveis na
biblioteca scikit-learn ferramentas para manipulação de datasets, extração e
pré-processamento de vetores de características. Toda a documentação, assim
como diversos exemplos de utilização, podem ser encontrados no endereço
https://scikit-learn.org/stable/. Segue abaixo alguns exemplos utilizando a
biblioteca scikit-learn para o problema clássico da classificação da planta
Iris. Neste primeiro momento, o intuito é conhecer o dataset. Para isso,
execute o código abaixo e comente os resultados respondendo a seguinte questão:
Quais informações sobre o dataset Iris estão disponíveis no dicionário iris?
"""
from sklearn.datasets import load_iris

iris = load_iris()

print(iris.data)
print(type(iris.data))
print(iris.feature_names)
print(iris.target)
print(type(iris.target))
print(iris.target_names)
print(iris.data.shape)
