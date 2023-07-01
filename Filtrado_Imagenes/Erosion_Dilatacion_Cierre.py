"""
FILTROS
autor: Alejandra De la cruz De la cruz
"""

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\coins.png", 0)
_, th  = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) #Binarizacion

kernel = np.ones((3,3), np.uint8)

# erosion = cv2.erode(th, kernel, iterations= 1)
dilatacion = cv2.dilate(th, kernel, iterations= 1)
erosion = cv2.erode(dilatacion, kernel, iterations= 5)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen erosionada", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen dilatada", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Imagen erosionada", erosion)
cv2.imshow("Imagen dilatada", dilatacion)
cv2.waitKey(0)
cv2.destroyAllWindows()

""" Morfologia de cierre """
img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\coins.png", 0)
_, th  = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) #Binarizacion

kernel = np.ones((3,3), np.uint8)

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Close", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Close", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""Eliminar elementos no deseados"""
img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\opening.png", 0)
_, th  = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) #Binarizacion

kernel = np.ones((3,3), np.uint8)

#Aplicar una erosion para eliminar los puntos 
erosion = cv2.erode(th, kernel, iterations= 1)

#Aplicar una dilatacion para volver a su estado original
dilatacion = cv2.dilate(erosion, kernel, iterations= 1)

cv2.namedWindow("Imagen Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen erosionada", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen dilatada", cv2.WINDOW_NORMAL)

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen erosionada", erosion)
cv2.imshow("Imagen dilatada", dilatacion)

cv2.waitKey(0)
cv2.destroyAllWindows()

""" Morfologia de apertura """
img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\coins.png", 0)
_, th  = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) #Binarizacion

kernel = np.ones((3,3), np.uint8)

openx = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Open", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Open", openx)

cv2.waitKey(0)
cv2.destroyAllWindows()