"""APLICACION DE MASCARA"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

path = r'C:\Users\User\Desktop\PDI\Histogramas\lena.png'
img = cv2.imread(path, 0) 

mask = np.zeros(img.shape[:2], np.uint8)

mask[0:300, 0:300] = 255

masked_img = cv2.bitwise_and(img, img, mask=mask) #Aplicamos una compuerta AND bit a bit entre img a img, pero solo en la parte de la mascara con pixeles blancos 

histCompleto = cv2.calcHist([img], [0], None, [256], [0, 255])
histMask = cv2.calcHist([img], [0], mask, [256], [0,255])

plt.subplot(221), plt.imshow(img, "gray")
plt.subplot(222), plt.imshow(mask, "gray")
plt.subplot(223), plt.imshow(masked_img, "gray")

#Graficamos los histogramas
plt.subplot(224), plt.plot(histCompleto), plt.plot(histMask)
plt.xlim([0,255])

plt.show()
