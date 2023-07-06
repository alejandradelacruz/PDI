"""
Created on Mon July 07 
@autor: Alejandra De la cruz De la cruz 
"""

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Contornos\\tornillos.jpg")
img2 = img.copy()

#Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Binarizar la imagen 
_, th = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)

#Creamos nuestro kernel para discriminar lo que no nos sirve de una imagens
kernel = np.ones((15,15), np.uint8)

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

#Buscar los contornos de la imagen
contornos, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Dibujar los contornos 
cv2.drawContours(img2, contornos, -1, (0,150,200), 20)

#Cantidad de modenas
cantidadTornillos = len(contornos)
img2 = cv2.putText(img2, "son " + str(cantidadTornillos) + " tornillos", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 10, cv2.LINE_AA)

print("Son " + str(cantidadTornillos) + " tornillos")

cv2.namedWindow("Imagen Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen Procesada", cv2.WINDOW_NORMAL)
cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL)

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Procesada", closing)
cv2.imshow("Resultado", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()