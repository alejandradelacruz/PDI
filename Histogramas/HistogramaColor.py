import cv2
from matplotlib import pyplot as plt
import numpy as np 


path = r'C:\Users\User\Desktop\PDI\Histogramas\lena.png'
img = cv2.imread(path) 

#Le da color a nuestro histograma
color = ('b', 'g', 'r')

for i,col in enumerate(color): #Recorremos la variable color usando un ciclo for y con enumerate obtenemos cada espacio de la tupla enumerada
    #Es decir, 0 b; 1 g; 2 r
    print(i,col)
    hist = cv2.calcHist([img], [i], None, [256], [0,255]) #Calculamos el histograma para cada canal de la imagen 
    plt.plot(hist, color = col) #Graficamos el histograma por color
    plt.xlim([0,256]) #Definimos el rango 

plt.show() #Mostramos el histograma