from sklearn import svm 

X = [[0,0,0], [1,0,0], [0,1,0], [1,1,0], [0,0,1], [1,0,1]]
y = [0, 1, 1, 2, 10, 10]

modelo = svm.SVC()
modelo.fit(X, y)

puerta = 1
ventana = 1
flama = 1

Entrada = [puerta, ventana, flama]

respuesta = modelo.predict([Entrada])
print(respuesta[0])