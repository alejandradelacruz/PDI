# Ciclos: Es una secuencia de instrucciones de codigo que se ejecuta repetidas veces, hatsa que la condicion 
# asignada a ese ciclo o bucle deje de cumplirse

#CICLO FOR: Se utiliza para recorrer los elementos de un objeto de un codigo iterable, ejemplo una lista, tupla o diccionario 

listaDeValores = [16, 20, 18, 5, 9, 23, 29]

#for valor in listaDeValores:
#    print(valor)
#print("\n")

#for valor in range(len(listaDeValores)):
#    print(listaDeValores[valor])

#suma = 0
#for valor in listaDeValores:
#    suma = suma + valor
#print(suma)

#for elemento in range(1,5):
#    print(elemento)

#for elemento in range(10):
#    print(elemento)

#for elemento in listaDeValores:
#    if elemento == 18:
#        print("Se ha encontrado un: ", elemento)
#        break; 
#    print(elemento)

if 18 in listaDeValores:
    print("Se ha encontrado un 18")
else:
    print("No se encontro el 18")