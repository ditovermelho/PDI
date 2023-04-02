"""
# Questão 03: Implemente uma função que, dados dois pontos p = (x, y) e q = (s, t), calcule a
distância Euclidiana
De(p, q) = √ (x − s)2 + (y − t)2
Em seguida, calcule a distância entre os pontos p = (0, 2) e q = (2,4). Chame esta
função de d_euclidiana (p, q).
"""
import d

p = (0, 2)
q = (2, 4)
dist = d.euclidiana(p, q)
print(dist)
