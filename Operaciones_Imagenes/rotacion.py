import cv2
import numpy as np

"""FORMA 1 """
# path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\2.png'
# imagen = cv2.imread(path) #Leemos la imagen a trsladar
# imagen2 = cv2.resize(imagen,(200,200))
# alto, ancho, _ = imagen2.shape #Obtenemos sus medidas

# angle = 90
# center = (ancho // 2, alto //2)
# scale = .2

# M = cv2.getRotationMatrix2D(center, angle, scale)
# print(M)

# imgT = np.zeros((alto+1,ancho+1,3), np.uint8) #Generamos una imagen base donde se guardara la imagen trasladada

# for i in range(alto): #Recorremos las filas de la matriz de la imagen 
#     for j in range(ancho): #Recorremos las columnas de la matriz de la imagen 
#         try:
#             px = np.array((j,i,1), np.uint8)
#             dot = np.dot(M,px)
#             x = int((dot[0]))
#             y = int((dot[1]))
#             imgT[y,x] = imagen2[i,j]
#         except:
#             pass

# cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("t", cv2.WINDOW_NORMAL)

# cv2.imshow("Original", imagen2)
# cv2.imshow("t", imgT)

# cv2.waitKey()
# cv2.destroyAllWindows()

"""FORMA 2"""
# path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\2.png'
# imagen = cv2.imread(path) #Leemos la imagen a trsladar
# imagen2 = cv2.resize(imagen,(200,200))
# alto, ancho, _ = imagen2.shape #Obtenemos sus medidas

# angle = 70
# center = (ancho // 2, alto //2)
# scale = 1

# M = cv2.getRotationMatrix2D(center, angle, scale)
# imgT = cv2.warpAffine(imagen2,M,(ancho,alto), borderValue=(255,255,255))

# cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("t", cv2.WINDOW_NORMAL)

# cv2.imshow("Original", imagen2)
# cv2.imshow("t", imgT)

# cv2.waitKey()
# cv2.destroyAllWindows()

"""FORMA 3"""
# import cv2
# import numpy as np
# import imutils


# imagen = cv2.imread("2.png") ## leemos la imagen a trasladar
# imagen2 = cv2.resize(imagen,(200,200)) ##la redimensionamos para efectos practicos
# alto, ancho, _ = imagen2.shape ##obtenemos sus medidas

# angle = 70
# center = (ancho//2, alto//2)

# imgT = imutils.rotate_bound(imagen2, angle , (255,255,255))#

# cv2.namedWindow("org", cv2.WINDOW_NORMAL)
# cv2.namedWindow("t", cv2.WINDOW_NORMAL)

# cv2.imshow("org", imagen2) ##mostramos la imagen redimensionada
# cv2.imshow("t",imgT) ##mostramos la imagen trasladada

# cv2.waitKey() ##esperamos que se presione cualquier tecla
# cv2.destroyAllWindows() ##se destruyen las centanas de opencv

"""FORMA 4"""
path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\2.png'
imagen = cv2.imread(path) #Leemos la imagen a trsladar
num_rows, num_cols = imagen.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 1)
img_rotation = cv2.warpAffine(imagen, rotation_matrix, (num_cols, num_rows))
cv2.imshow('Rotation', img_rotation)
cv2.waitKey()