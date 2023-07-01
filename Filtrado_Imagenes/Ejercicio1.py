import cv2
import numpy as np

img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\a.jpg", 0)
equializacion = cv2.equalizeHist(img)

blur = cv2.blur(equializacion, (8,8))
blur = cv2.medianBlur(blur, 3)

#Afilamiento de la imagen 
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
afilada = cv2.filter2D(blur, -1, sharpen_kernel)

resulado = np.hstack((img, equializacion, blur, afilada)) #concatenar imagenes 

cv2.namedWindow("Resultado general", cv2.WINDOW_NORMAL)
cv2.imshow("Resultado general", resulado)
cv2.waitKey(0)
cv2.destroyAllWindows()