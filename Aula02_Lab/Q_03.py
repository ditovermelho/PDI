# Questão 03
import math

# Definindo a função euclidiana


def d_euclidiana(p, q):
    x, y = p
    s, t = q
    dist = math.sqrt((x - s)**2 + (y - t)**2)
    return dist


p = (0, 2)
q = (2, 4)
dist = d_euclidiana(p, q)
print(dist)
