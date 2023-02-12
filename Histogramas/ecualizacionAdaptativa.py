"""SE UTILIZA CUANDO NO SE QUIERE PERDER DETALLES EN UNA IMAGEN"""
import cv2
from matplotlib import pyplot as plt
import numpy as np

path = r'C:\Users\User\Desktop\PDI\Histogramas\antes.jpg'
img = cv2.imread(path, 0) #Leemos la imagen de entrada y la guardamos en la variable img 
clahe = cv2.createCLAHE(clipLimit = 5.0, tileGridSize = (8,8)) #Creamos la configuracion para el algoritmo 
#CLAHE con un umbral de 5.0 y un kernes de 8 x 8
cl1 = clahe.apply(img) #Ejecutamos el algoritmo sobre lla imagen de entrada
res = np.hstack((img,cl1)) #Concatenamos la imagen de entrada con la imagen ecualizada 

cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL) #Construimos nuestra ventana donde se mostrara la imagen 
cv2.imshow("Resultado", res) #Mostramos la imagen concatenada
cv2.waitKey()
cv2.destroyAllWindows() 

#Creamos el histograma de la imagen normal
hist, bins = np.histogram(img.flatten(), 256, [0,256]) #Calculamos el histograma con numpy y aplanamos los datos de la imagen de entrada
plt.hist(img.flatten(), 256, [0,256], color = 'b') #Graficamos el histograma
plt.xlim([0,256]) #Definimos limites 
plt.legend('H', loc= 'upper left') #Definimos una leyenda
plt.show() #Mostramos el grafico

#Creamos el histograma de la imagen equalizada
hist, bins = np.histogram(res.flatten(), 256, [0,256])
plt.hist(res.flatten(), 256, [0,256], color = 'r')
plt.xlim([0,256])
plt.legend('H', loc= 'upper left')
plt.show()

