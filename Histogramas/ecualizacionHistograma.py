import cv2
from matplotlib import pyplot as plt
import numpy as np

path = r'C:\Users\User\Desktop\PDI\Histogramas\a.jpg'
img = cv2.imread(path, 0) #Leemos la imagen de entrada y la guardamos en la variable img 
equ = cv2.equalizeHist(img) #Realizamos la equalizacion del histograma

res=np.hstack((img,equ)) #Concatenamos la imagen de entrada con la imagen equalizada
cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL) #Construimos nuestra ventana donde se mostrara la imagen 
cv2.imshow("Resultado", res) #Mostramos la imagen concatenada
cv2.waitKey()
cv2.destroyAllWindows() 

#Creamos el histograma de la imagen normal
hist, bins = np.histogram(img.flatten(), 256, [0,256])
plt.hist(img.flatten(), 256, [0,256], color = 'b')
plt.xlim([0,256])
plt.legend('H', loc= 'upper left')
plt.show()

#Creamos el histograma de la imagen equalizada
hist, bins = np.histogram(equ.flatten(), 256, [0,256])
plt.hist(equ.flatten(), 256, [0,256], color = 'r')
plt.xlim([0,256])
plt.legend('H', loc= 'upper left')
plt.show()

