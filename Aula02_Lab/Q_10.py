# Questão 10

"""
Comandos de instalação de Bibliotecas: 

pip install numpy
python -m pip install -U matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np

import d

Iq = 0.5*np.ones((500, 500), dtype='int')
Ic = 0.5*np.ones((500, 500), dtype='int')

p = (200, 200)
pc = (300, 300)

for i in range(500):
    for j in range(500):
        q = (i, j)
        if d.chebyshev(p, q) <= 100:
            Iq[i, j] = 0
        if d.euclidiana(pc, q) <= 100:
            Ic[i, j] = 0

a = Iq - Ic
b = np.minimum(Iq, Ic)
c = np.maximum(Iq+0.5, Ic)

plt.figure(1)
plt.subplot(1, 3, 1)
plt.imshow(a, cmap='gray', vmin=0, vmax=1)
plt.title('Iq – Ic')

plt.subplot(1, 3, 2)
plt.imshow(b, cmap='gray', vmin=0, vmax=1)
plt.title('Iq and Ic')

plt.subplot(1, 3, 3)
plt.imshow(c, cmap='gray', vmin=0, vmax=1)
plt.title('Iq+0.5 or Ic')

plt.tight_layout()
plt.show()
