from matplotlib import pyplot as plt
from skimage import exposure
from skimage.io import imread

I = imread('./pythonfile/Laboratorio_3_1.jpg', as_gray=True)
hist, bin_centers = exposure.histogram(I, normalize=False)
l = hist.shape
x = range(l[0])  # número de bins para visualizar o histograma da imagem I

plt.figure()
plt.title('Imagem em tons de cinza.')
plt.imshow(I, cmap='gray')

plt.figure(figsize=[20, 5])
plt.subplot(1, 3, 1)
plt.title('Histograma em um plote comum')
plt.plot(x, hist)

plt.subplot(1, 3, 2)
plt.title('Histograma em gráfico de barras')
plt.bar(x, hist)

plt.subplot(1, 3, 3)
plt.title('Histograma em gráfico do tipo stem')
plt.stem(x, hist)
plt.show()
