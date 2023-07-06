"""
Created on Mon July 07 
@autor: Alejandra De la cruz De la cruz 
"""

from contextlib import closing
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Contornos\\coins.png")
img2 = img.copy()

#Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Binarizar la imagen 
_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

#Crear nuestros kernel
kernel = np.ones((3,3), np.uint8)

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
bordes = cv2.Canny(closing, 135, 255)

#Buscar los contornos de la imagen
contornos, jerarquia = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Dibujar los contornos 
cv2.drawContours(img2, contornos, -1, (0,255,0), 3)

#Cantidad de modenas
cantidadMonedas = len(contornos)
img2 = cv2.putText(img2, "son " + str(cantidadMonedas) + " monedas", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

print("Son " + str(cantidadMonedas) + " monedas")

cv2.imshow("Imagen original", img)
cv2.imshow("Imagen Procesada", closing)
cv2.imshow("Imagen con bordes", bordes)
cv2.imshow("Resultado", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()