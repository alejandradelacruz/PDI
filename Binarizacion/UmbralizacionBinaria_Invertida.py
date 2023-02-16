""" UMBRALIZACION BINARIA INVERTIDA """

import cv2

path = r'C:\Users\User\Desktop\PDI\Binarizacion\coins.png'
img = cv2.imread(path, 0)

#Algoritmos de Umbralizacion 
# cv2.threshold(imagem, valor de umbral, umbral maximo, tipo de algoritmo)
#Nos devuelve el umbral establecido y la imagen binarizada
_, th = cv2.threshold(img,100, 255, cv2.THRESH_BINARY)
#Invertido
# _, th = cv2.threshold(img,100, 255, cv2.THRESH_BINARY_INV) 

cv2.imshow("Original", img)
cv2.imshow("Binarizada", th)
cv2.waitKey()
cv2.destroyAllWindows()