#Sentencia If: es utilizada para ejecutar cierto bloque de codigo solo si se cumple la condicion deseada 
x = 1
# if x == 1: ##Si x es igual a 1, se ejecuta el codigo bajo el if
#    print("x es igual a 1")
# else:
#    print("x no es igual a 1")

#Sentencia elif: 
# if x == 1:
#    print("x es igual a 1")
# elif x == 1:
#    print("x es igual a 1")

# edad = int(input("Ingresa tu edad: "))
# if edad < 20:
#    print("No puedes acceder")
# else:
#    print("Puedes acceder")

# edad = int(input("Ingresa tu edad: "))
#if edad > 20 and edad < 30:
#    print("Puedes acceder")
# else:
#    print("No puedes acceder")
# print("\n")

edad = input("Ingresa tu edad: ")
if edad.isdigit(): #Evaluamos si el valor ingresado es un numero
    if int(edad) >= 20 and int(edad) <= 30:
        print("puedes acceder")
    else:
        print("no puedes acceder")
else:
    print("El valor ingresado no es numerico")
