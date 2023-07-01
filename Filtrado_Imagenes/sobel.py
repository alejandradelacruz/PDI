import cv2
import numpy as np

img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\coins.png", 0)

x = cv2.Sobel(img, cv2.CV_16S, 1,0, ksize=3)
y = cv2.Sobel(img, cv2.CV_16S, 0,1, ksize=3)

absx = cv2.convertScaleAbs(x)
absy = cv2.convertScaleAbs(y)

destino = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)

cv2.imshow("absx", absx)
cv2.imshow("absy", absy)
cv2.imshow("Resultado", destino)
cv2.waitKey(0)
cv2.destroyAllWindows()