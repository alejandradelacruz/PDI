""" UMBRALIZACION DE OTSU """
import cv2
from matplotlib import pyplot as plt

path = r'C:\Users\User\Desktop\PDI\Binarizacion\coins.png'
img = cv2.imread(path, 0)

#Calcular el histograma
his = cv2.calcHist([img], [0], None, [256], [0,255])
plt.hist(img.ravel(), 256, [0,255])
plt.show()

#Calcular la imagen umbralizada 
umbral , th = cv2.threshold(img, 0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(umbral)

cv2.imshow("Original",img)
cv2.imshow("Binarizada", th)

cv2.waitKey()
cv2.destroyAllWindows()
