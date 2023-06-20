"""
Questão 03:
Utilize o classificador já treinado para classificar o seguinte vetor de
características: x_new= np.array([[3,4,5,2]]). A qual espécie da planta Iris
pertence esse novo vetor?
"""
import numpy as np
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

x_new = np.array([[3, 4, 5, 2]])

new_prediction = knn.predict(x_new)
print('Espécie da planta Iris:', iris.target_names[new_prediction])
