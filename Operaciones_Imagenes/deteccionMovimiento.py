""" BASE DE LA DETECCIÓN DE MOVIMIENTO EN SISTEMAS DE VIDEO VIGILANCIA """
import cv2
import numpy as np

path1 = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\casaVacia.jpg'
img1 = cv2.imread(path1) #Leemos la imagen 1 
img1 = cv2.resize(img1, (500,500)) #Redimensionamos la imagen 1 

path2 = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\casaDibujo.jpg'
img2 = cv2.imread(path2) #Leemos la imagen 2
img2 = cv2.resize(img2, (500,500)) #Redimensionamos la imagen 2 

resultadoResta = cv2.absdiff(img2,img1) #Realizamos la resta de imagenes donde el resultado es el valor absoluto de la diferencia 

cv2.imshow("Casa Vacia", img1)
cv2.imshow("Casa Dibujo", img2)
cv2.imshow("Resultado", resultadoResta)

cv2.waitKey()
cv2.destroyAllWindows()
