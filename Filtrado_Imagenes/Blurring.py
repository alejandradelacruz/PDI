"""
FILTROS PASA BAJA
autor: Alejandra De la cruz De la cruz
"""
import cv2

#filtro de promediado
img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\salYpimienta.jpg", 0)
imgBlurred = cv2.blur(img,(8,8)) #Aplicamos un filtro de promediado con un kernel de 8x8 a la imagen original 

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Modificada", imgBlurred) #Resultado de eliminar el ruido de la sal y pimienta, pero no visible para el ser humano 
cv2.waitKey(0)
cv2.destroyAllWindows()

