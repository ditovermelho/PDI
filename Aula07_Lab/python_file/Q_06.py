"""
Questão 06:
Treine e teste o classificador k-NN sobre o dataset Digits. Mantenha o mesmo
protocolo do Exercício 2 (apenas adapte o código). Qual a acurácia encontrada?
"""

from sklearn import metrics
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.3, random_state=0)

knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

score = metrics.accuracy_score(y_test, y_pred)
print('Acurácia:', score)
