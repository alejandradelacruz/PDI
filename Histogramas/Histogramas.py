import cv2
from matplotlib import pyplot as plt #Importamos la libreria de matplotlib 
import numpy as np 

path = r'C:\Users\User\Desktop\PDI\Histogramas\lena.png'

img = cv2.imread(path, 0) #Leemos la imagen en escala de grises
hist = cv2.calcHist([img], [0], None, [256], [0, 255]) #[Imagen con la que vamos a trabajar], [canal], [Mascara presente], [Numero de parte en el que vamos a dividir el histograma], [rango de gama o intensidad]

#Graficamos el histograma
plt.hist(img.ravel(), 256, [0,255]) #Graficamos el histograma, .ravel nos devuelve la matriz en formato plano continuo, el siguiente datos es en cuantas partes se divide el histograma, el ultimo dato es el rango de gama
plt.show() 




