"""
Questão 04:
Utilize um laço for para variar o parâmetro n_neighbors do classificador k-NN
no intervalo [1,15] e, para cada valor deste parâmetro, treine e teste o
classificador armazenando apenas a acurácia. Em seguida, realize um plot onde
na abcissa deve constar o parâmetro n_neighbors e na ordenada a acurácia.
Analisando o plot, responda a seguinte questão: para quais valores do
parâmetro analisado o classificador obteve a melhor acurácia? E a menor? Obs.
Para realizar este experimento defina o parâmetro random_state=10 na função
train_test_split, isso garantirá que para cada simulação, conjuntos diferentes
de treinamento e teste serão gerados
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=10)

n_neighbors_range = range(1, 16)
accuracies = []

for n_neighbors in n_neighbors_range:
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = np.mean(y_pred == y_test)
    accuracies.append(accuracy)

plt.plot(n_neighbors_range, accuracies, marker='o')
plt.xlabel('n_neighbors')
plt.ylabel('Acurácia')
plt.title('Acurácia em função do número de vizinhos')

plt.tight_layout()  # Ajuste automático no espaçamento entre subplots
plt.show()  # Exibindo todas as imagens criadas.

best_accuracy = max(accuracies)
best_neighbors = n_neighbors_range[accuracies.index(best_accuracy)]
worst_accuracy = min(accuracies)
worst_neighbors = n_neighbors_range[accuracies.index(worst_accuracy)]

print(
    f"A melhor acurácia foi obtida com n_neighbors = {best_neighbors}:{best_accuracy}")
print(
    f"A pior acurácia foi obtida com n_neighbors = {worst_neighbors}:{worst_accuracy}")
