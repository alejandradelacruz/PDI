import cv2 
import numpy as np

"""
matriz de transformacion de perspectiva 
      VERTICAL          HORIZONTAL
    | 1  Se  0 |       | 1   0  0 |    
    | 0  1   0 |       | Sh  1  0 |
    | 0  0   1 |       | 0   0  1 |
"""
"""FORMA 1"""
# tMatriz = np.array([[1, 0, 0], [1, 1, 0], [0, 1, 1]]) #Creamos la matriz de transformacion en HORIZONTAL y la guardamos en tMatriz
# #tMatriz = np.array([[1, 1, 0], [0, 1, 0], [0, 1, 1]]) #Creamos la matriz de transformacion en VERTICAL y la guardamos en tMatriz
# matrizResultante = np.zeros((500, 500, 3), np.uint8) #Creamos la matriz resultante en la que guardaremos la imagenes transformada

# path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\1.png'
# imagen = cv2.imread(path) #Leemos la imagen a transformar y la guardamos en la variable imagen 

# alto, ancho, _ = imagen.shape #Obtenemos la dimensiones altura y ancho de la imagen de entrada 

# for i in range(alto):
#     for j in range(ancho):
#         pixel = imagen[i,j] #Creamos el pixel que incrustaremos en la imagen transformada 
#         vector = np.array([j,i,1]) #Generamos el vector a transformar 
#         resultado = np.dot(tMatriz,vector) #Aplicamos el producto punto entre la matriz de transformacion y el vector
#         x = resultado[0] #Extraemos el componente x del vector resultante 
#         y = resultado[1] #Extraemos el componente y del vector resultante 
#         matrizResultante[y,x] = pixel #Reemplazamos el pixel original en la imagen transformda

# cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Escalada", cv2.WINDOW_NORMAL)

# cv2.imshow("Original", imagen) #Mostramos la imagen original
# cv2.imshow("Escalada", matrizResultante) #Mostramos la imagen resultante 

# cv2.waitKey() #Esperamos que se presiones cualquier tecla
# cv2.destroyAllWindows() #Mostramos la imagen resultante 

"""EJEMPLO DE TRANSFORMACION DE PERSPECTIVA"""
path = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\1.png'
imagen = cv2.imread(path)

alto, ancho, canal = imagen.shape #Obtenemos sus dimensiones 
cv2.namedWindow("imagen1", cv2.WINDOW_NORMAL) #Generamos una ventana con la que trabajaremos 

global listaPuntos
listaPuntos=[] 

#event, x, y, flags, params van por default
def obtenerPuntos(event, x, y, flags, params): #Construimos la funcion para trabajar cn cv2.setMouseallBack

    if event == cv2.EVENT_LBUTTONDBLCLK: #Leemos el evento del mouse, registrado por setMouseCallBack
            #Si event == doble click izquierda
            listaPuntos.append([x,y]) #Agregamos las posiciones de x,y y a una lista y esa lista le agregamos a listaPuntos

cv2.setMouseCallback("imagen1", obtenerPuntos) #Utilizamos la funcion setMouseCallBack

cv2.imshow("imagen1", imagen)

while True:
    if cv2.waitKey(0) == 13:
        print(listaPuntos)
        pts1 = np.float32(listaPuntos)
        pts2 = np.float32([[0,0], [ancho,0], [0,alto], [ancho,alto]])
        matriz = cv2.getPerspectiveTransform(pts1,pts2)
        resultadoImagen = cv2.warpPerspective(img, matriz, (ancho,alto))
        cv2.imshow("imagen1", resultadoImagen)
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()