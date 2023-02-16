""" UMBRALIZACION BINARIA + TRACKBAR """

import cv2
def umbral(valor):
    _, th = cv2.threshold(img,valor,255, cv2.THRESH_BINARY)
    cv2.imshow("Binarizando", th)


cv2.namedWindow("Binarizando")

path = r'C:\Users\User\Desktop\PDI\Binarizacion\coins.png'
img = cv2.imread(path, 0)

#Creamos el trackbar
cv2.createTrackbar("Umbral", "Binarizando", 0, 255, umbral) #va de 0 a 255 y manda llamar a la funcion umbral

cv2.waitKey()
cv2.destroyAllWindows()