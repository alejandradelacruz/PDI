"""
FILTROS PASA BAJA
autor: Alejandra De la cruz De la cruz
"""
import cv2

#filtro de desenfoque medio
img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\images.jpg", 0)
imgmedian = cv2.medianBlur(img, 9) #Aplicamos un filtro de desenfoque medio con un kernel de un solo digito 

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Modificada", imgmedian) #Resultado de eliminar el ruido de la sal y pimienta, pero no visible para el ser humano 
cv2.waitKey(0)
cv2.destroyAllWindows()