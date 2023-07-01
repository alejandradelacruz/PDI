"""
FILTROS PASA BAJA
autor: Alejandra De la cruz De la cruz
"""
import cv2

#filtrado bilateral 
img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\images.jpg", 0)
imgbilateral = cv2.bilateralFilter(img, 9, 75, 75) #Aplicamos un filtro de desenfoque medio con un kernel de un solo digito 
#d: 9, sigmaColor: 75, sigmaSpace: 75 

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Modificada", imgbilateral) #Resultado de eliminar el ruido de la sal y pimienta, pero no visible para el ser humano 
cv2.waitKey(0)
cv2.destroyAllWindows()