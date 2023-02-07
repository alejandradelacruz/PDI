import cv2
path1 = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\1.png'
img1 = cv2.imread(path1)
img1 = cv2.resize(img1,(400,400))

path2 = r'C:\Users\User\Desktop\PDI\Operaciones_Imagenes\2.png'
img2 = cv2.imread(path2)
img2 = cv2.resize(img2,(400,400))

#Aplicamos las operaciones aritmeticas
resultadoSuma = cv2.add(img1, img2) #Realizamos la suma de imagenes
resultadoResta = cv2.subtract(img2,img1) #Realizamos la resta de imagenes 
resultadoMultiplicacion = cv2.multiply(img1,img2) #Realizamos la multiplicacion de imagenes 
resultadoDivision = cv2.divide(img1,img2) #Realizamos la division de imagenes 


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("resultadoSuma", resultadoSuma) 
cv2.imshow("resultadoResta", resultadoResta)
cv2.imshow("resultadoMultiplicacion", resultadoMultiplicacion)
cv2.imshow("resultadoDivision", resultadoDivision)

cv2.waitKey()
cv2.destroyAllWindows()