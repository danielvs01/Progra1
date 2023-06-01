# Minimo y maximo, clasificaion de listas, sumando lista, como unir conjunto de datos y contar numeros de apariciones
# Ademas de utilizacion de instrumentos de cuerda y actualizacion de cadenas

numeros = [10,45,2,89,54,1,-3]
maximo = max(numeros)
minimo = min(numeros)
print(maximo)
print(minimo)
numeros.sort()
print(numeros)

nombres = ["Christopher", "Karla", "Daniel", "Erick"]
nombres.sort()
print(nombres)

# sumar listas

promedios = [85, 95, 65]
print(sum(promedios))

# unir listas o conjunto de datos

ventas_sab = [50,150,90,85]
ventas_dom = [250,300,100,900]
total = ventas_sab + ventas_dom
print(total)

# como saber la moda

pregunta1 = [1,1,1,1,4,4,5,3,5,4,3,2,5,2,2,3,4,1,1,5,1,4,1,3,1,2,3,4,5,2,1,2,5]
print(pregunta1.count(1))
print(3 in pregunta1)


# instrumentos de cuerda

nuevo_usuario = "Daniel Vidal Solano"
usuario_lista = nuevo_usuario.split()
print(usuario_lista)

direccion = "Barrio CTPBA, Buenos Aires, Puntarenas, Costa Rica, 60301"
nueva_direccion = direccion.replace("Barrio CTPBA", "Barrio del cole")
dataset_direccion = direccion.split(",")
print(dataset_direccion)
print(nueva_direccion)

