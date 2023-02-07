import cv2

#Comando para leer una webCam
cap = cv2.VideoCapture(0) #Mandamos llamar la camara 0 y guardamos sus configuraciones en cap
conteo = 0 #Inicializamos un conteo en 0

while True: #Definimos un ciclo infinito 
    ret, frame = cap.read() #Leemos u obtenemos las capturas de la camara 

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Convertimos la captura a escala de grises 

    #ALGORITMO PARA OBTENER EL FONDO DE LA IMAGEN
    if conteo == 10: #Si el conteo es igual a 10 guarda la imagen como fondo
        fondo = gris #Fondo es igual a la imagen en escala de grises 
    
    if conteo > 10: #Si el conteo es mayor a 10 realiza lo siguiente 
        dif = cv2.absdiff(gris, fondo) #Realizamos la resta de el fondo a la imagen actual tomada 

        #Binarizacion de la imagen 
        _, imagenBinarizada = cv2.threshold(dif, 15, 255, cv2.THRESH_BINARY) #Realizamos la binarizacion de la imagen 

        #Adquirimos los contornos de la imagen 
        contornos, _ = cv2.findContours(imagenBinarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        for contorno in contornos:
            area = cv2.contourArea(contorno) #Calculamos el area del contorno 

            if area > 200:
                x,y,ancho,alto = cv2.boundingRect(contorno) #Obtenenos el rectangulo del contorno 
                cv2.rectangle(frame, (x,y), (x+ancho, y+alto), (0,255,0), 2) #Dibujamos el rectangulo en la imagen frame 
    
    cv2.imshow("Frame", frame) #Mostramos la imagen 
    conteo = conteo + 1 #Aumentamos el contador en 1 

    if cv2.waitKey(1) == 13: #13 --> Enter 
        break;

cap.release()
cv2.destroyAllWindows()

