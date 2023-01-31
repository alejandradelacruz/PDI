import cv2
import numpy as np

imagenObscura = np.zeros((100,100,3), np.uint8) #Creamos una matriz de 3 dimensiones y la llenamos con ceros 
#(100,100,3) -> Imagen de 100 x 100 con 3 canales 

pixel = imagenObscura[97,97] #Obtenemos el valor del pixel en la posicion 97,97 de la matriz general 
"""Nos devuelve un vector de 3 elementos """
print(pixel) #Imprimimos el valor del pixel

imagenObscura[30,60] = [255, 255, 255] #Reemplazamos el valor del pixel en la posicon 97, 97 y lo hacemos de color blanco 
pixel = imagenObscura[30,60]
print(pixel) 

"""Obtener las dimensiones de la imagen generada, utilizaremos la funcion shape""" 
alto, largo, canales = imagenObscura.shape
print(alto, largo, canales)

"""Recorremos la imagen imprimiendo los valores de cada pixel"""
for i in range(largo):
    for j in range(alto):
        print(imagenObscura[i,j])

"""Modificar los valores de cada pixel"""
for i in range(largo):
    for j in range(alto):
        pixel = imagenObscura[i,j]
        if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
            imagenObscura[i,j] = [0,255,230]

cv2.namedWindow("block", cv2.WINDOW_NORMAL)
cv2.imshow("block", imagenObscura)

cv2.waitKey()
cv2.destroyAllWindows()

""" APLICAR SLICING A LISTAS Y VECTORES """
lista = [1,2,8,9,5,1,6,56,4,8]

for elemento in lista:
    print(elemento)

print(lista[:]) #Muestra toda la lista 
print (lista[0:]) #Muestra toda la lista desde la posicion 0 hasta el final
print((lista[5:])) #Muestra la lista desde la posicion 5 hasta el final
print(lista[::-1]) #Muestra toda la lista de forma descendente 

lista[5:] = [1,1,1,1,1,1]
print(lista) #Muestra toda lista y despues de la posicion 5 reemplaza los valores por '1'

lista[:] = [1,1,1,1,1,1]
print(lista)
print(lista[5:9])

"""TRABAJANDO CON LA IMAGEN CANDADOS.JPG"""
path = r'C:\Users\User\Desktop\PDI\opencv\candados.jpg'
img =cv2.imread(path) #Leemos la imagen de entrada y la guardamos en la variable img
alto, largo, _ = img.shape #Obtenemos las dimensiones de la imagen 
print(alto,largo) #Imprimimos sus dimensiones 

#Extraemos la imagen del candado 1
candado1 = img[0:alto, 0:int(largo/2)] #Obtenemos los pixeles comprendidos desde 0 al total del alto de la imagen 
# y asu vez hasta la mitad del largo de la misma.
candado2 = img[0:alto, int(largo/2):] #Obtenemos los pixeles comprendidos desde 0 al total del alto de la imagen 
# y asi vez desde la mitad del largo de la misma hasta el final del largo

#Generamos la imagen compuesta con las mismas dimensiones que la original y la rellenamos con ceros 
imagenCompuesta = np.zeros((alto, largo, 3), np.uint8)
#Rellenamos la imagen 
imagenCompuesta[0:alto, 0:int(largo/2)] = candado2 #Reemplazamos los pixeles de la primer mitad con la imagen del candado2 
imagenCompuesta[0:alto, int(largo/2):] = candado1 #Reemplazamos los pixeles de la segunda mitad con la imagen del candado1

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado1", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado2", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen Compuesta", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("candado1", candado1)
cv2.imshow("candado2", candado2)
cv2.imshow("Imagen Compuesta", imagenCompuesta)

cv2.waitKey()
cv2.destroyAllWindows()

"""TRABAJANDO CON EL COMANDO SELECT ROI"""
path = r'C:\Users\User\Desktop\PDI\opencv\candados.jpg'
img =cv2.imread(path) #Leemos la imagen de entrada y la guardamos en la variable img
imgCopy = img.copy()

alto, largo, canales = img.shape

cv2.namedWindow("ROI", cv2.WINDOW_NORMAL)

roi1 = cv2.selectROI("ROI", img)
print(roi1)

candado1 = img[int(roi1[1]) : int(roi1[1]+roi1[3]), int(roi1[0]) : int(roi1[0]+roi1[2])]
alto1, largo1, _ = candado1.shape
roi2 = cv2.selectROI("ROI", img)
print(roi2)

candado2 = img[int(roi2[1]) : int(roi2[1]+roi2[3]), int(roi2[0]) : int(roi2[0]+roi2[2])]
alto2, largo2, _ = candado2.shape

newCandado1 = cv2.resize(candado1, (largo2, alto2))
newCandado2 = cv2.resize(candado2, (largo1, alto1))

imgCopy[int(roi1[1]) : int(roi1[1]+ roi1[3]), int(roi1[0]) : int(roi1[0]+ roi1[2])] = newCandado2
imgCopy[int(roi2[1]) : int(roi2[1]+ roi2[3]), int(roi2[0]) : int(roi2[0]+ roi2[2])] = newCandado1                                                                
        

cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado1", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado2", cv2.WINDOW_NORMAL)
cv2.namedWindow("imgCompuesta", cv2.WINDOW_NORMAL)

cv2.imshow("original", img)
cv2.imshow("candado1", candado1)
cv2.imshow("candado2", candado2)
cv2.imshow("imgCompuesta", imgCopy)

cv2.waitKey()
cv2.destroyAllWindows()


