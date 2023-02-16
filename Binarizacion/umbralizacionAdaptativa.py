""" UMBRALIZACION ADAPTATIVA """
import cv2

kernel = 3
constante = 0

#Construimos las funciones 
def updateKernel(krn): 
    global kernel
    kernel = krn

    if kernel < 3:
        kernel = 3
    elif kernel % 2 == 0:
        kernel += 1
    
    umbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTATIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel, constante)
    cv2.imshow("Binarizada", umbralizada)

def updateConstante(cte):
    global constante
    constante = cte

    umbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTATIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel, constante)
    cv2.imshow("Binarizada", umbralizada)

cv2.namedWindow("Binarizada")

path = r'C:\Users\User\Desktop\PDI\Binarizacion\coins.png'
img = cv2.imread(path, 0)

cv2.createTrackbar("kernel", "Binarizada", kernel, 255, updateKernel)
cv2.createTrackbar("constante", "Binarizada", constante, 255, updateConstante)

cv2.waitKey()
cv2.destroyAllWindows()