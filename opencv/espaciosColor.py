import cv2 #Importamos la libreria de opencv

"""ESPACIO DE COLOR RGB"""
#path = r'C:\Users\User\Desktop\PDI\opencv\1.jpeg'

#img = cv2.imread(path) #Se lee la imagen original

#B, G, R = cv2.split(img) #Separamos la imagen en sus 3 canales de color B G R 

#img2 = cv2.merge((B,G,R)) #Unimos los 3 canales y guardamos la imagen resultate

#Genera ventanas
#cv2.namedWindow("RGB", cv2.WINDOW_NORMAL)
#cv2.namedWindow("B", cv2.WINDOW_NORMAL)
#cv2.namedWindow("G", cv2.WINDOW_NORMAL)
#cv2.namedWindow("R", cv2.WINDOW_NORMAL)
#cv2.namedWindow("BGR", cv2.WINDOW_NORMAL)

#Muestra la imagen 
#cv2.imshow("RGB", img)
#cv2.imshow("B", B)
#cv2.imshow("G", G)
#cv2.imshow("R", R)
#cv2.imshow("BGR", img2)

#cv2.waitKey()
#cv2.destroyAllWindows()

"""ESPACIO DE COLOR HSV: es mayormente utilizado para la deteccion de objetos mediante color"""

#path = r'C:\Users\User\Desktop\PDI\opencv\1.jpeg'
#img = cv2.imread(path)

#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Hace el cambio de RGB a HSV

#h, s, v = cv2.split(hsv) #Dividimos los canales

#imprimir
#cv2.imshow("HSV", hsv)
#cv2.imshow("H", h)
#cv2.imshow("S", s)
#cv2.imshow("V", v)

#cv2.waitKey()
#cv2.destroyAllWindows()

"""CONVERSION ENTRE ESPACIOS DE COLOR"""
"""CONVERSION A ESCALA DE GRISES"""
path = r'C:\Users\User\Desktop\PDI\opencv\1.jpeg'
img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convertimos de RGB a escala de grises

cv2.imshow("RGB", img)
cv2.imshow("gray", gray)

cv2.waitKey()
cv2.destroyAllWindows()