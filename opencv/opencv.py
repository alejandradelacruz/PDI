"""1. INTRODUCCION A OPENCV"""

import cv2 #Importamos la libreria opencv

#ruta
path = r'C:\Users\User\Desktop\PDI\opencv\1.jpeg'

##Utilizando el comando imread de opencv, leeremos la imagen 1.jpeg y la guardaremos en la variable img
#img = cv2.imread(path)

#Indicamos el nombre de la ventana donde se va a mostrar la imagen
#ventana = "img"

##Utilizando el comando imshow de opencv, mostraremos la imagen en una ventana llamada ventana1 
#cv2.imshow(ventana, img)

#El comando waitKey, controla el tiempo de muestreo de la señal de entrada por teclado 
#cv2.waitKey()

#El comando destroyAllWindows, destruye o cierra las ventanas creadas por opencv 
#cv2.destroyAllWindows()

#Guardamos la imagen contenida en la variable img en el archivo "iamgenGuardada1.jpeg"
#cv2.imwrite("imagenGuardad1.jpeg", img)

"""2. LEER IMAGENES EN ESCALA DE GRISES"""
#Mandamos llamar la imagen 1.jpeg en escala de grises y la guardamos en la variable img
"""img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
ventana1 = "img"
cv2.imshow(ventana1, img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("imagenGuardad2.jpeg", img)"""

"""3. JUGANDO CON waitKey y namedWindow"""
#imagen a color
#img = cv2.imread(path) 

#imagen en escala de grises
#img2 = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 

"""while True:
    cv2.imshow("color", img)
    cv2.imshow("grises", img2)

    key = cv2.waitKey()

    if key == ord("g"):
        cv2.imwrite("imagenguardada.png", img2)
    elif key == ord("c"):
        cv2.imwrite("imagenguardada3.png", img)
    else:
        break
cv2.destroyAllWindows()"""

## OTRA FORMA DE HACERLO
img = cv2.imread(path) 
img2 = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 

#cv2.imshow("ventana", img) #Mostramos la imagen en la ventana "ventana", es redimensionable pero no cambia su escala

#Comando para visualizar una imagen en pantalla completa 
#cv2.namedWindow("ventana", cv2.WND_PROP_FULLSCREEN) #Aplicamos la propiedad full screen a la ventana
#manera1: 
#cv2.setWindowProperty("ventana", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #Activamos la propiedad full screen 
#manera2: cv2.setWindowProperty("ventana", 0, 1)

#cv2.namedWindow("ventana", cv2.WINDOW_NORMAL) #Esta propiedad nos permite redimensionar la ventana
#cv2.namedWindow("ventana", cv2.WINDOW_AUTOSIZE) #Esta propiedad se ajusta al tamaño de la imagen

while True:
    key = cv2.waitKey()

    if key == ord("4"):
        cv2.imshow("ventana", img)
    elif key == ord("6"):
        cv2.imshow("ventana", img2)
    else:
        break;
cv2.destroyAllWindows()

