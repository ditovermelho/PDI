
import math

# Definindo a função euclidiana


def euclidiana(p, q):
    x, y = p
    s, t = q
    return math.sqrt((x - s)**2 + (y - t)**2)

# Definindo a função chebyshev


def chebyshev(p, q):
    return max(abs(p[0] - q[0]), abs(p[1] - q[1]))
