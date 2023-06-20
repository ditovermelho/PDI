"""
Questão 02:
Como pôde ser observado no Exercício 1, o dataset Iris é constituído dos
atributos já extraídos de todas as imagens. Dessa forma, para treinar um
classificador sobre este (ou qualquer outro) dataset é preciso dividi-lo em
dois subconjuntos: um para treino e outro para teste do classificador. Na fase
de treinamento, o subconjunto de treino será utilizado para calibrar o
classificador tendo como base a acurácia alcançada sobre esse conjunto. Já na
fase de teste, utiliza-se o classificador calibrado para classificar um novo
conjunto de dados (o conjunto de teste), que consiste de exemplos mantidos
escondidos e que serão utilizados para analisar a capacidade de generalização
do classificador. Os resultados obtidos sobre o conjunto de teste é que são
utilizados para demonstrar a eficácia do método estudado. Baseado nestas
informações execute o código abaixo e comente detalhadamente, linha por linha,
o experimento conduzido. Qual o classificador utilizado? Comente seu
desempenho para este dataset.
"""

from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=0)

print(f'Conjunto de treinamento: {X_train.shape}')
print('Conjunto de teste:', X_test.shape)

knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

score = metrics.accuracy_score(y_test, y_pred)
print('Acuracia:', score)
matcon = metrics.confusion_matrix(y_test, y_pred)
print('Matriz de Confusao: \n', matcon)
