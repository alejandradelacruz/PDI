import cv2
import numpy as np

"""METODO 1"""
path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\2.png'
imagen = cv2.imread(path) #Leemos la imagen a trsladar
alto, ancho, _ = imagen.shape #Obtenemos sus medidas

escala = 2
tmatriz = np.array([[escala, 0, 0], [0, escala, 0], [0, escala, 1]])
imagen2 = np.zeros((alto*escala, ancho*escala, 3), np.uint8)

for i in range(alto):
    for j in range(ancho):
        pixel = imagen[i,j]
        vector = np.array([j,i,1])
        resultado = np.dot(tmatriz,vector)
        x = resultado[0]
        y = resultado[1]
        imagen2[y,x] = pixel 

cv2.imshow("Original", imagen)
cv2.imshow("escalada", imagen2)

cv2.waitKey()
cv2.destroyAllWindows()

"""METODO 2"""
# path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\im1.png'
# imagen = cv2.imread(path) #Leemos la imagen a trsladar

# escalada = cv2.resize(imagen,(900,700), interpolation=cv2.INTER_CUBIC) ## interpolación bicubica
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_NEAREST) ## interpolación de vecinos cercanos
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_LINEAR) ##interpolación bilineal
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_AREA) ##muestreo usando relación de area del pixel
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_LANCZOS4) ## interpolación de lanczos en vecindario de 8x8
# escalada = cv2.resize(imagen,(900,800), interpolation=cv2.INTER_LINEAR_EXACT) ## interpolación bilineal exacta de bits

# cv2.imshow('original',imagen)

# cv2.imshow('escalada',escalada)

# cv2.waitKey(0)
# cv2.destroyAllWindows()