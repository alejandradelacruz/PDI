def promedio(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    promedio = suma / len(lista)

    return promedio,suma

def moda(lista):
    listaConteo = []
    for elemento in lista:
        cuenta = 0
        for elemento2 in lista:
            if elemento == elemento2:
                cuenta = cuenta + 1 
        listaConteo.append(cuenta)

    mayor = listaConteo[0]
    for elemento in listaConteo:
        if elemento > mayor:
            mayor = elemento
    
    for index in range(len(listaConteo)):
        if listaConteo[index] == mayor:
            moda = lista[index]
            break
    return moda