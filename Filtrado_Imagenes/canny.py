import cv2
import numpy as np

# img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\coins.png", 0)

# bordes = cv2.Canny(img, 135, 255)

# cv2.imshow("Resultado", bordes)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\coins.png", 0)

# gaussiana = cv2.GaussianBlur(img, (9,9), 0)
# _, th = cv2.threshold(gaussiana, 100, 255, cv2.THRESH_BINARY)

# bordes = cv2.Canny(th, 135, 255)
# cv2.imshow("Resultado", bordes)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

imgA = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\coins.png")
imgB = imgA.copy()
img = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)

gaussiana = cv2.GaussianBlur(img, (9,9), 0)

_, th = cv2.threshold(gaussiana, 100, 255, cv2.THRESH_BINARY)

bordes = cv2.Canny(th, 135, 255)

alto, largo = img.shape

for i in range(largo):
    for j in range(alto):
        if bordes[j,i] == 255:
            imgB[j,i] = (0,155,0)

cv2.imshow("Original", imgA)
cv2.imshow("Bordes", bordes)
cv2.imshow("Resultado", imgB)
cv2.waitKey(0)
cv2.destroyAllWindows()