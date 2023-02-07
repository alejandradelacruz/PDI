import cv2
import numpy as np 

#VECTOR DE TRASLACION 
# | 1  0  tx |    | x |    | x + tx |
# | 0  1  ty | *  | y | =  | y + ty |
# | 0  0  1  |    | 1 |    |   1    |

""" ----> FORMA 1 <---- """
path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\1.jpg' #Leemos la imagen a trasladar
imagen = cv2.imread(path)
imagen2 = cv2.resize(imagen, (100,50)) #Redimensionamos la imagen para efectos practicos 
alto, ancho, _ = imagen2.shape #Obtenemos las medidas de la imagen
print(alto)

tx = 10 #Definimos la traslacion en x
ty = 2 #Definimos la traslacion en y 

mT = np.array(([1, 0, tx], [0, 1, ty], [0, 0, 1]), np.uint8) #Creamos nuestra matriz de transformacion 
imgT = np.zeros((alto+ty, ancho+tx, 3), np.uint8) #Generamos una imagen base donde se guardara la imagen trasladad 

for i in range(alto): #Recorremos las filas de la matriz de la imagen
    for j in range(ancho): #Recorremos las columnas de la matriz de la imagen 
        px = np.array(([j,i,1]), np.uint8) #Formamos nuestro vector [px,py,1]
        dot = np.dot(mT,px) #Aplicamos producto punto entre la matriz de transformacion y el vector del pixel
        x = dot[0] #Extraemos el valor para x
        y = dot[1] #Extraemos el valor para y
        imgT[y,x] = imagen2[i,j] #[alto, ancho]: Reemplazamos los valores de los pixeles

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("traslacion", cv2.WINDOW_NORMAL)

cv2.imshow("Original", imagen2) #Mostramos la imagen redimensionada
cv2.imshow("traslacion", imgT) #Mostramos la imagen trasladada

cv2.waitKey()
cv2.destroyAllWindows()

""" ----> FORMA 2 <---- """
# path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\1.jpg' #Leemos la imagen a trasladar
# imagen = cv2.imread(path)
# imagen2 = cv2.resize(imagen, (100,50)) #Redimensionamos la imagen para efectos practicos 
# alto, ancho, _ = imagen2.shape #Obtenemos las medidas de la imagen
# print(alto)

# tx = 10 #Definimos la traslacion en x
# ty = 2 #Definimos la traslacion en y 

# mT = np.array(([1, 0, tx], [0, 1, ty], [0, 0, 1]), np.uint8) #Creamos nuestra matriz de transformacion 
# imgT = np.zeros((alto+ty, ancho+tx, 3), np.uint8) #Generamos una imagen base donde se guardara la imagen trasladada 

# for i in range(alto): #Recorremos las filas
#     for j in range(ancho): #Recorremos las columnas
#         x = j+tx #Sumamos el desplazamiento en x al indice de las columnas
#         y = i+ty #Sumamos el desplazamiento en y al indice de las filas
#         imgT[y,x] = imagen2[i,j] #Reemplazamos los pixeles en las imagenes 

# cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("traslacion", cv2.WINDOW_NORMAL)

# cv2.imshow("Original", imagen2) #Mostramos la imagen redimensionada
# cv2.imshow("traslacion", imgT) #Mostramos la imagen trasladada

# cv2.waitKey()
# cv2.destroyAllWindows()

"""UTILIZANDO ALGUNAS FUNCIONES DE OPENCV"""
# path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\1.jpg' #Leemos la imagen a trasladar
# imagen = cv2.imread(path)

# # Store height and width of the image
# height, width = imagen.shape[:2] #obtenemos las dimenciones de la imagen

# mT = np.float32([[1, 0, 100], [0, 1, 2]]) ##generamos la matriz de transformación

# ## utilizamos la función cv2.warpAffine(), esta recibe la imagen a trasladar, la matríz de transformación y las dimensiones originales de la imagen
# ##a trasladar, nos devuelve la imagen con la traslación aplicada
# imgT = cv2.warpAffine(imagen, mT, (width, height))

# cv2.imshow("Original", imagen) ##mostramos la imagen redimensionada
# cv2.imshow("traslacion",imgT) ##mostramos la imagen trasladada

# cv2.waitKey() ##esperamos que se presione cualquier tecla
# cv2.destroyAllWindows() ##se destruyen las centanas de opencv