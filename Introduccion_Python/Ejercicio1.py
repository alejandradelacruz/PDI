# Realizar un sistema que solicite 10 numeros, al final debe imprimir el promedio, suma y moda 
import operaciones 

lista = []
cuenta = 0

while cuenta < 10:
    cuenta = cuenta + 1
    numero = int(input("Ingresa un numero: "))
    lista.append(numero)
print(lista)

promedio,suma = operaciones.promedio(lista)
moda = operaciones.moda(lista)
print(promedio, suma, moda)