# Ser capaz de morganizar muchos datos relacionados, es una parte escencial de la ciencia de datos

# listas

# Los datos dentro de la lista se llaman elementos

tareas = ["Read", "workout", "code"]

print(tareas)

user = ["cmurillo", "Arauz", "jgamboa", 5, True]

temperaturas = [17,20,26,24]
temperaturas[2] = 35
print(temperaturas[2])


laps = [320,315,321]

laps.append(365)
laps.insert(1,319)
eliminado = laps.pop(0)

print(laps)
print("El elemento eliminado es:", eliminado)

# Recorrer listas por medio de un bucle

notas = [98,80,74,96,50,45]

for nota in notas:
    print(nota)

artistas = ["Roses", "Franco"]

for artista in artistas:
    print(artista)

# Para averiguar el numero de elementos que tiene una lista es con la palabra LEN

users = ["cmurillo", "Arauz", "jgamboa"]
conteo = len(users)
print(conteo)

# Podemos usar la longitud de la lista para crear declaraciones condicionales basadas en la cantidad de elementos como el anterior

if len(users) > 0:
    print("Empieza a trabajar")

lista_compras = ["papas", "fideos", "arroz"]
if len(lista_compras) > 0:
    print("La listas de compras es la siguiente: ")
    for arti in lista_compras:
        print(arti)
else:
    print("No tienes nada en tu lista de compras")