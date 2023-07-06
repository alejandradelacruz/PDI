"""
Created on Mon July 07 
@autor: Alejandra De la cruz De la cruz 
"""

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Contornos\\coins.png")
img2 =  img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

#LISTA DE CONTORNOS 
contornos, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Calculando el centroide y dibujando los contornos en la imagen
for index in range(len(contornos)):
    cv2.drawContours(img2, contornos, index, (0,255,0), 5)

    #Momentos de la imagen: Puntos caracteristicos de la imagen 
    cnt = contornos[index]
    momentos = cv2.moments(cnt)

    #Calculando la coordenada x e y del centroide
    cx = int(momentos['m10']/momentos['m00']) 
    cy = int(momentos['m01']/momentos['m00'])

    img = cv2.circle(img, (cx,cy), radius=2, color=(0,0,255), thickness=-1)
    img = cv2.putText(img, str(cx)+ ", "+ str(cy), (cx-20,cy), cv2.FONT_HERSHEY_SIMPLEX, .3, (255,0,0), 1, cv2.LINE_AA)

cantidad = len(contornos)
img2 = cv2.putText(img2, "son " + str(cantidad) + " monedas", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
print("Son " + str(cantidad) + " monedas")

cv2.namedWindow("Imagen Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen Procesada", cv2.WINDOW_NORMAL)
cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL)

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Procesada", closing)
cv2.imshow("Resultado", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
