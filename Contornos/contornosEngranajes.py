"""
Created on Mon July 07 
@autor: Alejandra De la cruz De la cruz 
"""
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Contornos\\gear1.PNG")
img2 = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Contornos\\gear2.PNG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 150, 255,
                      cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, th2= cv2.threshold(gray2, 150, 255,
                      cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((5,5), np.uint8)
closingImg = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
closingImg2 = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel)

contornos, _ = cv2.findContours(closingImg, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
contornos2, _ = cv2.findContours(closingImg2, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)

contornosLista = []
for index in range(len(contornos)):
    area = cv2.contourArea(contornos[index])
    if area > 500:
        cnt = contornos[index]
        contornosLista.append(cnt)

contornosLista2 = []
for index in range(len(contornos2)):
    area = cv2.contourArea(contornos2[index])
    if area > 500:
        cnt = contornos2[index]
        contornosLista2.append(cnt)


suma = 0.0
for index in range(len(contornosLista)):
    ret = cv2.matchShapes(contornosLista[index],
                          contornosLista2[index], 1,0.0)
    suma += ret

if suma > 0.0009:
    img2 = cv2.putText(img2, "No son iguales", (10,30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1,
                       cv2.LINE_AA)
    cv2.drawContours(img, contornosLista, -1, (0,255,0), 1)
    cv2.drawContours(img2, contornosLista2, -1, (0,0,255), 1)

else:
    img2 = cv2.putText(img2, "Son iguales", (10,30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1,
                       cv2.LINE_AA)
    cv2.drawContours(img, contornosLista, -1, (0,255,0), 1)
    cv2.drawContours(img2, contornosLista2, -1, (0,255,0), 1)

cv2.namedWindow("imagen1", cv2.WINDOW_NORMAL)
cv2.namedWindow("imagen2", cv2.WINDOW_NORMAL)
cv2.imshow("imagen1", img)
cv2.imshow("imagen2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()