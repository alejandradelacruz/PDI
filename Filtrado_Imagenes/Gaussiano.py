"""
FILTROS PASA BAJA
autor: Alejandra De la cruz De la cruz
"""
import cv2

#filtro gaussiano 
img = cv2.imread("C:\\Users\\User\\Desktop\\PDI\\Filtrado_Imagenes\\images.jpg", 0)
imgGaussiano = cv2.GaussianBlur(img,(9,9), 0) #Aplicamos un filtro de promediado con un kernel de impar y una desviacion estandar de 0 a la imagen original 

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Modificada", imgGaussiano) #Resultado de eliminar el ruido de la sal y pimienta, pero no visible para el ser humano 
cv2.waitKey(0)
cv2.destroyAllWindows()